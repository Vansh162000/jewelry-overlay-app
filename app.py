import streamlit as st
from PIL import Image

def overlay_jewelry(user_image, jewelry_image, position):
    user_img = Image.open(user_image)
    jewelry_img = Image.open(jewelry_image)

    if position == 'necklace':
        position = (int(user_img.width / 4), int(user_img.height / 2))
    elif position == 'mattapatti':
        position = (int(user_img.width / 3), int(user_img.height / 10))
    elif position == 'hairclip':
        position = (int(user_img.width / 2), int(user_img.height / 5))
    elif position == 'earrings':
        position = (int(user_img.width / 4), int(user_img.height / 3))
    else:
        position = (0, 0)

    user_img.paste(jewelry_img, position, jewelry_img)
    return user_img

st.title("Jewelry Overlay Application")

user_image = st.file_uploader("Upload your image", type=['jpg', 'png', 'jpeg'])
if user_image:
    st.image(user_image, caption='Your Image', use_column_width=True)

    jewelry_image = st.file_uploader("Upload your jewelry image", type=['jpg', 'png', 'jpeg'])
    if jewelry_image:
        st.image(jewelry_image, caption='Jewelry Image', use_column_width=True)

        position = st.selectbox("Select position for the jewelry", 
                                 ['necklace', 'mattapatti', 'hairclip', 'earrings'])

        if st.button("Overlay Jewelry"):
            result_image = overlay_jewelry(user_image, jewelry_image, position)
            st.image(result_image, caption='Image with Jewelry Overlay', use_column_width=True)
