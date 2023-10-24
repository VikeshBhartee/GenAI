# blog_app.py

import streamlit as st

# Sample data
blog_posts = [
    {"title": "Deep Learning Basics", "description": "Introduction to deep learning concepts.", "tags": ["AI", "Deep Learning"]},
    {"title": "Web Development with Flask", "description": "Building web apps using Flask.", "tags": ["Web Development", "Flask"]},
    {"title": "Data Visualization Techniques", "description": "Visualizing data using Python.", "tags": ["Data Science", "Visualization"]},
    # ... add more blog posts
]

def main():
    st.title("Blog Post Recommender")

    # Get unique tags from the blog posts
    unique_tags = list(set(tag for post in blog_posts for tag in post["tags"]))
    
    # Capture user's area of interest
    selected_tags = st.multiselect("Select your areas of interest:", unique_tags)

    # Filter and display recommended blog posts
    st.subheader("Recommended Blog Posts:")
    for post in blog_posts:
        if any(tag in selected_tags for tag in post["tags"]):
            st.write(f"**{post['title']}**")
            st.write(post['description'])
            st.write(f"*Tags: {', '.join(post['tags'])}*")
            st.write("---")

if __name__ == "__main__":
    main()
