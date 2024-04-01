import streamlit as st


st.set_page_config(
    page_title="Lakshita Singh - Engineer, Roboticist, Maker",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.5, 0.5], gap="large")
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 100%;
    }
    </style>

    <div class="profile-img">

    ![]('PXL_20240102_000607702-EDIT.jpg')
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.image('PXL_20240102_000607702-EDIT.jpg')
with col2:
    st.markdown(
        """
    #    
    # Lakshita Singh 

    - MS (Robotics) Student, University of Washington
    - B.Tech in Mathematics and Computing, Delhi Technological University 
    - Software Developer 
    - Roboticist
    
    """
    )


st.markdown(
    """
# Projects

"""
)
col3, col4 = st.columns([0.5, 0.5], gap="large")


# with col3:
#     st.markdown(
#         '''
#         [Smart Wearable](https://github.com/laks1806/Smart-Wearable)

#     '''
#     )
#     st.video("https://github.com/laks1806/Smart-Wearable")

with col3:
    st.markdown(
        '''

        [Smart Wearable](https://github.com/laks1806/Smart-Wearable) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/laks1806/Smart-Wearable)

        '''
    )
    # st.video("https://github.com/laks1806/Smart-Wearable")
    st.write(""" This device is designed to monitor your sitting time and provide reminders to stay active. It incorporates BME280 and MPU6050 sensors to measure environmental parameters and user motion in real-time. If you sit for more than 2 hours continuously, the device will vibrate to remind you to stand up and move around. Additionally, it provides alerts to drink water at regular intervals. The device features LED indicators and an OLED display for visualizing information. """)

    

with col4:
    st.markdown(
        '''
        [Rakshak web app](https://github.com/laks1806/Rakshak_) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/laks1806/Rakshak_)


    '''
    )
    st.write(""" A solution to combat sexual assault. Users log in and provide contact details for up to five trusted guardians. They can activate a live location feature to share their whereabouts or discreetly trigger an emergency alert with a double-press for immediate assistance. Guardians can navigate to the user's location swiftly, enhancing user safety. Additionally, users can input their route for safety checks, and the device's location can be tracked in real-time.""")

      


st.markdown(
    """
# Hobbies

- Swimming
- Reading
- Singing
- Playing Guita, Ukulele, Harmonica 

""")
st.markdown(
    """
# About


A motivated engineer, who believes that engineering isn't about perfect solutions; it's about doing the best you can with limited resources. Curious about how these technologies work and how I can contribute to work towards their advancement.

""")


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/laks1806" target="_blank"> by laks</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)