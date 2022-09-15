
import streamlit as st
import datetime

st.title('Create a Campaing')

def display_form():
    st.header('Set-Up Campaign Parameters')
    col1, col2 = st.columns(2)

    with st.container():

        with col1:
            country_option = st.selectbox(
                'Country',
                ('Mexico', 'Colombia', 'Peru', 'Republica Dominicana'))


            brand_option = st.selectbox(
                'Brand',
                ('Corona', 'Club Colombia', 'Modelo', 'Poker'))

            objective_option = st.selectbox(
                'Campaign Objective',
                ('Awareness', 'Consideration', 'Conversion'))

            sd = st.date_input(
                "Start Date",
                datetime.date(2019, 7, 6))

        with col2:

            ed = st.date_input(
                "End Date",
                datetime.date(2019, 7, 6))

            campaign_id = st.text_input('Campaign', 'campaign id')

            passion_points_options = st.multiselect(
                'Passion Points',
                ['Music', 'Gaming', 'Sports', 'Travel'],
                ['Music', 'Gaming'])

            campaign_id = st.text_input('Campaign Spend', '$ 200000')