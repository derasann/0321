import streamlit as st
from PIL import Image

st.title('新しい送信機')

st.write('Display Image')
img = Image.open('boxer.jpg')
st.image(img, caption='ELRSに移行！', use_column_width=False, width=300)

option = st.slider(
    'どの位良いと思いますか、',
    min_value=1, max_value=10, value=5
)
'あなたの評価は、', option, 'です。'