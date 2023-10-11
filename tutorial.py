import streamlit as ST
ST.set_page_config(page_title='My Streamlit',page_icon='random')
mymenu=ST.sidebar.selectbox('my Menu',('Home','FillForm','Downloads'))
ST.image('https://theenvoyweb.com/wp-content/uploads/2021/02/Wakanda.jpg')
ST.title('Wakanda Forever')
ST.header('By Abhishek Yadav')
ST.text('This is created by Streamlit Library')
if (mymenu=='Home'):
    ST.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
    ST.video('https://www.youtube.com/watch?v=aFgtBbSwxxw&pp=ygUOd2FrYW5kYSB2aWRlb3M%3D')
elif(mymenu=='FillForm'):
    with ST.form('my Form'):
        name=ST.text_input('Enter name')
        DOB=ST.date_input("Choose Date of Birth")
        marks=ST.slider('Choose Marks')
        k=ST.form_submit_button("Submit Form")
        if k:
            ST.write('Name:',name,'dob:',DOB,'Marks:',marks)
elif(mymenu=='Downloads'):
    ST.header("Downloads")
    ST.download_button('Download Now','hello is the downloaded data','wakanda.txt')
            
