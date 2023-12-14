import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config("main", "🏠")

st.sidebar.image(
    "/home/hrc/data/medical-platform/public/name_njmu_black.png",
    use_column_width="auto",
)

with st.sidebar:
    selected = option_menu(
        "",
        ["Home", "Settings"],
        icons=["house", "gear"],
        default_index=0,
    )
