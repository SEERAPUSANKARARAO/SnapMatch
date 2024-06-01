import streamlit as st
from PIL import Image
import os
from src.snapmatcher import process_images
    
def main():
    st.title("SnapMatch")

    uploaded_input_file = st.sidebar.file_uploader("Upload Input Image", type=["jpg", "jpeg", "png", "webp"])
    uploaded_db_files = st.sidebar.file_uploader("Upload Database Images", type=["jpg", "jpeg", "png", "webp"], accept_multiple_files=True)
    if st.sidebar.button("Process Images"):
        if uploaded_input_file is not None and uploaded_db_files is not None:
            process_images(uploaded_input_file, uploaded_db_files)
            verified_images = os.listdir("./output")
            for image_filename in verified_images:
                image_path = os.path.join("./output", image_filename)
                image = Image.open(image_path)
                st.image(image, caption=image_filename)
        else:
            st.warning("Please upload an input image and database images.")

if __name__ == "__main__":
    main()
