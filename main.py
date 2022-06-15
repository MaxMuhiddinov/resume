import streamlit as st
from fastai.vision.all import *
import pathlib
import plotly.express as px
import platform
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath
#title
st.title('Transportni klassifikatsiya qiluvchi model')

#rasimni joylash

file = st.file_uploader("Rasimni yuklash", type=['jfif','png', 'jpeg', 'gif', 'svg'])
if file:
    img = PILImage.create(file)
    st.image(file)
    model = load_learner('transport_model.pkl')



    pred, pred_id, probs = model.predict(img)

    st.success(f"Bashorat:{pred}")

    st.info(f"Extimolik: {probs[pred_id]*100:.1f}%")
    fig = px.bar(x=probs*100, y=model.dls.vocab)
    st.plotly_chart(fig)