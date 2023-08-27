import streamlit as st
import openai
import os
from PIL import Image
import streamlit.components.v1 as components
from pdf2docx import Converter
from response_creator import final_model_response
from document_formatter import heading_from_pdf
from document_formatter import text_from_pdf
from document_formatter import heading_from_docx
from document_formatter import text_from_docx
from pdf_creator import response_file_pdf
import time

#The logo of the competition 'TechSurf 2023'
# and the company 'ContentStack'
image1 = Image.open('symbo.PNG')
image2 = Image.open("new_symbo.PNG")

#initializing variables
heading = "-1"
text = "-1"
response = "-1"
DALLE_image_title="-1"
DALLE_image = Image.open('symbo.png')
lst_sources = ["0","0"]
bool_output=0
submit=False

#Defining the OpenAI secret keys, this is stored in the streamlit secrets and obtained from over ther
openai_key = st.secrets["openai_key"]
serper_api_key=st.secrets["serper_api_key"]
os.environ['OPENAI_API_KEY']=openai_key
openai.api_key = openai_key
os.environ["SERPER_API_KEY"] = serper_api_key

if "preview" not in st.session_state:
    st.session_state["preview"]=True
if "pdf" not in st.session_state:
    st.session_state["pdf"]=True
if "docx" not in st.session_state:
    st.session_state["docx"]=True

st.session_state["preview"]=True
st.session_state["pdf"]=True
st.session_state["docx"]=True
st.session_state["model"]="gpt-3.5-turbo"

#Displaying the two logos as columns side by side
col1, col2 = st.columns(2)

with col1:
   st.image(image1)

with col2:
   st.image(image2)

#Setting up the layout of the page
st.title('**:red[NextGenAI]** Content Generator')

with st.sidebar:
    st.markdown('# **NextGenAI Content Generator**')
    st.markdown("Submission for the Prototype round of **:violet[<TechSurf/> 2023]** by **ContentStack**.")
    st.markdown("Submission by [Ankur Kumar Raj](www.github.com/ankurkraj)")
    st.markdown("---")

#Extra customization features that can be added as wished
with st.sidebar.expander(" 🛠️ Additional Low Level Customizations 🛠️", expanded=False):
    # Option to preview memory store
    st.markdown('If you wish to provide your own API key, you can get one at [OpenAI](https://platform.openai.com/account/api-keys)')
    openaikey = st.text_input("㊙️ OpenAI API Secret Key", type="password")
    if openaikey:
        openai_key = openaikey
    st.markdown("---")
    st.markdown('By default All the output formats will be displayed. You can check any of the boxes to not display a particular output format.')

    if st.checkbox("Do not preview the model OutPut"):
        st.session_state["preview"]=False
    if st.checkbox("Do not output PDF form of the OutPut"):
        st.session_state["pdf"]=False
    if st.checkbox("Do not preview DOCX(Microsoft Word) form of the OutPut"):
        st.session_state["docx"]=False

    st.markdown("---")
    # Option to preview memory buffer
    st.session_state['model'] = st.selectbox(
        label="Model",
        options=[
            "gpt-3.5-turbo",
            "text-davinci-003",
            "gpt-4",
        ],
    )

st.markdown("---")

st.markdown(':writing_hand What kind of input will you be providing ?')
input_type = st.selectbox(
        "✍️ What kind of input will you be providing ?",
        ('Input in the Box', 'Upload a File'))
if input_type == "Input in the Box":
    text = st.text_input("Input Content", type="default",
                              placeholder="Input the Type of content that you want the model to generate the content based on.",
                              help="You can choose this option if you want to directly input the content.")
    if text:
        st.success('Input Received ', icon="✅")
else:
    uploaded_file = st.file_uploader(
        "📁 Upload a pdf, docx, or txt file",
        type=["pdf", "docx", "txt"],
        help="The pdfs that contain texts as images are not supported",
    )
    if uploaded_file:
        st.success('File Uploaded ', icon="✅")
        if str(uploaded_file.name)[len(str(uploaded_file.name))-4:]==".pdf":
            print("PDF file recognised")
            heading = heading_from_pdf(uploaded_file)
            text = text_from_pdf(uploaded_file)
        if str(uploaded_file.name)[len(str(uploaded_file.name))-5:]==".docx":
            print("DOCX file recognised")
            heading = heading_from_docx(uploaded_file)
            text = text_from_docx(uploaded_file)

bool_head = st.radio(
    "Do you want to provide a heading ?",
    ('Yes', 'No'), help="Click here if you want to provide a heading, leave it blank if you want the model to generate a heading on its own or recognize the heading itself from the given input")

if bool_head == "Yes":
    heading = st.text_input("Heading", type="default", placeholder="Input the Heading")
    if heading:
        st.success('Heading Received ', icon="✅")
Creativity = st.slider(
    "Creativity Bar",0.0, 1.0, 0.01, help="Determines the creativity level of the content generated, by default it is set to 0. The most technically accurate results are produced by the model at Value = 0. While out of the box outputs are generated by greater values. 1 being at the max.")

if bool_output==0:
    submit = st.button("Submit the inputs and Generate additional Content ")

if submit==True:
    with st.spinner('Displaying your amazing content...'):
        msg = st.toast(
            'It usually take about 2 minutes to generate the content...,',
            icon="⏲️")
        time.sleep(4)
        msg.toast('if it takes more than 3 min, kindly refresh and try again')
        time.sleep(4)
        response = "-1"
        response,dalle_prompt,heading = final_model_response(text, openai_key, serper_api_key, heading, Creativity)
        heading.replace('"','')
        heading.replace('.','')
        pdf_file = response_file_pdf(heading, dalle_prompt, response)
        doc_file = Converter('varying_new_format.pdf')
        doc_file.convert(heading+'.docx')
    bool_output = 1
    st.snow()
    if bool_output==1:
        col3, col4 = st.columns(2)
        with col3:
            st.download_button(
                label="Download data as PDF",
                data=pdf_file,
                file_name='essay' + '.pdf',
                key="PDF Key",
                mime='text/pdf',
            )

        with col4:
            st.download_button(
                label="Download data as DOCX",
                data='heading.docx',
                file_name='essay' + '.docx',
                key="DOCX Key",
                mime='text/docx',
            )
