import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import av
from datetime import datetime, timezone, timedelta
import threading
import time

# st.set_page_config(
#     page_title="Cam App",  
#     layout="wide")

st.title('RemoteCam App')
datetime_loc = st.empty()

# col1, col2 = st.columns(2)

def date_display():
    while ctx.state.playing:
        now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y年%m月%d日 %H:%M:%S")
        datetime_loc.text(now)

def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    cv2.putText(img,
            text="test",
            org=(0, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4)
    return av.VideoFrame.from_ndarray(img, format="bgr24")



ctx = webrtc_streamer(
      key='example1', 
      video_frame_callback=callback,
    #   source_video_track=1,
    #   source_audio_track=1
      )

thread1 = threading.Thread(target=date_display)
thread1.start()

# with col1:
#     ctx = webrtc_streamer(
#          key='example1',
#          video_frame_callback=callback
#          )
#     st.text("bbbbb")

# with col2:
#     webrtc_streamer(
#          key='example2',
#          )


# while ctx.state.playing:
#     now = datetime.now(timezone(timedelta(hours=9))).strftime("%Y年%m月%d日 %H:%M:%S")
    # datetime_loc.text(now)
