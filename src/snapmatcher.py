from deepface import DeepFace
from PIL import Image
import shutil
import os

def process_images(input_file, db_files):
    output_folder = "D:/@Projects_made/1_image/output"
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)

    new_image_directory =r'D:\@Projects_made\1_image\temp'
    if os.path.exists(new_image_directory):
        shutil.rmtree(new_image_directory)
    os.makedirs(new_image_directory) 
    img = Image.open(input_file)
    new_image_path = os.path.join(new_image_directory, input_file.name)
    img.save(new_image_path)

    # Save uploaded database files to a directory
    db_directory = r'D:\@Projects_made\1_image\my_files'
    if os.path.exists(db_directory):
        shutil.rmtree(db_directory)
    os.makedirs(db_directory)
    for image_path in db_files:
        img = Image.open(image_path)
        new_image_path = os.path.join(db_directory, image_path.name)
        img.save(new_image_path)

    models = ["SFace", "Facenet"]

    for model in models:
        dfs = DeepFace.find(
            img_path=new_image_path,
            db_path=db_directory,
            model_name=model,
            enforce_detection=True
        )

        for i in range(len(dfs[0]['identity'])):
            image_path = dfs[0]['identity'][i]
            image = Image.open(image_path)
            filename = os.path.basename(image_path)
            output_path = os.path.join(output_folder, filename)
            image.save(output_path)