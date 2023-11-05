import streamlit as st

with st.container():
    st.title("Information Technology")
    st.subheader("Free courses")

    # Define a list of blocks with titles and URLs
    blocks = [
        {"title": "Diploma in Information Technology Management", "url": "https://alison.com/course/diploma-in-information-technology-management-revised-2017", "border_color": "red"},
        {"title": "Security Management", "url": "https://alison.com/course/security-management", "border_color": "blue"},
        {"title": "Office 365 for End Users", "url": "https://alison.com/course/office-365-for-end-users", "border_color": "green"},
         {"title": "Other", "url": "https://alison.com/courses?query=iT", "border_color": "pink"},
    ]

    # Create equally spaced columns for the blocks
    cols = st.columns(3)

    for i, block in enumerate(blocks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <a href="{block['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="border: 2px solid {block['border_color']}; padding: 10px; border-radius: 5px; cursor: pointer;">
                        <h3>{block['title']}</h3>
                        Expand your knowledge and take these free courses.
                    </div>
                    <br>
                </a>
                """,
                unsafe_allow_html=True
            )

with st.container():
    st.title("Agriculture")
    st.subheader("Free courses")

    # Define a list of blocks with titles and URLs
    blocks = [
        {"title": "How to Manage a Poultry Farming Business", "url": "https://alison.com/course/how-to-manage-a-poultry-farming-business", "border_color": "purple"},
        {"title": "Diploma in Dairy, Food Process and Product Technology", "url": "https://alison.com/course/security-management", "border_color": "orange"},
        {"title": "Introduction to Arboriculture", "url": "https://alison.com/course/introduction-to-arboriculture", "border_color": "grey"},
        {"title": "Other", "url": "https://alison.com/tag/farming?utm_source=google&utm_medium=cpc&utm_campaign=Performance-Max_Tier-3_First-Click-Targeting-III&gclid=CjwKCAjw15eqBhBZEiwAbDomEjHRHfQmnxuxmKmvyhE2j3q5vxRwvvzddm0A4J7b54b9_MmOx6m9jhoC2ZQQAvD_BwE&tgac=dXhoZWs7VHJhZmZpY0d1YXJkO1RyYWZmaWNHdWFyZEF1ZGllbmNlO2M3ZDgyODdkNjZkNWE0ZjlkZGNiMWJiMzM2OWQyYWJkNGM0OTZmY2VmY2NjYTEyODZhZGRjNzdhYjhiZjNjNWY%3D", "border_color": "pink"},
    ]

    # Create equally spaced columns for the blocks
    cols = st.columns(3)

    for i, block in enumerate(blocks):
        with cols[i % 3 ]:
            st.markdown(
                f"""
                <a href="{block['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="border: 2px solid {block['border_color']}; padding: 10px; border-radius: 5px; cursor: pointer;">
                        <h3>{block['title']}</h3>
                        Expand your knowledge and take these free courses.
                    </div>
                    <br>
                </a>
                """,
                unsafe_allow_html=True
            )
            

with st.container():
    st.title("Law Enforcement")
    st.subheader("Free courses")

    # Define a list of blocks with titles and URLs
    blocks = [
        {"title": "Introduction to Legal Concepts", "url": "https://alison.com/course/introduction-to-legal-concepts?utm_source=google&utm_medium=cpc&utm_campaign=PPC_Tier-3_First-Click_Publisher-Courses&utm_adgroup=Course-2139_Introduction-to-Legal-Concepts&gclid=CjwKCAjw15eqBhBZEiwAbDomEuoDlAr0abJa_wX3YtJMcUm_8RGzODb5CEHRTCo620o7FzxIcPhOmRoCJdMQAvD_BwE", "border_color": "red"},
        {"title": "Basics of Business Law", "url": "https://alison.com/course/basics-of-business-law", "border_color": "blue"},
        {"title": "Fundamentals of Commercial Law", "url": "https://alison.com/course/fundamentals-of-commercial-law", "border_color": "green"},
        {"title": "Other", "url": "https://alison.com/courses?query=law", "border_color": "pink"},
    ]

    # Create equally spaced columns for the blocks
    cols = st.columns(3)

    for i, block in enumerate(blocks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <a href="{block['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="border: 2px solid {block['border_color']}; padding: 10px; border-radius: 5px; cursor: pointer;">
                        <h3>{block['title']}</h3>
                        Expand your knowledge and take these free courses.
                    </div>
                    <br>
                </a>
                """,
                unsafe_allow_html=True
            )
            
with st.container():
    st.title("Medicine")
    st.subheader("You may need to pay to take these courses")

    # Define a list of blocks with titles and URLs
    blocks = [
        {"title": "Vital Signs", "url": "https://www.coursera.org/learn/vital-signs", "border_color": "white"},
        {"title": "Anatomy Specialization", "url": "https://www.coursera.org/specializations/anatomy", "border_color": "white"},
        {"title": "Become an EMT", "url": "https://www.coursera.org/specializations/become-an-emt", "border_color": "white"},
        {"title": "Other", "url": "https://www.coursera.org/courses?query=medical", "border_color": "pink"},
    ]

    # Create equally spaced columns for the blocks
    cols = st.columns(3)

    for i, block in enumerate(blocks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <a href="{block['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="border: 2px solid {block['border_color']}; padding: 10px; border-radius: 5px; cursor: pointer;">
                        <h3>{block['title']}</h3>
                      Expand your knowledge today.
                    </div>
                    <br>
                </a>
                """,
                unsafe_allow_html=True
            )
            
            
with st.container():
    st.title("Accounting")
    st.subheader("You may need to pay to take these courses")

    # Define a list of blocks with titles and URLs
    blocks = [
        {"title": "Introduction to Finance and Accounting", "url": "https://www.coursera.org/specializations/finance-accounting", "border_color": "white"},
        {"title": "Fundamentals of Accounting Specialization", "url": "https://www.coursera.org/specializations/accounting-fundamentals", "border_color": "white"},
        {"title": "Bookkeeping Basics", "url": "https://www.coursera.org/learn/bookkeeping-basics", "border_color": "white"},
        {"title": "Other", "url": "https://www.coursera.org/courses?query=accounting", "border_color": "pink"},
    ]

    # Create equally spaced columns for the blocks
    cols = st.columns(3)

    for i, block in enumerate(blocks):
        with cols[i % 3]:
            st.markdown(
                f"""
                <a href="{block['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                    <div style="border: 2px solid {block['border_color']}; padding: 10px; border-radius: 5px; cursor: pointer;">
                        <h3>{block['title']}</h3>
                     Expand your knowledge today.
                    </div>
                    <br>
                </a>
                """,
                unsafe_allow_html=True
            )
            