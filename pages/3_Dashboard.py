import streamlit as st
import plotly.graph_objects as go
#containers
st.markdown("<h1 style='text-align: center;'>Campaign Summary Stats", unsafe_allow_html=True)

card_container = st.container()


with card_container:
    col1, col2, col3= st.columns(3)
    col1.metric("AUDIENCE SIZE", "3,680,415")
    col1.metric("CAMPAIGN SPEND", "$ 200,000")
    col2.metric("CAMPAIGN START", "21-03-2022")
    col2.metric("CAMPAIGN END", "21-04-2022")
    col3.metric("OBJECTIVE", "Consideration")
    col3.metric("VEHICLE", "Meta")

row1 = st.container()

with row1:
#spend by group
    col1_row1, col2_row1 = st.columns(2)
    groups =['Control Group','Test Group']
    fig = go.Figure([go.Bar(x=groups, y = [46.27, 58.07])])
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
    x=['Model A', 'Model B', 'Model C', 'Model D']

    fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='cell A1'))
    fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='cell A2'))
    fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='cell A3'))
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
            labels = ['18-25','26-35','36-50','50-100']
            values = [4500, 2500, 1053, 500]

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
            labels = ['Male','Female']
            values = [7600, 8200]

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
    fig = go.Figure(data=go.Scatterpolar(
    r=[4, 5, 2, 2, 3],
    theta=['Fitness','Music','Gaming', 'Travel',
            'Sports'],
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