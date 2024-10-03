import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("User Activity Dashboard")

# Light/Dark theme toggle
theme = st.radio("Choose Theme", ["Light", "Dark"])

# Apply the chosen theme (Note: Streamlit doesn't directly support this but we can customize the page)
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown(
        """
        <style>
        body {
            background-color: white;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

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
        # Filter the dataframe by the selected user
        filtered_df = df[df['Name'] == selected_name]

        # Group tasks by Status
        status_groups = filtered_df.groupby('Status')

        # Display tasks in card-like components
        for status, group in status_groups:
            st.subheader(f"Status: {status}")

            for index, row in group.iterrows():
                # Using st.write to simulate card-like appearance
                st.markdown(
                    f"""
                    <div style="border:1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px;">
                        <strong>Description:</strong> {row['Description']} <br>
                        <strong>Count:</strong> {row['Count']} <br>
                        <strong>Status:</strong> {row['Status']}
                    </div>
                    """, unsafe_allow_html=True
                )

        # Optionally, we can still show the bar chart for an overview
        fig = px.bar(filtered_df, x='Description', y='Count', color='Status', title=f'Activities for {selected_name}')
        st.plotly_chart(fig)
