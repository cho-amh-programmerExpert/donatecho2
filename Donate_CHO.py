import streamlit as st
from streamlit_extras.colored_header import colored_header
from st_paywall import add_auth

st.set_page_config(page_icon="🪙", page_title="Donate C.H.O | Payment Plan")
hidden_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hidden_streamlit_style, unsafe_allow_html=True)

# ====== Authentication & Subscription ====== #

colored_header(label="💸 Donation Status Page", description="The state of donating to C.H.O", color_name="red-70")
add_auth(required=True)

# ====== Main App: After Subscription ====== #

st.write("**Thank you so much for subscribing! Your help is very much appreciated.**")
_, _, _, l, m, r, _, _, _ = st.columns(9)
l.divider()
m.write(f"**:blue[Status]: :green[Active]**")
r.divider()
st.write(f"**:orange[Subscribed Via]: \":green[{st.session_state.email}]\"**")
