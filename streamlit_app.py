import streamlit as st
import fitz  # PyMuPDF
import zipfile
import io

st.title("PDF to JPG Converter")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:

        for file in uploaded_files:
            pdf = fitz.open(stream=file.read(), filetype="pdf")

            for page_num in range(len(pdf)):
                page = pdf.load_page(page_num)
                pix = page.get_pixmap()

                img_bytes = pix.tobytes("jpg")
                file_name = f"{file.name}_page_{page_num+1}.jpg"

                zip_file.writestr(file_name, img_bytes)

    st.download_button(
        "Download ZIP",
        zip_buffer.getvalue(),
        file_name="images.zip"
    )
