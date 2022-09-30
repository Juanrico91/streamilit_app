
from re import S
import streamlit as st
import datetime
import requests

st.title('Create a Campaing')


def display_form():
    st.header('Set-Up Campaign Parameters')
    col1, col2 = st.columns(2)

    with st.form("Create Campaign"):

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

            control_group_name1 = st.text_input('Control group name 1','beerLover')

            vehicle_option = st.selectbox(
                'Vehicle',
                ('Meta', 'Youtube', 'Twitter'))

        with col2:

            ed = st.date_input(
                "End Date",
                datetime.date(2019, 7, 6))

            campaign_id = st.text_input('Campaign', 'campaign id')

            passion_points_options = st.multiselect(
                'Passion Points',
                ['Entertain','Art',
                'Music', 'Gaming',
                'Sports', 'Travel',
                'Movies', 'Social',
                'Environment', 'Food',
                'Health', 'Traditions'])

            campaign_spend = st.text_input('Campaign Spend', '350000')

            control_group_name2 = st.text_input('Control group name 2','PokerAmigos')

            audience_size = st.slider('Campaign Spend', 1000, 100000, 1)

        passion_potints_levels = st.button('Input passion points levels')
        if passion_potints_levels:
            for passion_point in passion_points_options:
                st.slider(passion_point, 0, 5, 0.5)

        submitted = st.form_submit_button("Create Campaign")
        if submitted:
            create_campaign_json = {
                "brand": brand_option,
                "name": campaign_id,
                "cam_control_groups": [control_group_name1, control_group_name2],
                "start_date": sd,
                "end_date": ed,
                "campaign_spend": campaign_spend,
                "vehicle": vehicle_option,
                "audience_size": audience_size,
                "country": country_option,
                "objective": objective_option,
                "passion_points": passion_points_options
                }

            headers = {'accept': 'application/json'}

            create_campaign_post = requests.post(
                'http://35.192.1.213/campaigns',
                headers=headers,
                json = create_campaign_json)
            st.balloons()
