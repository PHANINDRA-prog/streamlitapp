import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("User Activity Dashboard")

# File uploader widget
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded Excel file
    df = pd.read_excel(uploaded_file)

    # Display the DataFrame
    st.write("Data Overview:")
    st.dataframe(df)

    # Dropdown for selecting a name
    selected_name = st.selectbox("Select a User", df['Name'].unique())

    if selected_name:
        filtered_df = df[df['Name'] == selected_name]
        fig = px.bar(filtered_df, x='Description', y='Count', title=f'Activities for {selected_name}')
        st.plotly_chart(fig)
