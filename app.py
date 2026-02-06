import streamlit as st

st.set_page_config(page_title="Lumina Care")

st.title("Lumina Care")
menu = ["Profile", "Care Plan", "Resources", "Safety"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Profile":
    st.header("Patient Profile")
    st.text_input("Name", value="Robert Miller")
    st.number_input("Age", value=82)
    st.selectbox("Stage", ["Early", "Middle", "Late"])
    st.text_area("Medical History")
    st.text_input("Emergency Contact", value="555-0199")
    st.button("Save Profile")

elif choice == "Care Plan":
    st.header("Daily Care Plan")
    st.checkbox("08:00 AM - Medication")
    st.checkbox("10:00 AM - Morning Walk")
    st.checkbox("06:00 PM - Dinner")
    st.button("Add to Schedule")

elif choice == "Resources":
    st.header("Resource Hub")
    st.write("Early: Forgetfulness")
    st.write("Middle: Confusion and Wandering")
    st.write("Late: Physical Decline")

elif choice == "Safety":
    st.header("Safety Alerts")
    status = st.radio("Status", ["Safe", "Wandering"])
    if status == "Wandering":
        st.error("ALERT: Patient outside safe zone!")
    else:
        st.success("Patient is safe.")

st.sidebar.write("Security: Encrypted")
