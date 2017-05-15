import pytest

from filestack import Transform
from filestack.config import CDN_URL

APIKEY = 'SOMEAPIKEY'
HANDLE = 'SOMEHANDLE'
EXTERNAL_URL = 'SOMEEXTERNALURL'


@pytest.fixture
def transform():
    return Transform(apikey=APIKEY, external_url=EXTERNAL_URL)


def test_sanity(transform):
    assert transform.apikey == APIKEY
    assert transform.external_url == EXTERNAL_URL
    assert hasattr(transform, 'delete')


def test_resize(transform):
    target_url = '{}/{}/resize=height:500,width:500/{}'.format(CDN_URL,
                                                               APIKEY,
                                                               EXTERNAL_URL)
    resize = transform.resize(width=500, height=500)
    assert resize.get_transformation_url() == target_url


def test_crop(transform):
    target_url = '{}/{}/crop=dim:500/{}'.format(CDN_URL,
                                                APIKEY,
                                                EXTERNAL_URL)
    crop = transform.crop(dim=500)
    assert crop.get_transformation_url() == target_url


def test_rotate(transform):
    target_url = '{}/{}/rotate=deg:90/{}'.format(CDN_URL,
                                                 APIKEY,
                                                 EXTERNAL_URL)
    rotate = transform.rotate(deg=90)
    assert rotate.get_transformation_url() == target_url


def test_flip(transform):
    target_url = '{}/{}/flip/{}'.format(CDN_URL,
                                        APIKEY,
                                        EXTERNAL_URL)
    flip = transform.flip()
    assert flip.get_transformation_url() == target_url


def test_flop(transform):
    target_url = '{}/{}/flop/{}'.format(CDN_URL,
                                        APIKEY,
                                        EXTERNAL_URL)
    flop = transform.flop()
    assert flop.get_transformation_url() == target_url


def test_watermark(transform):
    target_url = '{}/{}/watermark=file:somefile.jpg/{}'.format(CDN_URL,
                                                               APIKEY,
                                                               EXTERNAL_URL)
    watermark = transform.watermark(file="somefile.jpg")
    assert watermark.get_transformation_url() == target_url


def test_detect_faces(transform):
    target_url = '{}/{}/detect_faces=minsize:100/{}'.format(CDN_URL,
                                                            APIKEY,
                                                            EXTERNAL_URL)
    detect_faces = transform.detect_faces(minsize=100)
    assert detect_faces.get_transformation_url() == target_url


def test_crop_faces(transform):

    target_url = '{}/{}/crop_faces=width:100/{}'.format(CDN_URL,
                                                        APIKEY,
                                                        EXTERNAL_URL)
    crop_faces = transform.crop_faces(width=100)
    assert crop_faces.get_transformation_url() == target_url


def test_pixelate_faces(transform):
    target_url = '{}/{}/pixelate_faces=minsize:100/{}'.format(CDN_URL,
                                                              APIKEY,
                                                              EXTERNAL_URL)
    pixelate_faces = transform.pixelate_faces(minsize=100)
    assert pixelate_faces.get_transformation_url() == target_url


def test_round_corners(transform):
    target_url = '{}/{}/round_corners=radius:100/{}'.format(CDN_URL,
                                                            APIKEY,
                                                            EXTERNAL_URL)
    round_corners = transform.round_corners(radius=100)
    assert round_corners.get_transformation_url() == target_url


def test_vignette(transform):
    target_url = '{}/{}/vignette=amount:50/{}'.format(CDN_URL,
                                                      APIKEY,
                                                      EXTERNAL_URL)
    vignette = transform.vignette(amount=50)
    assert vignette.get_transformation_url() == target_url


def test_polaroid(transform):
    target_url = '{}/{}/polaroid=color:blue/{}'.format(CDN_URL,
                                                       APIKEY,
                                                       EXTERNAL_URL)
    polaroid = transform.polaroid(color='blue')
    assert polaroid.get_transformation_url() == target_url


def test_torn_edges(transform):
    target_url = '{}/{}/torn_edges/{}'.format(CDN_URL,
                                              APIKEY,
                                              EXTERNAL_URL)
    torn_edges = transform.torn_edges()
    assert torn_edges.get_transformation_url() == target_url


def test_shadow(transform):
    target_url = '{}/{}/shadow=blur:true/{}'.format(CDN_URL,
                                                    APIKEY,
                                                    EXTERNAL_URL)
    shadow = transform.shadow(blur=True)
    assert shadow.get_transformation_url() == target_url


def test_circle(transform):
    target_url = '{}/{}/circle=background:true/{}'.format(CDN_URL,
                                                          APIKEY,
                                                          EXTERNAL_URL)
    circle = transform.circle(background=True)
    assert circle.get_transformation_url() == target_url


def test_border(transform):
    target_url = '{}/{}/border=width:500/{}'.format(CDN_URL,
                                                    APIKEY,
                                                    EXTERNAL_URL)
    border = transform.border(width=500)
    assert border.get_transformation_url() == target_url


def test_sharpen(transform):
    target_url = '{}/{}/sharpen=amount:50/{}'.format(CDN_URL,
                                                     APIKEY,
                                                     EXTERNAL_URL)
    sharpen = transform.sharpen(amount=50)
    assert sharpen.get_transformation_url() == target_url


def test_blur(transform):
    target_url = '{}/{}/blur=amount:10/{}'.format(CDN_URL,
                                                  APIKEY,
                                                  EXTERNAL_URL)
    blur = transform.blur(amount=10)
    assert blur.get_transformation_url() == target_url


