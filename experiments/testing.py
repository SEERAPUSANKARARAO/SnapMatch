
from deepface import DeepFace
from PIL import Image
import shutil
import os

output_folder = "D:/@Projects_made/1_image/output"

if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

os.makedirs(output_folder)



uploaded_file = ["D:/@Projects_made/1_image/pic/gettyimages-2076186637-2048x2048.jpg"]
uploaded_db = ["D:/@Projects_made/1_image/pic/gettyimages-2076186637-2048x2048.jpg",
               "D:/@Projects_made/1_image/pic/gettyimages-2094628358-2048x2048.jpg",
               "D:/@Projects_made/1_image/pic/Nicolas-Cage-2009.webp",
               "D:/@Projects_made/1_image/pic/gettyimages-2076181995-2048x2048.jpg"]


models = ["SFace", "Facenet"]



new_image_directory = r'D:\@Projects_made\1_image\temp'
if os.path.exists(new_image_directory):
    shutil.rmtree(new_image_directory)

os.makedirs(new_image_directory)
for image_path in uploaded_file:
    # Open the image
    img = Image.open(image_path)
    
    # Get the image filename
    image_filename = os.path.basename(image_path)
    
    # Define the new image file path
    new_image_path_1 = os.path.join(new_image_directory, image_filename)
    
    # Save the image to the new directory
    img.save(new_image_path_1)

    print(f"Image saved to {new_image_path_1}")


new_directory = r'D:\@Projects_made\1_image\my_files'

# Create the new directory if it doesn't exist
os.makedirs(new_directory, exist_ok=True)

# Loop through each image path
for image_path in uploaded_db:
    img = Image.open(image_path)
    image_filename = os.path.basename(image_path)
    print("---------------------",image_filename)
    new_image_path = os.path.join(new_directory, image_filename)
    img.save(new_image_path)

    print(f"Image saved to {new_image_path}")

for model in models:
    # st.write(f"Model: {model}")

    dfs = DeepFace.find(
        img_path=new_image_path_1,
        db_path="D:/@Projects_made/1_image/my_files",
        model_name=model,
        enforce_detection=True
    )

    # Display results and save images to the output folde
    for i in range(len(dfs[0]['identity'])):
        image_path = dfs[0]['identity'][i]
        # Open the image
        image = Image.open(image_path)
        # Extract the filename
        filename = os.path.basename(image_path)
        # Define the output path for the image
        output_path = os.path.join(output_folder, filename)
        # Save the image to the output folder
        image.save(output_path)
        print(f"Image saved: {output_path}")




