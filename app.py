import streamlit as st
import logging

# Configure the root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # Set the minimum level to capture

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root_logger.addHandler(handler)

logger = logging.getLogger(__name__)

logger.debug("This is a debug message (root logger configured)")
st.write("Hello Streamlit!")