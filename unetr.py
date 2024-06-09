import streamlit as st
import sys
import os
from PIL import Image
import PyPDF2
import tensorflow as tf
import numpy  as np
import cv2
import patchify
from metrics import dice_coef,dice_loss
sys.path.append('C:/strhackprix')
st.page_link("frontstr.py", label="Home", icon="🏠")
st.title("CT Scan Segmentation")





st.write("This is the CT scan segment page.")
    
    # CSS for styling
st.markdown("""
        <style>
        body {
            font-family: Arial, sans-serif;
            background: url('https://i.pinimg.com/736x/71/0e/f5/710ef5f9e67adb0033e3278fafdff440.jpg');
            background-size: cover;
            color: #343a40;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background-color: #007bff;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            color: #fff;
        }

        section {
            margin-top: 20px;
        }

        section h2 {
            color: #007bff;
        }

        footer {
            margin-top: 20px;
            text-align: center;
            color: #555;
        }

        .response-image img {
            max-width: 100%;
            height: auto;
        }
        </style>
        """, unsafe_allow_html=True)

    # Header
st.markdown('<header><h1>Upload CT Scan</h1></header>', unsafe_allow_html=True)

    # File upload section
st.markdown('<section><h2>Select a PDF file (Max size: 200MB)</h2></section>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False)

    # Process the file upload
if uploaded_file is not None:
        file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
        st.write(file_details)
        
        
        
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
            file_buffer = uploaded_file.getbuffer()

    # Convert the buffer to a NumPy array
            file_bytes = np.frombuffer(file_buffer, dtype=np.uint8)

    # Decode the image from the buffer
            image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            cf = {}
            cf["image_size"] = 256
            cf["num_channels"] = 3

            cf["patch_size"] = 32
            cf["num_patches"] = (cf["image_size"]*2)//(cf["patch_size"]*2)
            cf["flat_patches_shape"] = (
                cf["num_patches"],
                cf["patch_size"]*cf["patch_size"]*cf["num_channels"]
            )
            st.success("PDF file uploaded successfully!")
            model_path = os.path.join("C:\strhackprix", "model.h5")
            with tf.keras.utils.custom_object_scope({'dice_loss': dice_loss,'dice_coef':dice_coef}):
                model = tf.keras.models.load_model(model_path, custom_objects={"dice_coef":dice_coef,"dice_loss": dice_loss})
            
            image = cv2.resize(image, (cf["image_size"], cf["image_size"]))
            x = image / 255.0

            patch_shape = (cf["patch_size"], cf["patch_size"], cf["num_channels"])
            patches = patchify(x, patch_shape, cf["patch_size"])
            patches = np.reshape(patches, cf["flat_patches_shape"])
            patches = patches.astype(np.float32)
            patches = np.expand_dims(patches, axis=0)
            pred = model.predict(patches, verbose=0)[0]
            orange = (0, 165, 255)
            orange1= np.full((cf["image_size"], cf["image_size"], 3), orange, dtype=np.uint8)
            masked_image = cv2.bitwise_and(image,orange1, mask=pred)
            pred = np.concatenate([pred, pred, pred], axis=-1)
            rgb_image = cv2.cvtColor(pred, cv2.COLOR_BGR2RGB)

            """ Save final mask """
            
            
            save_image_path = os.path.join("results", "response.png")
            cv2.imwrite(save_image_path,rgb_image)
            

            # Display a response image (replace with your own image processing logic)
            # Assuming 'response.png' is the image you want to display
            if os.path.exists("response.png"):
                image = Image.open("response.png")
                st.image(image, caption='Response Image', use_column_width=True)

    # Footer
st.markdown('<footer><p>&copy; AM^2</p></footer>', unsafe_allow_html=True)
