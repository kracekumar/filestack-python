import filestack.models
from filestack import config
from filestack.uploads.external_url import upload_external_url
from filestack.trafarets import STORE_LOCATION_SCHEMA, STORE_SCHEMA
from filestack import utils
from filestack.utils import requests
from filestack.uploads import intelligent_ingestion
from filestack.uploads.multipart import multipart_upload


class Client:
    """
    The hub for all Filestack operations. Creates Filelinks, converts external urls
    to Transformation objects, takes a URL screenshot and returns zipped files.
    """
    def __init__(self, apikey, security=None, storage='S3'):
        """
        Args:
            apikey (str): The path of the file to wrap
            storage (str): default storage to be used for uploads (one of S3, `gcs`, dropbox, azure)
            security (:class:`filestack.Security`): Security object that will be used by default
                for all API calls
        """
        self.apikey = apikey
        self.security = security
        STORE_LOCATION_SCHEMA.check(storage)
        self.storage = storage

    def transform_external(self, external_url):
        """
        Turns an external URL into a Filestack Transformation object

        >>> t_obj = client.transform_external('https://image.url')
        >>> t_obj.resize(width=800)  # now you can do this

        Args:
            external_url (str): file URL

        Returns:
            :class:`filestack.Transformation`
        """
        return filestack.models.Transformation(apikey=self.apikey, security=self.security, external_url=external_url)

    def urlscreenshot(self, external_url, agent=None, mode=None, width=None, height=None, delay=None):
        """
        Takes a 'screenshot' of the given URL

        Args:
            external_url (str): URL
            agent (str): one of: :data:`"desktop"` :data:`"mobile"`
            mode (str): one of: :data:`"all"` :data:`"window"`
            width (int): screen width
            height (int): screen height

        Returns:
            :class:`filestack.Transformation`
        """
        params = locals()
        params.pop('self')
        params.pop('external_url')

        params = {k: v for k, v in params.items() if v is not None}

        url_task = utils.return_transform_task('urlscreenshot', params)

        new_transform = filestack.models.Transformation(
            self.apikey, security=self.security, external_url=external_url
        )
        new_transform._transformation_tasks.append(url_task)

        return new_transform

    def zip(self, destination_path, file_handles, security=None):
        """
        Takes array of handles and downloads a compressed ZIP archive
        to provided path

        Args:
            destination_path (str): path where the ZIP file should be stored
            file_handles (list): list of filelink handles and/or URLs
            security (:class:`filestack.Security`): Security object that will be used
                for this API call

        Returns:
            int: ZIP archive size in bytes
        """
        url_parts = [config.CDN_URL, self.apikey, 'zip', '[{}]'.format(','.join(file_handles))]
        sec = security or self.security
        if sec is not None:
            url_parts.insert(3, sec.as_url_string())
        zip_url = '/'.join(url_parts)
        total_bytes = 0
        with open(destination_path, 'wb') as f:
            response = requests.get(zip_url, stream=True)
            for chunk in response.iter_content(5 * 1024 ** 2):
                f.write(chunk)
                total_bytes += len(chunk)

        return total_bytes

    def upload_url(self, url, store_params=None, security=None):
        """
        Uploads local file from external url

        Args:
            url (str): file URL
            store_params (dict): store parameters to be used during upload
            security (:class:`filestack.Security`): Security object that will be used
                for this API call

        Returns:
            :class:`filestack.Filelink`: new Filelink object
        """
        handle = upload_external_url(url, self.apikey, store_params, security=security or self.security)
        return filestack.models.Filelink(handle=handle)

    def upload(self, filepath=None, file_obj=None, store_params=None, intelligent=False):
        """
        Uploads local file or file-like object.

        Args:
            filepath (str): path to file
            file_obj (io.BytesIO or similar): file-like object
            store_params (dict): store parameters to be used during upload
            intelligent (bool): upload file using Filestack Intelligent Ingestion

        Returns:
            :class:`filestack.Filelink`: new Filelink object

        Important:
            fix this
        """
        # TODO: add security to metho arguments

        if store_params:  # Check the structure of parameters
            STORE_SCHEMA.check(store_params)

        upload_method = multipart_upload
        if intelligent:
            upload_method = intelligent_ingestion.upload

        response_json = upload_method(
            self.apikey, filepath, file_obj, self.storage, params=store_params, security=self.security
        )

        handle = response_json['handle']
        return filestack.models.Filelink(handle, apikey=self.apikey, security=self.security)
