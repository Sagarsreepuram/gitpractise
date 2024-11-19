import streamlit as sl
from PIL import Image
from PIL.ImageFilter import *

sl.markdown("<h1 style='text-align:center;'>Image Editor</h1>",unsafe_allow_html=True)
sl.markdown("---")
image = sl.file_uploader("Uplaod the Iamge", type=[".jpg",".jpeg",'png']) 
#When the user uplaoded the img it will be printed in the terminal
# if image:
#     img = Image.open(image)
#     print(img)
#     print(img.mode)
#     print(img.format)
#     print(img.size)

# to dispaly in the browser itself
info = sl.empty()
size = sl.empty()
mode = sl.empty()
format= sl.empty()
if image:
    img=Image.open(image)
    info.markdown("<h2 style ='text-algin:center;'>Information</h2>",unsafe_allow_html=True)
    size.markdown(f"<h6>size: {img.size} </h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>mode: {img.mode} </h6>", unsafe_allow_html=True)
    format.markdown(f"<h6>format: {img.format} </h6>", unsafe_allow_html=True)   
    sl.markdown("<h2 style ='text-algin:center;'>Resizing</h2>",unsafe_allow_html=True)
    width = sl.number_input("width",value=img.width)
    height = sl.number_input("Height",value=img.height)
    sl.markdown("<h2 style='text-algin:center'> Rotation </h2>",unsafe_allow_html=True)   
    degree = sl.number_input("Degree")  
    sl.markdown("<h2 style='text-algin:center'> Rotation </h2>",unsafe_allow_html=True)
    filter = sl.selectbox("Filters",options=("None","Blur","Detail","Emboss","Smooth")) 
    s_btn = sl.button("Submit")
    if s_btn:
        edited=img.resize((width, height)).rotate(degree) 
        filtered=edited
        if filter !="None":
            if filter == "Blur":
               filtered = edited.filter(BLUR)
            elif filter == "Detail":
                filtered = edited.filter(DETAIL)
            elif Filter == "Emboss":
                filtered = edited.filter(EMBOSS)
            else:
                 edited.filter(SMOOTH)  
        sl.image(filtered)                  