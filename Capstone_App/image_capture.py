
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import cv2
import numpy as np
from PIL import Image
import os

class VideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.frame = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.frame = img
        return av.VideoFrame.from_ndarray(img, format="bgr24")

def app():
    st.title("Capture an Image of Your Food")
    st.write("Click the button below to open your camera")

    webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor)

    if webrtc_ctx.video_processor:
        if st.button("Capture"):
            img = webrtc_ctx.video_processor.frame
            if img is not None:
                
                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
               
                img_pil = Image.fromarray(img_rgb)
                # Display the  image
                st.image(img_pil, caption="Captured Image")

                # Create the new_images folder if it doesn't exist
                if not os.path.exists('new_images'):
                    os.makedirs('new_images')

                # Save the image in the new_images folder
                img_pil.save(os.path.join('new_images', 'captured_image.png'))
                st.success("Image saved successfully!")
            else:
                st.warning("No frame available to capture")

# Run the app
if __name__ == '__main__':
    app()
