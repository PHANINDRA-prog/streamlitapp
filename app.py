import streamlit as st
import pandas as pd
import plotly.express as px

# File uploader widget
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded Excel file
    df = pd.read_excel(uploaded_file)

    # Dropdown for selecting a name
    selected_name = st.selectbox("Select a User", df['Name'].unique())

    if selected_name:
        filtered_df = df[df['Name'] == selected_name]

        # Loop through rows and display as cards with status-based borders
        for _, row in filtered_df.iterrows():
            status = row['Status']
            
            # Assign border color based on status
            if status == 'Done':
                border_color = 'green'
            elif status == 'In Progress':
                border_color = 'yellow'
            elif status == 'Backlog':
                border_color = 'red'
            else:
                border_color = 'gray'
            
            # Create card-style display for each task
            st.markdown(
                f"""
                <div class="card" style="border: 2px solid {border_color};">
                    <h3>{row['Description']}</h3>
                    <p>Status: {row['Status']}</p>
                    <p>Count: {row['Count']}</p>
                </div>
                """, unsafe_allow_html=True
            )

        # Create a bar chart showing activity counts with status-based coloring
        color_map = {
            'Done': 'green',
            'In Progress': 'yellow',
            'Backlog': 'red'
        }
        
        # Add a new column for the bar color based on status
        filtered_df['Bar Color'] = filtered_df['Status'].map(color_map)

        # Create the bar chart with the assigned colors
        fig = px.bar(
            filtered_df,
            x='Description',
            y='Count',
            title=f'Activities for {selected_name}',
            color='Bar Color',
            color_discrete_map=color_map
        )
        
        st.plotly_chart(fig)
