import streamlit as st
import os
from PIL import Image
import subprocess
import requests

# Define each page as a separate function
def main_page():
    st.title("Medical imaging analyzer")
    st.write("")
    # Add buttons for navigation
    # if st.button("Go to CT Scan Segment",key="button 1"):
    #     # st.session_state.page = "CT Scan Segment"
    #     st.switch_page("pages/unetr.py")

    if st.button("Go to Analyze Response",key="button 2"):
        # st.session_state.page = "Analyze Response"
        command = "python -m streamlit run app.py --server.port 8502"
        result = subprocess.run(command,shell=True, capture_output=True,text=True)
    
    # Capture and display the output of the external script
        st.write("Output from the external script:")
        st.write(result.stdout)
 



    
# def ct_scan_segment():
#     if st.button("Go to Main Page"):
#         st.session_state.page = "Main Page"
    
#     st.title("CT Scan Segment")
#     st.write("This is the CT scan segment page.")
    
#     # CSS for styling
#     st.markdown("""
#         <style>
#         body {
#             font-family: Arial, sans-serif;
#             background: url('https://i.pinimg.com/736x/71/0e/f5/710ef5f9e67adb0033e3278fafdff440.jpg');
#             background-size: cover;
#             color: #343a40;
#         }

#         .container {
#             max-width: 1200px;
#             margin: 0 auto;
#             padding: 20px;
#         }

#         header {
#             background-color: #007bff;
#             padding: 20px 0;
#             text-align: center;
#         }

#         header h1 {
#             color: #fff;
#         }

#         section {
#             margin-top: 20px;
#         }

#         section h2 {
#             color: #007bff;
#         }

#         footer {
#             margin-top: 20px;
#             text-align: center;
#             color: #555;
#         }

#         .response-image img {
#             max-width: 100%;
#             height: auto;
#         }
#         </style>
#         """, unsafe_allow_html=True)

#     # Header
#     st.markdown('<header><h1>Upload CT Scan</h1></header>', unsafe_allow_html=True)

#     # File upload section
#     st.markdown('<section><h2>Select a PDF file (Max size: 200MB)</h2></section>', unsafe_allow_html=True)
#     uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"], accept_multiple_files=False)

#     # Process the file upload
#     if uploaded_file is not None:
#         file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
#         st.write(file_details)
        
#         # Save the uploaded file
#         os.makedirs("uploads", exist_ok=True)
#         with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
#             f.write(uploaded_file.getbuffer())
        
#         st.success("PDF file uploaded successfully!")

#         # Display a response image (replace with your own image processing logic)
#         # Assuming 'response.png' is the image you want to display
#         if os.path.exists("response.png"):
#             image = Image.open("response.png")
#             st.image(image, caption='Response Image', use_column_width=True)

#     # Footer
#     st.markdown('<footer><p>&copy; AM^2</p></footer>', unsafe_allow_html=True)





# def analyze_response():
#     if st.button("Go to Main Page"):
#         st.session_state.page = "Main Page"
    
    # st.title("Analyze Response")
    # st.write("This is the analyze response page.")
    
    # # CSS for styling
    # st.markdown("""
    #     <style>
    #     body {
    #         font-family: Arial, sans-serif;
    #         background: url('https://i.pinimg.com/736x/71/0e/f5/710ef5f9e67adb0033e3278fafdff440.jpg');
    #         background-size: cover;
    #         color: #343a40;
    #         margin: 0;
    #         padding: 0;
    #     }

    #     .container {
    #         max-width: 600px;
    #         margin: 50px auto;
    #         padding: 20px;
    #         background-color: #fff;
    #         border-radius: 10px;
    #         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    #     }

    #     header h1 {
    #         text-align: center;
    #         color: #007bff;
    #         margin-bottom: 20px;
    #     }

    #     section {
    #         margin-top: 20px;
    #     }

    #     section h2 {
    #         color: #007bff;
    #         margin-bottom: 10px;
    #     }

    #     input[type="file"] {
    #         display: block;
    #         width: 100%;
    #         padding: 10px;
    #         margin-bottom: 20px;
    #         border: 1px solid #ced4da;
    #         border-radius: 4px;
    #         box-sizing: border-box;
    #     }

    #     button {
    #         display: block;
    #         width: 100%;
    #         padding: 10px;
    #         background-color: #007bff;
    #         color: #fff;
    #         border: none;
    #         border-radius: 4px;
    #         cursor: pointer;
    #         transition: background-color 0.3s ease;
    #     }

    #     button:hover {
    #         background-color: #0056b3;
    #     }

    #     .response {
    #         margin-top: 20px;
    #     }

    #     .response h2 {
    #         color: #007bff;
    #         margin-bottom: 10px;
    #     }

    #     .response p {
    #         font-weight: bold
    #     }
    #     </style>
    #     """, unsafe_allow_html=True)

    # # Header
    # st.markdown('<header><h1>CT Scan Analyzer</h1></header>', unsafe_allow_html=True)

    # # File upload section
    # st.markdown('<section><h2>Select a PDF file to analyze</h2></section>', unsafe_allow_html=True)
    # uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    # # Process the file upload
    # if uploaded_file is not None:
    #     # Display file details
    #     file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
    #     st.write(file_details)

    #     # Simulate analysis (replace with your actual analysis logic)
    #     def analyze_pdf(file):
    #         # Read the PDF file
    #         reader = PyPDF2.PdfFileReader(file)
    #         text = ""
    #         for page in range(reader.numPages):
    #             text += reader.getPage(page).extract_text()
    #         return text

    #     # Perform analysis
    #     analysis_result_text = analyze_pdf(uploaded_file)

    #     # Display analysis result
    #     st.markdown('<section class="response"><h2>Analysis Result</h2></section>', unsafe_allow_html=True)
    #     st.text_area("Analysis Result", value=analysis_result_text, height=300)

    # # Footer
    # st.markdown('<footer><p>&copy; AM^2</p></footer>', unsafe_allow_html=True)






# Page mapping

# page_names_to_funcs = {
#     "Main Page": main_page,
#     "CT Scan Segment": ct_scan_segment,
#     "Analyze Response": analyze_response,
# }

# Initialize session state
# if "page" not in st.session_state:
#     st.session_state.page = "Main Page"





# # Render the selected page
# page_names_to_funcs[st.session_state.page]()

if __name__ == "__main__":
    main_page()