def test_monochrome(transform):
    target_url = '{}/{}/monochrome/{}'.format(CDN_URL,
                                              APIKEY,
                                              EXTERNAL_URL)
    monochrome = transform.monochrome()
    assert monochrome.get_transformation_url() == target_url


def test_blackwhite(transform):
    target_url = '{}/{}/blackwhite=threshold:50/{}'.format(CDN_URL,
                                                           APIKEY,
                                                           EXTERNAL_URL)
    blackwhite = transform.blackwhite(threshold=50)
    assert blackwhite.get_transformation_url() == target_url


def test_sepia(transform):
    target_url = '{}/{}/sepia=tone:80/{}'.format(CDN_URL,
                                                 APIKEY,
                                                 EXTERNAL_URL)
    sepia = transform.sepia(tone=80)
    assert sepia.get_transformation_url() == target_url


def test_pixelate(transform):
    target_url = '{}/{}/pixelate=amount:10/{}'.format(CDN_URL,
                                                      APIKEY,
                                                      EXTERNAL_URL)
    pixelate = transform.pixelate(amount=10)
    assert pixelate.get_transformation_url() == target_url


def test_oil_paint(transform):
    target_url = '{}/{}/oil_paint=amount:10/{}'.format(CDN_URL,
                                                       APIKEY,
                                                       EXTERNAL_URL)
    oil_paint = transform.oil_paint(amount=10)
    assert oil_paint.get_transformation_url() == target_url


def test_negative(transform):
    target_url = '{}/{}/negative/{}'.format(CDN_URL,
                                            APIKEY,
                                            EXTERNAL_URL)
    negative = transform.negative()
    assert negative.get_transformation_url() == target_url


def test_modulate(transform):
    target_url = '{}/{}/modulate=brightness:155,hue:155,saturation:155/{}'.format(CDN_URL,
                                                                                  APIKEY,
                                                                                  EXTERNAL_URL)
    modulate = transform.modulate(brightness=155, hue=155, saturation=155)
    assert modulate.get_transformation_url() == target_url


def test_partial_pixelate(transform):
    target_url = ('{}/{}/partial_pixelate=amount:10,blur:10,'
                  'objects:[[x,y,width,height],[x,y,width,height]],type:rect/{}').format(CDN_URL,
                                                                                         APIKEY,
                                                                                         EXTERNAL_URL)

    partial_pixelate = transform.partial_pixelate(amount=10, blur=10,
                                                  type='rect', objects='[[x,y,width,height],[x,y,width,height]]')
    assert partial_pixelate.get_transformation_url() == target_url


def test_partial_blur(transform):
    target_url = ('{}/{}/partial_blur=amount:10,blur:10,'
                  'objects:[[x,y,width,height],[x,y,width,height]],type:rect/{}').format(CDN_URL,
                                                                                         APIKEY,
                                                                                         EXTERNAL_URL)

    partial_blur = transform.partial_blur(amount=10, blur=10,
                                          type='rect', objects='[[x,y,width,height],[x,y,width,height]]')
    assert partial_blur.get_transformation_url() == target_url


def test_collage(transform):
    target_url = ('{}/{}/collage=autorotate:true,color:white,'
                  'files:[FILEHANDLE,FILEHANDLE2,FILEHANDLE3],fit:crop,'
                  'height:1000,margin:50,width:1000/{}').format(CDN_URL,
                                                                APIKEY,
                                                                EXTERNAL_URL)

    collage = transform.collage(files='[FILEHANDLE,FILEHANDLE2,FILEHANDLE3]',
                                margin=50, width=1000, height=1000, color='white',
                                fit='crop', autorotate=True)
    assert collage.get_transformation_url() == target_url


def test_upscale(transform):
    target_url = '{}/{}/upscale=noise:low,style:artwork/{}'.format(CDN_URL, APIKEY, EXTERNAL_URL)
    upscale = transform.upscale(noise='low', style='artwork')
    assert upscale.get_transformation_url() == target_url


def test_enhance(transform):
    target_url = '{}/{}/enhance/{}'.format(CDN_URL,
                                           APIKEY,
                                           EXTERNAL_URL)
    enhance = transform.enhance()
    assert enhance.get_transformation_url() == target_url


def test_redeye(transform):
    target_url = '{}/{}/redeye/{}'.format(CDN_URL,
                                          APIKEY,
                                          EXTERNAL_URL)
    redeye = transform.redeye()
    assert redeye.get_transformation_url() == target_url


def test_urlscreenshot(transform):
    target_url = ('{}/{}/urlscreenshot=agent:desktop,delay:3000,'
                  'height:1080,mode:window,width:1920/{}').format(CDN_URL,
                                                                  APIKEY,
                                                                  EXTERNAL_URL)

    urlscreenshot = transform.urlscreenshot(agent='desktop', mode='window', width=1920, height=1080, delay=3000)
    assert urlscreenshot.get_transformation_url() == target_url


def test_ascii(transform):
    target_url = '{}/{}/ascii=background:black,colored:true,foreground:black,reverse:true,size:100/{}'.format(CDN_URL,
                                                                                                              APIKEY,
                                                                                                              EXTERNAL_URL)

    ascii = transform.ascii(background='black', foreground='black', colored=True, size=100, reverse=True)
    assert ascii.get_transformation_url() == target_url
