import streamlit as st
import pandas as pd
from io import StringIO
import os
# uploaded_file = st.file_uploader("Choose a file",accept_multiple_files=False)
# if uploaded_file is not None:
#     # Create a temporary path to store the uploaded file
#     temp_dir = "./uploaded_video"
#     os.makedirs(temp_dir, exist_ok=True)

#     # Save the file locally
#     file_path = os.path.join(temp_dir, uploaded_file.name)
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

#     # Display the path
#     st.write(f"File saved at: {file_path}")
#     print(file_path)
# # print(uploaded_file)
# # # video_file = open("test.mp4", "rb")
# # # video_bytes = video_file.read()

# # st.video(uploaded_file)
temp="./uploaded_video/test video.mp4"
temp="video/"+temp.split('/')[-1];
print(temp)