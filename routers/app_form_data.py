from fastapi import APIRouter, Form, File, UploadFile
from typing import Annotated

from fastapi.responses import HTMLResponse


app_form_data_router = APIRouter()


@app_form_data_router.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

@app_form_data_router.post("/file/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app_form_data_router.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}

@app_form_data_router.post("/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"file_sizes": [len(file) for file in files]}


@app_form_data_router.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}


@app_form_data_router.post("/files2/")
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()] = "asd",
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app_form_data_router.get("/")
async def main():
    content = """
<body>
<form action="/form-data/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
</form>
<form action="/form-data/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
</form>

<form action="/form-data/files2/" enctype="multipart/form-data" method="post">
    files 2
    <input name="file" type="file">
    <input name="fileb" type="file">
    <input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)