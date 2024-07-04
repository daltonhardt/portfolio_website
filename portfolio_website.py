import streamlit as st
import google.generativeai as genai

# genai.configure(api_key=os.environ["API_KEY"])
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

persona = """
        You are Dalton AI bot.You help people anwer questions about Industry 4.0.
        If you are responding don't answer in second or third person. If you don't know the answer you simply say
        'That's a secret'. Here is more info about 4F and PSL companies.
        Dalton's Github: https://github.com/daltonhardt
        Dalton's Website: https://4f-psl-eng.webflow.io/
        """

base_directory = "/Users/dalton/Desktop/workspace/code/PycharmProjects/AiZero2Hero/"
col1, col2 = st.columns(2)
st.title('Hello :wave:  I am Dalton Hardt')
st.sidebar.title('This is my portfolio')
st.sidebar.image('./images/Foto-Dalton.jpg')
st.sidebar.markdown('I help companies implementing Internet of Things (IoT) and Computer Vision solutions.')

st.header("Dalton's AI Bot")
st.write("Ask anything about us:")
user_question = st.text_input(label=' ', placeholder='write it here...')
if st.button("Ask", use_container_width=200):
    prompt = persona + "Here is the question that the user asked" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)


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
st.slider("Engineering Process", 0, 100, 80)

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
