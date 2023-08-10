
from fastapi import FastAPI, File, UploadFile
import uvicorn
from pdf2image import convert_from_bytes
import os
from starlette.middleware.cors import CORSMiddleware
