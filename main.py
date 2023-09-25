from libraries import *
app = FastAPI()

# @app.get("/")
# def welcome():
#     return {"message": 'api Hello world '}


origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])


@app.post('/conversion')
async def pdf_to_base64Image(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()

        images = convert_from_bytes(pdf_bytes, poppler_path=poppler_path)

        base64_images = []
        for i, image in enumerate(images):
            img_byte_array = io.BytesIO()
            image.save(img_byte_array, format='PNG')
            img_byte_array = img_byte_array.getvalue()
            base64_image = base64.b64encode(img_byte_array).decode('utf-8')
            width, height = image.size
            base64_images.append({
                "page": i + 1,
                "base64": base64_image,
                "width": width,
                "height": height
            })

        return {"pages": base64_images}
    except Exception as e:
        return {"error": str(e)}


def convert_to_base64(images):
    base64_images = []
    print(type(images))
    for i, image in enumerate(images):
        img_data = image_to_base64(image)
        base64_images.append({"page": i+1, "base64": img_data})
    return base64_images


def image_to_base64(image):
    img_byte_array = image.convert('RGB').tobytes()
    base64_data = base64.b64encode(img_byte_array).decode('utf-8')
    return base64_data
