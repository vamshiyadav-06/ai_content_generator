import streamlit as st
import requests

BACKEND_URL = st.secrets["be_server_url"]

st.set_page_config(
    page_title="AI Content Genergitator",
    layout="wide"
)

st.title("AI Content Generator")
st.write("Generate Blogs, LinkedIn Posts, Captions, Emails and more")

topic = st.text_input("Enter your Topic here")

technology = st.selectbox(
    "Select Technology",
    [
        "python",
        "java",
        "mern",
        "flutter",
        "react",
        "angular",
        "nodejs",
        "api",
        "agentic ai",
        "generative ai",
        "deep learning"
    ]
)

content_type = st.selectbox(
    "Select Content Type",
    [
        "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Facebook Post",
        "Email",
        "YouTube Description",
        "Product Description",
        "Ad Copy",
        "Other"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
    ]
)

generate_button = st.button("Generate")

if generate_button:
    if not topic.strip():
        st.error("Please enter a topic")
    else:
        with st.spinner("Generating content..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    params={
                        "topic": topic,
                        "technology": technology,
                        "content_type": content_type,
                        "tone": tone
                    }
                )

                st.write("Status Code:", response.status_code)

                result = response.json()

                st.success("Content Generated Successfully")

                st.subheader("Generated Content")
                st.write(result.get("content", "No content returned"))

            except Exception as e:
                st.error(f"Error: {e}")