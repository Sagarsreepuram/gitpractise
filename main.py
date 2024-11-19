#importing the library od streamline
import streamlit as sl
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np

tabel = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7], "Column 2":[11,12,13,14,15,16,17]})

# To hide the Hamburger(3 dots button in the last)
# sl.markdown('''
# <style>
# .st-emotion-cache-w3nhqi.ef3psqc5
# {
#  visibility: hidden;           
# }
# </style>    
# ''',unsafe_allow_html=True)



sl.title("Hi! This is Streamlit WebPage")
sl.subheader("Hi! I am your Sub Header")
sl.header("Hi! I am a Header")
sl.text("Hi! Hi Welcome to the text like para")

# Markdown Function to bring up the html

# where this **text** will allow in the bold  
sl.markdown("**Hello** Motto")
# for Italic use single *
sl.markdown("**Hello** *Motto*")
# for h1 use # space text
sl.markdown("# Hello Motto")
# for h2 use ## space text
sl.markdown("## Hello Motto")
# for h3 use ### space text
sl.markdown("### Hello Motto")
# for h1 use > space Blockquote
sl.markdown("> Hello Motto")
# for h1 use 1. space text
sl.markdown("1. Hello Motto")
# for h1 use - space text
sl.markdown("- Hello Motto")
# for h1 use --- for line
sl.markdown("---")
# for h1 use [tittle](websitelink)
sl.markdown("[Google](https://www.google.com/)")

sl.markdown("---")
sl.caption("Hi Welcome to the caption")
# To use the maths function we latix
sl.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
#use json format
json={"a":"3,2,6,5","b":"6,5,9,4,","c":"df,dff,2"}
sl.json(json)

code="""
print("Hello"+add(,))
def add(a,b):
    return a+b
"""
sl.code(code,language="Python")

#Swiss Army function is sl.write
sl.write("Hello, Streamlit!")
sl.write("# Big Heading\n\nHere's some **bold text**!")

#How to use metric Function
#to get this matic function  u need to type delta="1.4ms⁻¹" to get as shown type this after 1 click tab\^-1
sl.metric(label="Wind speed", value="120ms⁻¹", delta="1.4ms⁻¹")
#if u want change the arrow of the delta to downwards use - 
sl.metric(label="Wind speed", value="120ms⁻¹", delta="-1.4ms⁻¹")

#To create table use panda lib import that and create this 
#tabel = pd.DataFrame({"Column 1":[1,2,3,4,5,6,7], "Column 2":[11,12,13,14,15,16,17]})
sl.table(tabel)
#It will look in organized way we can sort it also 
sl.dataframe(tabel)

#Adding an img to streamlit
sl.image("neualto_technologies_pvt_ltd_logo.jpg", caption="Our Company Name")

#We can add the audio(" audiofilename ")
# sl.audio("Audiofile.mp3")

#aWe can add the audio(" Videofilename ")
# sl.video("videofile.mp3")

# to stop the server  ctrl + c

#Checkbox to check it
sl.checkbox("Checkbox")
#Checkbox to check it to get checkit use true
sl.checkbox("Checkbox", value="true")
#To statisfy the condition
state = sl.checkbox("check", value=True)
if state:
    sl.write("Hi welcome")
else:
    pass

#If you want to notifed of the change if uncheck the box what ever u wanted notify will display in console
# def change():
#     print("changed")
# state = sl.checkbox("checbox", value=True, on_change=change)

#If you want to change the session output as true or false by using session state
def change():
    print(sl.session_state.checker)
state = sl.checkbox("checbox", value=True, on_change=change, key="checker")

#Radio button options to select the text
Button = sl.radio("In Which Country You Live?", options=("India","USA" ,"Canada","Germany"))
print(Button)

#On click function to intreact with button
def fun_btn():
    print("Button got clicked")
Btn = sl.button("Click Here", on_click=fun_btn)

#If we want to select box use this function
select = sl.selectbox("What is favorite car",options=("BMW", "Benz", "Audi")) 

#If you want multi select
Select_mutli = sl.multiselect("Select you your Items to cart",options=("Tomoto", "Carrot", "Beans","Borocoli", "Beetrrot"))

#How to upload the files
sl.title("Uplaod the Files")
sl.markdown("---")
Img = sl.file_uploader("Please Upload your Img", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
if Img is not None:
   sl.image(Img)

#Slider to select the size
Entry_Age = sl.slider("Select the percentage", min_value=18, max_value=70, value=22)
print(Entry_Age)
#To cutomize the options we have select slider
Entry_Pub = sl.select_slider("Select The Age",options=["Gillys Resto bar","IronHill","Skytop bar"])

#To get data from the user. it will print in console
#Max char function is to limit the character 
input=sl.text_input("Enter your course name" ,max_chars=20)
print(input)
#if you want more text area
text_area= sl.text_area("Describe about your course")
#Time and date input from user
# time=sl.time_input("Enter the your avaliable time")
# date=sl.date_input("Enter your available date ")

#progress bar to see the progress
# bar=sl.progress(0)
# for i in range(10):
#     bar.progress((i+1)*10)
#     ts.sleep(1)

#Set the progress bar with the timer
def converter(value):
    m,s,mm=value.split(":")
    ts = int(m)*60+int(s)+int(mm)/1000
    return ts
val= sl.time_input("Set Timer",value=time(0,0,0))
if str(val) == "00:00:00":
    sl.write("Please sent timer")
else:
    sec=converter(str(val))
    print(sec)
    bar=sl.progress(0)
    per=sec/100
    prog = sl.empty()
    for i in range(100):
        bar.progress(i+1)
        prog.write(str(i+1) + "%")
        ts.sleep(per)    
sl.markdown("---")
#Headings and using the markdown for html h1
sl.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)

#One way to create forms
form = sl.form("Form 1")
form.text_input("First Name")
form.form_submit_button("Submit")

#Another way to create form
with sl.form("Form 2"):
    sl.text_input("What is your FirstName")
    sl.text_input("What is your LastName")
    sl.form_submit_button("Submit")

#To create column in the forms and to align center use html property
sl.markdown("<h1 style='text-align:center;'>User Registration</h1>", unsafe_allow_html=True)
with sl.form("From 3", clear_on_submit=True):
    col1,col2 = sl.columns(2)
    f_name=col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    sl.text_input("Email Addreess")
    sl.text_input("Enter the Password")
    sl.text_input("Confirm the Password")
    day,month,year = sl.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")     
    s_submit=sl.form_submit_button("Submit")
    if s_submit:
        if f_name == "" and l_name == "":
            sl.warning("Complete the above Fields")
        else:
            sl.success("Submitted Successfull")

#Side menu to display
# sl.sidebar.write("Hello this is my side bar")
# #To create a graph of sin(0) 
# x=np.linspace(0,10,100)
# fig=plt.figure()
# plt.plot(x, np.sin(x))
# sl.write(fig)

#Now we will create different types of graph like bar line etc and sin(0) and cos(0) and 
# we can use github link for style the graph 
x=np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5,6])
opt = sl.sidebar.radio("Select Any Graph", options=("line","bar","H-line"))
if opt == "line":
    sl.markdown("<h1 style = 'text-align:center;'>Line Graph</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x),'--')
    sl.write(fig)
elif opt == "bar":
    sl.markdown("<h1 style='text-align:center;'>Bar Graph</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")    
    plt.bar(bar_x, bar_x*10)
    sl.write(fig)
else: 
    sl.markdown("<h1 style='text-align:center;'>H-line</h1>",unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")

    plt.barh(bar_x*10,bar_x)
    sl.write(fig)