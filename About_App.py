### Contents of the main file ###
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# This is the New York Vehicle Collision Report! 👋")

#st.sidebar.success("Select a demo above.")

st.markdown(
    """
    The global collision index is continuously recording greater levels of accidents. The statistics speak for 
    themselves and they are quite concerning. Each year, 1.35 million are killed in transit-related accidents
    worldwide. This figure translates into a daily 3,700 people killed in crashes in which the most affected 
    are pedestrians, motorcyclists, and cyclists, representing almost half of the parties killed. As this figure
    exacerbates year over year, it is relevant to provide an outlook on New York City’s vehicle collision record as 
    one of the foremost economic hubs in the USA. This report will help individuals and organizations
    within New York City to be aware of the situation concerning vehicle collisions by visualizing the 
    locations with the greatest collision index, displaying the main causes leading to collisions, and 
    comparing the aftermath in injured-killed parties. 
"""
)

#collision image?
