import streamlit as st
import pypdfium2 as pdfium
import io
import zipfile

st.set_page_config(page_title="PDF to JPG Converter", layout="centered")

st.title("📄 PDF to JPG Converter")
st.write("Upload your PDF files and download all pages as JPG in a ZIP file.")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded!")

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:

        for file in uploaded_files:
            pdf = pdfium.PdfDocument(file.read())

            for page_index in range(len(pdf)):
                page = pdf[page_index]
                image = page.render(scale=2).to_pil()

                img_buffer = io.BytesIO()
                image.save(img_buffer, format="JPEG")

                file_name = f"{file.name}_page_{page_index + 1}.jpg"
                zip_file.writestr(file_name, img_buffer.getvalue())

    st.download_button(
        label="📥 Download All JPG (ZIP)",
        data=zip_buffer.getvalue(),
        file_name="converted_images.zip",
        mime="application/zip"
    )
