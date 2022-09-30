import streamlit as st
import plotly.graph_objects as go
import requests
import pandas as pd
import random
import ast
#containers
st.markdown("<h1 style='text-align: center;'>Campaign Summary Stats", unsafe_allow_html=True)

selected_campaign =st.number_input("Insert de Id of the campaign", 0, 200, 7, 1)
selected_campaign_button = st.button("Get Data")

dns = 'http://127.0.0.1:8000'

if selected_campaign_button:

    headers = {
        'accept': 'application/json',
    }

    datacard_response = requests.get(f'{dns}/datacard/{selected_campaign}', headers=headers)
    datacard_data = datacard_response.json()

    #st.write(datacard_data)

    card_container = st.container()

    with card_container:
        col1, col2, col3= st.columns(3)
        col1.metric("AUDIENCE SIZE", str(datacard_data["audience_size"]))
        col1.metric("CAMPAIGN SPEND", f'$ {str(datacard_data["campaign_spend"])}')
        col2.metric("CAMPAIGN START", datacard_data["start_date"])
        col2.metric("CAMPAIGN END", datacard_data["end_date"])
        col3.metric("OBJECTIVE", datacard_data["objective"])
        col3.metric("VEHICLE", str(datacard_data["vehicle"]))

    row1 = st.container()

    with row1:
    #spend by group
        col1_row1, col2_row1 = st.columns(2)
        headers = {
            'accept': 'application/json',
        }

        spend_by_group_response = requests.get(f'{dns}/campaign_spends/{selected_campaign}',
        headers=headers)
        spend_by_group_data = spend_by_group_response.json()

        groups =['Control Group','Test Group']
        fig = go.Figure([go.Bar(x=groups, y = [spend_by_group_data["control_group_spend"],
                                                spend_by_group_data["test_group_spend"]])])
        fig.update_layout(
        title={'text':"Spend by Group",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        xaxis_title="Groups",
        yaxis_title="Spend [$ MM]",
        font=dict(
            family="sans serif",
        )
        )
        col1_row1.plotly_chart(fig, use_container_width = True)
    #spend by model
        headers = {
            'accept': 'application/json',
        }

        spend_by_model_response = requests.get(f'{dns}/campaigns/{selected_campaign}', headers=headers)
        spend_by_model_data = spend_by_model_response.json()
#        st.write(spend_by_model_data)

        spend_by_model_df = pd.DataFrame(spend_by_model_data["model_spends"])
#        st.write(spend_by_model_df)
        #fig = px.histogram(spend_by_model_df, x = "model_name")
        fig = go.Figure(go.Bar(x=spend_by_model_df[spend_by_model_df.columns[0]],
                                y=list(spend_by_model_df.iloc[:,1]),
                                name=spend_by_model_df.columns[1]))

        for i in range(2, len(spend_by_model_df.columns),1):
            fig.add_trace(go.Bar(x=spend_by_model_df["model_name"],
                                y=spend_by_model_df.iloc[:,i],
                                name=spend_by_model_df.columns[i]))
        fig.update_layout(
        title={'text':"Spend by Model",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        xaxis_title="Models",
        yaxis_title="Spend [$ MM]",
        legend_title="Cells: ",
        font=dict(
            family="sans serif",
        )
        )
        col2_row1.plotly_chart(fig, use_container_width=False)

    row2 = st.container()

    with row2:
        col1, col2= st.columns(2)
    # age group split
        with col1:

                headers = {
                    'accept': 'application/json',
                }

                age_split_response = requests.get(f'{dns}/age_split/{selected_campaign}', headers=headers)
                age_split_data =age_split_response.json()

                labels = ['18-25','26-35','36-45','Others']
                values = [age_split_data["cat_18_25"],
                            age_split_data["cat_26_35"],
                            age_split_data["cat_36_45"],
                            age_split_data["others"]]

                fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
                fig.update_layout(
                title={'text':"Age Group Split",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                font=dict(
                    family="sans serif",
                )
                )
                st.plotly_chart(fig, use_container_width=False)
        with col2:
                headers = {
                    'accept': 'application/json',
                }

                gender_split_response = requests.get(f'{dns}/gender_split/{selected_campaign}', headers=headers)
                gender_split_data = gender_split_response.json()

                labels = ["Male", "Female"]
                values = [gender_split_data["male"]
                            ,gender_split_data["female"]]

                fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
                fig.update_layout(
                title={'text':"Gender Split",
                        'y':0.9,
                        'x':0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                font=dict(
                    family="sans serif",
                )
                )
                st.plotly_chart(fig, use_container_width=False)

    row3 = st.container()

    with row3:
        # headers = {
        #     'accept': 'application/json',
        # }

        datacard_response = requests.get(f'{dns}/datacard/{selected_campaign}')
        datacard_data = datacard_response.json()
        fig = go.Figure(data=go.Scatterpolar(
        r=ast.literal_eval(datacard_data["passion_points_levels"]),
        theta=ast.literal_eval(datacard_data["passion_points"]),
        fill='toself'
        ))

        fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True
            )
        ),
        showlegend=False
        )
        st.plotly_chart(fig, use_container_width=False)