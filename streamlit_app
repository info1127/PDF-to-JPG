import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import zipfile
import io

st.set_page_config(page_title="PDF to JPG Converter", layout="wide")

st.title("📄 PDF to JPG Converter (Unlimited Upload)")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded!")

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:

        for file in uploaded_files:
            st.write(f"Processing: {file.name}")

            images = convert_from_bytes(file.read())

            for i, image in enumerate(images):
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='JPEG')

                file_name = f"{file.name}_page_{i+1}.jpg"
                zip_file.writestr(file_name, img_byte_arr.getvalue())

    st.download_button(
        label="📥 Download All JPG (ZIP)",
        data=zip_buffer.getvalue(),
        file_name="converted_images.zip",
        mime="application/zip"
    )
