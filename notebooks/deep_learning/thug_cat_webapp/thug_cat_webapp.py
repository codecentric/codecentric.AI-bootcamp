#
# WebApp mit starlette um in Katzenbildern Augen zu erkennen und eine Sonnebrille aufzusetzen
# Teil von bootcamp.codecentric.ai
#
# starten mit: python thug_cat_webapp.py

import uvicorn
import aiohttp
import base64

from fastai.vision import *
from starlette.routing import Route, Router
from starlette.templating import Jinja2Templates
from io import BytesIO

from transformer import CatTransformer


async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def upload(request):
    """
    Empfängt eine Datei via form POST request
    """
    data = await request.form()
    img_bytes = await (data["file"].read())
    return render_image_result(request, img_bytes)


async def process_url(request):
    """
    lädt eine Datei von einer angegebenen URL
    """
    img_bytes = await get_bytes(request.query_params["url"])
    return render_image_result(request, img_bytes)


def render_image_result(request, img_bytes):
    """
    Bekommt ein Bild als Bytes und macht eine prediction mit dem thug cat Modell.
    Dann zeigt es das Bild und die Landmarks auf einer HTML Seite an.
    """
    transform = CatTransformer("glasses.png", "../")
    img = open_image(BytesIO(img_bytes))
    orig_img = PIL.Image.open(BytesIO(img_bytes))

    img_glasses, landmarks = transform.put_on_glasses(img, orig_img)
    encoded = str(base64.b64encode(img_glasses._repr_png_()), 'utf-8')
    return templates.TemplateResponse("show.html", {'request': request,
                                                    'landmarks': landmarks,
                                                    'img': encoded
                                                    })


def form(request):
    """
    Zeigt ein HTML Formular via Template an.
    """
    return templates.TemplateResponse("index.html", {'request': request})


app = Router(
    [
        Route("/", endpoint=form, methods=["GET"]),
        Route("/process-url", endpoint=process_url, methods=["GET"]),
        Route("/upload", endpoint=upload, methods=["POST"]),

    ]
)

if __name__ == "__main__":
    templates = Jinja2Templates(directory='templates')
    uvicorn.run(app, host="0.0.0.0", port=8889)
