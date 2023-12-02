import folium
import streamlit as st
from streamlit_folium import st_folium

# Define the current page
current_page = st.session_state.get("current_page", "home")

# Home page
if current_page == "home":
    st.title("Home Page")
    st.image('Solar.png')
    st.write("Welcome to the Home Page!")

    # Button to go to the About page
    if st.button("Double Click to Go to Map demo Page"):
        st.session_state["current_page"] = "map"

# About page
elif current_page == "map":
    st.title("Map demo")
    st.write("This is the Map demo Page!")
    # The message and nested widget will remain on the page
    m = folium.Map(location=[21.502771, 39.247194], zoom_start=18)
    folium.Marker = m.add_child(folium.ClickForMarker("<b>Lat: </b> ${lat}<br/><b>Lon: </b> ${lng}<br><b>Altitude:</b> 10.00 m"))
    output = st_folium(m, width=700, height=500)
    if output["last_clicked"] is not None:
        output["last_clicked"]["alti"] = 10
        latitude_1_last_clicked    = round(output["last_clicked"]["lat"], 6)
        longitude_1_last_clicked   = round(output["last_clicked"]["lng"], 6)
        altitude_1_last_clicked    = output["last_clicked"]["alti"]
        st.write("• Latitude:", latitude_1_last_clicked)
        st.write("• Latitude:", longitude_1_last_clicked)
        st.write("• Altitude:", altitude_1_last_clicked, "meter")
    # Button to go back to the Home page
    if st.button("Double Click to Go to Home Page"):
        st.session_state["current_page"] = "home"
