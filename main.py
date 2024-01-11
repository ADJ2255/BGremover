import streamlit as st
from rembg import remove
from PIL import Image


def removebg(img):
    input = Image.open(img)
    return remove(input)

def main():
    st.title(" IMAGE BG REMOVER")
    uploaded_file = st.file_uploader("SELECT THE IMAGE..",type=["jpeg","jpg","png"])

    if uploaded_file is not None:
        st.image(uploaded_file,caption="uploaded image")
        st.write("Processing...")
        result=removebg(uploaded_file)
        st.image(result,caption= "result")
        

if __name__ == '__main__':
    main()    