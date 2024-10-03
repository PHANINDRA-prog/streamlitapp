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

    # Dropdown for selecting a user
    selected_name = st.selectbox("Select a User", df['Name'].unique())

    if selected_name:
        filtered_df = df[df['Name'] == selected_name]

        # Create a tree map-like structure based on status
        status_counts = filtered_df.groupby('Status').sum().reset_index()

        # Create cards for each status
        for _, row in status_counts.iterrows():
            if row['Status'] == 'Done':
                border_color = 'green'
            elif row['Status'] == 'In Progress':
                border_color = 'yellow'
            elif row['Status'] == 'Backlog':
                border_color = 'red'
            else:
                border_color = 'gray'  # Default color for other statuses

            st.markdown(
                f"""
                <div style="border: 2px solid {border_color}; border-radius: 5px; padding: 10px; margin: 10px 0;">
                    <h4>{row['Status']}</h4>
                    <p>Count: {row['Count']}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )

        # Plotting the activities as a bar chart
        fig = px.bar(filtered_df, x='Description', y='Count', title=f'Activities for {selected_name}')
        st.plotly_chart(fig)
