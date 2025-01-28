import streamlit as st
from streamlit_option_menu import option_menu  # For a better sidebar menu
from PIL import Image  # For handling icons

# Set page configuration
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #1E3A8A; /* Dark blue */
        color: white;
    }
    .sidebar .sidebar-content .stButton button {
        background-color: #3B82F6; /* Light blue */
        color: white;
        border-radius: 5px;
        padding: 10px;
        width: 100%;
    }
    .sidebar .sidebar-content .stButton button:hover {
        background-color: #2563EB; /* Darker light blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with options
with st.sidebar:
    st.title("My Profile")
    st.markdown("---")

    # Use option_menu for a better sidebar experience
    selected = option_menu(
        menu_title=None,
        options=["About Me", "My Experience", "Education", "Skills", "Projects", "Languages"],
        icons=["person-fill", "briefcase-fill", "book-fill", "tools", "folder-fill", "translate"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#1E3A8A"},  # Dark blue
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "white",
                "border-radius": "5px",
                "padding": "10px",
            },
            "nav-link-selected": {"background-color": "#3B82F6"},  # Light blue
        },
    )

# Main content based on selected option
if selected == "About Me":
    st.header("About Me")
    st.write("""
    Hello! I am a passionate website designer with a strong focus on creating beautiful and functional websites. 
    I have experience in UI/UX design, front-end development, and working with clients to deliver high-quality solutions.
    """)

elif selected == "My Experience":
    st.header("My Experience")
    st.write("""
    - **Web Designer** at XYZ Company (2020 - Present)
      - Designed and developed responsive websites.
      - Collaborated with clients to understand their needs.
    - **Freelance Designer** (2018 - 2020)
      - Worked on various projects, including e-commerce sites and portfolios.
    """)

elif selected == "Education":
    st.header("Education")
    st.write("""
    - **Bachelor of Science in Computer Science**  
      University of ABC (2015 - 2019)
    - **Certification in UI/UX Design**  
      Online Course (2020)
    """)

elif selected == "Skills":
    st.header("Skills")
    st.subheader("Soft Skills")
    st.write("- Communication")
    st.write("- Teamwork")
    st.write("- Problem Solving")

    st.subheader("Technical Skills")
    st.write("- HTML, CSS, JavaScript")
    st.write("- Python, Streamlit")
    st.write("- Adobe XD, Figma")

elif selected == "Projects":
    st.header("Projects")
    st.write("""
    - **Portfolio Website**  
      Designed and developed a personal portfolio website to showcase my work.
    - **E-commerce Platform**  
      Created a fully functional e-commerce website for a client.
    - **Blog Website**  
      Built a blog platform using Streamlit and Python.
    """)

elif selected == "Languages":
    st.header("Languages")
    st.write("""
    - English (Fluent)
    - French (Intermediate)
    - Spanish (Basic)
    """)
