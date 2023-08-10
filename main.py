from libraries import *
app = FastAPI()

# @app.get("/")
# def welcome():
#     return {"message": 'api Hello world '}


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])


@app.post('/conversion')
async def Pdf_to_image(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()
        images = convert_from_bytes(pdf_bytes)
        image_urls = saveImage(images)
        return {"url": image_urls}
    except Exception as e:
        return {"error": str(e), "type": type(e).__name__}

# save the images to desktop and return their urls


def saveImage(image):
    image_urls = []
    for i, image in enumerate(image):
        image_path = f'image_{i}.png'
        # Create the static folder (dir) if it does not exist
        if not os.path.exists('static'):
            os.mkdir('static')
        image.save(f'static/{image_path}', "PNG")
        image_urls.append(image_path)
    return image_urls
