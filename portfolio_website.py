import streamlit as st
import google.generativeai as genai

# genai.configure(api_key=os.environ["API_KEY"])
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """
        You have to pretend you are Dalton Hardt. You are 59 years old and have more than 25 years of experience in the industry.
        You help people answer questions about Industry 4.0 and develop projects related to this. Your knowledge includes ESP32 micro-processors,
        Arduino, sensors, 3d printing, cabling, wi-fi connection, and programing languages like C/C++, HTML, CSS, JavaScript and Python.
        You also have some knowledge with computer vision and specific libraries like Pandas and OpenCV.
        In summary you are a hands-on Product and Process Engineer and IT manager for R&D, Process and Technology. The consistent background in
        computer aided technologies, management and Industry 4.0 contribute to become an expert at aligning technology with business goals and
        Digital Transformation process and provide high return. Passionate about programming languages, Computer Vision, Machine Learning, AI
        and LLM.
        If the question is in portuguese (from Brazil) then you have to answer in portuguese always. If the question is in Spanish, of course
        you have to answer in Spanish, and so on. That means, you always answer in the same language as the question was made.
        If you are responding don't answer in second or third person. If you don't know the answer you simply say
        'That's a secret'. Here is more info about Dalton and his company 4F/PSL. Dalton has a partner, Mr. Paulo Lopes who also has
        a large experience in the Industry. Some of the customers can be found in the website but I can also list here:
        Embraco, Electrolux, Porto de Itapoá, WEG, Malwee and some others.
        Dalton's LinkedIn: www.linkedin.com/in/dalton-hardt
        Dalton's Github: https://github.com/daltonhardt
        Dalton's Website: https://4f-psl-eng.webflow.io/
        """

base_directory = "/Users/dalton/Desktop/workspace/code/PycharmProjects/AiZero2Hero/"
col1, col2 = st.columns(2)
st.title('Hello :wave:  I am Dalton Hardt')
st.sidebar.title('This is my portfolio')
st.sidebar.image('./images/Foto-Dalton.jpg')
st.sidebar.markdown('We help companies implementing Internet of Things (IoT) and Computer Vision solutions.')

#st.header("Dalton's AI Bot")
st.subheader("Ask anything about us:")
user_question = st.text_input(label=' ', placeholder='write it here...')
if st.button("Ask", use_container_width=200):
    prompt = persona + "Here is the question that the user asked" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col3, col4, col5 = st.columns(3)
with col3:
    st.subheader("Top skills:")
    st.markdown(
        """
        - 25+ years of industry experience
        - Industry 4.0
        - IoT, ESP32, 3D-printing
        - C++/JavaScript/Python
        """
    )
with col4:
    st.image("./images/TTUnit.jpg")
with col5:
    st.image("./images/RCP.jpg")

st.title("Our setup")
st.image("./images/setup.jpg")

st.title(" ")
st.title("Our Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Process Engineering", 0, 100, 80)

st.title("Gallery")
col1, col2 = st.columns(2)
with col1:
    for i in range(3):
        st.image(f"./images/g{i + 1}.jpg")
with col2:
    for i in range(3):
        st.image(f"./images/g{i + 4}.jpg")

st.title(" ")
st.title("Contact")
st.subheader("We have offices in Brazil and Spain.")
st.subheader("For inquiries, send an email to: dalton.hardt@gmail.com")
