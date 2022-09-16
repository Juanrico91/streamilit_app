import streamlit as st
from components import campaign_creation_form

campaign_creation_form.display_form()

create_campaign = st.button('Create Campaign')