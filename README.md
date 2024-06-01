# SnapMatch

SnapMatch is an image processing application that leverages DeepFace for facial recognition and similarity matching. This application allows users to upload a single input image and a set of database images. It then processes these images to find matches and displays the results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)


## Installation

To run SnapMatch, you need to have Python installed on your system. Follow the steps below to set up the project:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/SEERAPUSANKARARAO/SnapMatch.git
   cd snapmatch
   ```

2. **Set up the virtual environment:**

   ```sh
   python -m venv imge_find_env
   source imge_find_env/bin/activate  # On Windows use `imge_find_env\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, use the following command:

```sh
streamlit run stremlit_app_v1.py
```

After running the command, the application will be accessible in your web browser at `http://localhost:8501`. Follow the on-screen instructions to upload an input image and multiple database images, then click the "Process Images" button to see the results.

## Folder Structure

```plaintext
SnapMatch
├── .gitignore
├── app.py
├── folder_structure.txt
├── requirements.txt
├── setup.py
├── stremlit_app_v1.py
├── experiments
│   ├── test.ipynb
│   ├── testing.py
│   ├── test_case_2.py
├── imge_find_env
│   ├── package_info.json
│   ├── pyvenv.cfg
│   ├── README.md
│   ├── requirements.txt
├── my_files
│   ├── ds_model_facenet_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_sface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── gettyimages-2076181995-2048x2048.jpg
│   ├── gettyimages-2076186637-2048x2048.jpg
│   ├── gettyimages-2076186638-2048x2048.jpg
│   ├── gettyimages-2076235215-2048x2048.jpg
│   ├── gettyimages-2076237818-2048x2048.jpg
│   ├── gettyimages-2076870233-2048x2048.jpg
│   ├── gettyimages-2076870235-2048x2048.jpg
│   ├── gettyimages-2076870237-2048x2048.jpg
│   ├── gettyimages-2076870238-2048x2048.jpg
│   ├── gettyimages-2081604885-2048x2048.jpg
│   ├── gettyimages-2081619340-2048x2048.jpg
│   ├── gettyimages-2081619343-2048x2048.jpg
│   ├── gettyimages-2094627820-2048x2048.jpg
│   ├── gettyimages-2094627821-2048x2048.jpg
│   ├── gettyimages-2094628357-2048x2048.jpg
│   ├── gettyimages-2094628358-2048x2048.jpg
│   ├── gettyimages-2094628884-2048x2048.jpg
│   ├── gettyimages-2094629415-2048x2048.jpg
│   ├── gettyimages-2094629950-2048x2048.jpg
│   ├── gettyimages-2094633218-2048x2048.jpg
│   ├── gettyimages-2094634201-2048x2048.jpg
│   ├── gettyimages-2094701666-2048x2048.jpg
│   ├── KilianParis_Cannes_SayWho_SherazDebbich_2023-6935.jpg-768x1152.jpeg
│   ├── Nicolas-Cage-2009.webp
├── output
│   ├── gettyimages-2081604885-2048x2048.jpg
├── pic
│   ├── ds_model_arcface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_deepface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_deepid_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_dlib_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_facenet512_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_facenet_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_ghostfacenet_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_openface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_sface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── ds_model_vggface_detector_opencv_aligned_normalization_base_expand_0.pkl
│   ├── gettyimages-2076181995-2048x2048.jpg
│   ├── gettyimages-2076186637-2048x2048.jpg
│   ├── gettyimages-2076186638-2048x2048.jpg
│   ├── gettyimages-2076235215-2048x2048.jpg
│   ├── gettyimages-2076237818-2048x2048.jpg
│   ├── gettyimages-2076870233-2048x2048.jpg
│   ├── gettyimages-2076870235-2048x2048.jpg
│   ├── gettyimages-2076870237-2048x2048.jpg
│   ├── gettyimages-2076870238-2048x2048.jpg
│   ├── gettyimages-2081604885-2048x2048.jpg
│   ├── gettyimages-2081619340-2048x2048.jpg
│   ├── gettyimages-2081619343-2048x2048.jpg
│   ├── gettyimages-2094627820-2048x2048.jpg
│   ├── gettyimages-2094627821-2048x2048.jpg
│   ├── gettyimages-2094628357-2048x2048.jpg
│   ├── gettyimages-2094628358-2048x2048.jpg
│   ├── gettyimages-2094628884-2048x2048.jpg
│   ├── gettyimages-2094629415-2048x2048.jpg
│   ├── gettyimages-2094629950-2048x2048.jpg
│   ├── gettyimages-2094633218-2048x2048.jpg
│   ├── gettyimages-2094634201-2048x2048.jpg
│   ├── gettyimages-2094701666-2048x2048.jpg
│   ├── KilianParis_Cannes_SayWho_SherazDebbich_2023-6935.jpg-768x1152.jpeg
│   ├── Nicolas-Cage-2009.webp
├── src
│   ├── snapmatcher.py
│   ├── __init__.py
├── temp
│   ├── Robert_Downey_Jr.webp
├── testing_images_1
│   ├── gettyimages-2076186637-2048x2048.jpg
│   ├── gettyimages-2094628358-2048x2048.jpg
│   ├── Nicolas-Cage-2009.webp
├── test_images
    ├── Robert_Downey_Jr.webp
```
