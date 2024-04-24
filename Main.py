import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

def main():
    st.set_page_config(
        page_title="Pdf Sage",
        page_icon="📜")
    st.header("Pdf Sage")
    
    final = "https://lottie.host/a14539fe-6eb2-4fb8-83ec-0b1608a8a2a9/S0jM3luF7X.json"

    st_lottie(
    final,
    height=400,
    width=400,
    )
    
    st.subheader("Engage with PDFs in real-time conversations. Seamlessly discuss document content as it unfolds.")
    
if __name__ == "__main__":
    main()