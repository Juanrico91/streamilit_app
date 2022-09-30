from ast import While
import streamlit as st
import time
from datetime import date, timedelta
import requests
import json

st.title('Create a Campaing')

st.header('Set-Up Campaign Parameters')

form = st.form("Create Campaign")
col1, col2 = st.columns(2)

with col1:
    country_option = form.selectbox(
        'Country',
        ('Mexico', 'Colombia', 'Peru', 'Republica Dominicana'))


    brand_option = form.text_input('Brand','coronita')

    funel_objective_option = form.selectbox(
        'Funnel Objective',
        ('Awareness', 'Consideration', 'Conversion'))

    start_date = form.date_input(
        "Start Date",
        date.today())

    control_group_name1 = form.text_input('Control group name 1','CO_CatasBrillo_2021')
    control_group_name2 = form.text_input('Control group name 2','App Club America')
    control_group_name3 = form.text_input('Control group name 3','CO_QuinielaFutbol_2021')
    control_group_name4 = form.text_input('Control group name 4','CO_KitBrilloV2_2021')
    control_group_name5 = form.text_input('Control group name 5','CO_CamisetaMessi_2021')
    control_group_name6 = form.text_input('Control group name 6','CO_FutbolFemenil_2021')
    control_group_name7 = form.text_input('Control group name 7','Palco Corona')


    vehicle_option = form.selectbox(
        'Vehicle',
        ('Meta', 'Youtube', 'Twitter'))

with col2:

    end_date = form.date_input(
        "End Date",
        date.today() + timedelta(days=30))

    campaign_id = form.text_input('Campaign', 'campaign id')

    passion_points_list = ['Entertain','Art',
                            'Music', 'Gaming',
                            'Sports', 'Travel',
                            'Movies', 'Social',
                            'Environment', 'Food',
                            'Health', 'Traditions']

    entertain_slider = form.slider('Entertain', 0, 1 ,1)
    art_slider = form.slider('Art', 0, 1 ,1)
    music_slider = form.slider('Music', 0, 1 ,1)
    gaming_slider = form.slider('Gaming', 0, 1 ,1)
    sports_slider = form.slider('Sports', 0, 1 ,1)
    travel_slider = form.slider('Travel', 0, 1 ,1)
    movies_slider = form.slider('Movies', 0, 1 ,1)
    social_slider = form.slider('Social', 0, 1 ,1)
    environment_slider = form.slider('Environment', 0, 1 ,1)
    food_slider = form.slider('Food', 0, 1 ,1)
    health_slider = form.slider('Health', 0, 1 ,1)
    traditions_slider = form.slider('Traditions', 0, 1 ,1)

    campaign_objective = form.text_input('Campaign Objective', 'data_collection')

    campaign_spend = form.text_input('Campaign Spend', '200000')

    audience_size = form.slider('Audience Size', 1000, 100000, 1)

#form.write("Input passion points levels")

# with form:
#     load_passion_points_levels = form.form_submit_button('Load Passion Points Levels')
#     if load_passion_points_levels:
#         for passion_point in passion_points_options:
#             st.slider(passion_point, 0.0, 5.0, step=0.5, key=passion_point)
#     session_state = st.session_state
#    st.write(session_state)


def post_request():

    create_campaign_json = {
        "brand": str(brand_option),
        "start_date": str(start_date),
        "end_date": str(end_date),
        "campaign_spend": int(campaign_spend),
        "vehicle": str(vehicle_option),
        "audience_size": audience_size,
        "country": str(country_option),
        "objective": str(funel_objective_option),
        "passion_points": str({
                            'art' : art_slider,
                            'entertainment' : entertain_slider,
                            'environment' : environment_slider,
                            'food' : food_slider,
                            'gaming' : gaming_slider,
                            'healthwellness' : health_slider,
                            'movies' : movies_slider,
                            'music' : music_slider,
                            'social' : social_slider,
                            'sports' : sports_slider,
                            'traditions' : traditions_slider,
                            'travel' : travel_slider}),
        "name": str(campaign_id),
        "cam_control_groups": str([
            control_group_name1,
            control_group_name2,
            control_group_name3,
            control_group_name4,
            control_group_name5,
            control_group_name6,
            control_group_name7
        ]),
        "campaign_objective": str([campaign_objective]),
        "passion_points_levels":"string"
        }

    #headers = {'Content-type': 'application/json'}

    json_object = json.dumps(create_campaign_json, indent = 4)

    print(json_object)

    campaing_create_request = requests.post(
        'http://34.172.142.210/campaigns',
        #headers=headers,
        data = json_object)
# provisional
    stopper = True
    return stopper

if form.form_submit_button("Create Campaign", on_click=post_request()):
    st.balloons()
    st.write("Creating campaingn")
    my_bar = st.progress(0)
    # while stopper == False:
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1)