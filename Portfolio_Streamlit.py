import streamlit as st

# Set up the page config
st.set_page_config(page_title="Sadia - Developer Portfolio", page_icon=":sparkles:", layout="wide")

# Define CSS for custom styling
st.markdown("""
    <style>
        .big-font {
            font-size: 36px !important;
            font-weight: bold;
        }
        .nav-bar {
            background-color: #0b0b2b;
            color: white;
            padding: 10px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .nav-bar a {
            text-decoration: none;
            color: white;
            margin: 0 15px;
            font-size: 18px;
            font-weight: 500;
        }
        .nav-bar a:hover {
            color: #a4a4e1;
        }
        .section-title {
            font-size: 28px;
            color: #4040a7;
            margin-bottom: 15px;
            font-weight: bold;
        }
        .text-gray {
            color: gray;
        }
        .section-content {
            background-color: #000017;
            color: white;
            padding: 40px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            margin-bottom: 30px;
            text-align: center;
        }
        .btn {
            padding: 12px 20px;
            background: #1e2167;
            color: white;
            border: 2px solid white;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin: 5px;
            transition: background 0.3s, border 0.3s, transform 0.3s;
        }
        .btn:hover {
            background: #ffffff;
            color: #1e2167;
            border: 2px solid #1e2167;
            transform: scale(1.05);
        }
        .hero-img {
            width: 100%;
            max-width: 600px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        footer {
            background-color: #0e0e1a;
            color: gray;
            padding: 30px 0;
            text-align: center;
            border-top: 1px solid #444;
            position: relative;
        }
        footer .footer {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            padding: 20px;
        }
        footer h3 {
            margin-bottom: 15px;
            color: #a4a4e1;
        }
        footer ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        footer ul li {
            margin: 8px 0;
        }
        .card, .resource-card {
            background-color: #1e2167;
            color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }
        .card h3, .resource-card h3 {
            font-size: 22px;
        }
        .resource-card {
            background-color: #000017;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="nav-bar">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#hobbies">Hobbies</a>
        <a href="#mission">Mission</a>
        <a href="#resources">Resources</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# Main content with centered title
st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <h1>Sadia Sakharkar</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* Ensure the section content adapts to different screen sizes */
        .section-content {
            max-width: 90%; /* Adjust width to fit mobile screens */
            margin: auto; /* Center the content */
            padding: 10px; /* Add padding to avoid touching screen edges */
        }
        /* Flexbox adjustment for small screens */
        @media only screen and (max-width: 600px) {
            .big-font {
                font-size: 24px; /* Decrease font size on small screens */
                text-align: center; /* Center align text */
            }
            .section-content p {
                font-size: 16px; /* Decrease paragraph font size */
                text-align: justify; /* Justify text to avoid splitting */
            }
            .btn {
                display: block; /* Buttons on mobile should be stacked */
                width: 100%;
                margin-top: 10px; /* Space between buttons */
            }
        }
    </style>
    
    <div id="home" class="section-content">
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h1 class="big-font">Welcome to My Portfolio!</h1>
            <p>Hello! I'm Sadia Sakharkar, a passionate developer dedicated to crafting innovative solutions and exploring the latest technologies. From building sleek and user-friendly interfaces to diving into the world of AI and machine learning, my goal is to create impactful experiences and drive technological advancement.</p>
            <p>Feel free to browse through my skills, learn about my hobbies, and get to know my mission and the resources I recommend. If you have any questions or just want to connect, don’t hesitate to reach out!</p>
            <div style="margin-top: 20px;">
                <a href="mailto:sakharkarsadia@gmail.com?subject=Request for Resume" class="btn">Request Resume via Email</a>
                <a href="https://github.com/sadiasakharkar" target="_blank" class="btn">Visit Github</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)

# Skills Section with Accordion
st.markdown("""
    <div id="skills" class="section-content">
        <h2 class="section-title">My Skills</h2>
        <p>Here’s a look at the technologies and tools I excel in:</p>
""", unsafe_allow_html=True)

skills = [
    ("C ", "As a C Developer, I excel in crafting high-performance applications with efficiency and precision. My experience with C programming has equipped me with the skills to tackle system-level programming, develop robust algorithms, and create optimized solutions for complex computational problems."),
    ("C++ ", "In C++, I bring object-oriented programming principles to life, developing scalable and maintainable software. My expertise includes creating complex data structures, implementing advanced algorithms, and ensuring efficient memory management to build high-quality applications."),
    ("Java ", "My journey as a Java Developer has been driven by a passion for building versatile, platform-independent applications. I specialize in developing enterprise-level solutions, leveraging Java’s powerful frameworks, and ensuring seamless integration and performance across various environments."),
    ("Python ", "I have a foundational understanding of Python, and I am gaining hands-on experience with its applications. I am learning to use Python for web development, data analysis, and exploring its capabilities in machine learning. My goal is to deepen my proficiency and leverage Python for diverse projects."),
    ("HTML ", "With a deep understanding of HTML, I create well-structured and accessible web pages that serve as the foundation for exceptional user experiences. My expertise includes semantic HTML, responsive design, and ensuring cross-browser compatibility for a flawless web presence."),
    ("CSS ", "As a CSS Developer, I transform web designs into visually stunning and user-friendly interfaces. I excel in creating responsive layouts, implementing modern design trends, and optimizing styles for performance and consistency across different devices and screen sizes."),
    ("JavaScript ", "As a JavaScript Developer, I excel in creating interactive and dynamic web experiences. My expertise includes working with modern JavaScript frameworks and libraries, developing client-side functionalities, and ensuring responsive and engaging user interfaces."),
    ("MongoDB ", "With experience in MongoDB, I manage and design NoSQL databases for scalable and high-performance applications. My skills include data modeling, query optimization, and ensuring efficient data management to support robust and flexible application architectures."),
    ("AI/ML Enthusiast", "I am currently exploring the exciting field of AI/ML, learning about its potential to revolutionize various industries. While I am still developing my expertise, I am enthusiastic about applying AI/ML concepts to real-world problems and expanding my knowledge in this cutting-edge domain.")
]


for title, description in skills:
    with st.expander(title):
        st.write(description)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Hobbies Section
st.markdown("""
    <div id="hobbies" class="section-content">
        <h2 class="section-title">Technical Hobbies & Interests</h2>
        <p>Here are some of my technical hobbies and interests that keep me motivated and inspired:</p>
        <ul>
            <li><strong>Open Source Contributions:</strong> I actively contribute to open source projects, which helps me stay engaged with the developer community and learn from real-world codebases.</li>
            <li><strong>Competitive Programming:</strong> Participating in coding competitions sharpens my problem-solving skills and keeps me updated with algorithmic techniques.</li>
            <li><strong>Building Personal Projects:</strong> I enjoy working on personal projects that challenge my skills and allow me to experiment with new technologies.</li>
            <li><strong>Tech Meetups & Webinars:</strong> Attending tech meetups and webinars helps me stay informed about the latest trends and developments in the tech world.</li>
        </ul>
        <p>Outside of my professional work, I enjoy a variety of hobbies that keep me inspired and motivated:</p>
        <ul>
            <li><strong>Photography:</strong> Capturing moments and creating visual stories is a passion of mine. I love exploring different techniques and styles to enhance my photography skills.</li>
            <li><strong>Traveling:</strong> Discovering new cultures and places enriches my perspective and creativity. Traveling allows me to learn from diverse experiences and gain fresh insights.</li>
            <li><strong>Reading Fiction:</strong> I enjoy immersing myself in fictional worlds, which helps me unwind and spark creativity for my work.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Mission Section
st.markdown("""
    <div id="mission" class="section-content">
        <h2 class="section-title">My Mission</h2>
        <p>My mission is to harness the power of technology to create meaningful and impactful solutions. I strive to continually enhance my skills, stay updated with the latest advancements, and contribute to projects that make a positive difference in the world. My goal is to be at the forefront of innovation, developing technologies that solve real-world problems and improve the quality of life for individuals and communities.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Resources Section
st.markdown("""
    <div id="resources" class="section-content">
        <h2 class="section-title">Recommended Resources</h2>
        <p>Explore these valuable resources for learning and enhancing your programming skills:</p>
        <ul>
            <li><a href="https://www.youtube.com/@CodeWithHarry" target="_blank">Code with Harry YouTube Channel</a> - Features detailed tutorials and projects in various programming languages.</li>
            <li><a href="https://www.freecodecamp.org/" target="_blank">FreeCodeCamp</a> - Provides comprehensive, free tutorials and projects on web development technologies.</li>
            <li><a href="https://docs.python.org/" target="_blank">Official Python Documentation</a> - Essential for understanding Python’s features and best practices.</li>
            <li><a href="https://www.oracle.com/java/" target="_blank">Official Java Documentation</a> - Explore Java programming with official resources from Oracle.</li>
            <li><a href="https://en.cppreference.com/" target="_blank">C++ Reference</a> - A detailed reference for C++ programming, including language features and libraries.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)


# Contact Section
st.markdown("""
    <div id="contact" class="section-content">
        <h2 class="section-title">Contact Me</h2>
        <p>If you have any questions or would like to connect, feel free to reach out via email or connect with me on LinkedIn:</p>
        <p>Email: <a href="mailto:sakharkarsadia@gmail.com" style="color: #a4a4e1;">sakharkarsadia@gmail.com</a></p>
        <p>LinkedIn: <a href="https://www.linkedin.com/in/sadiasakharkar" target="_blank" style="color: #a4a4e1;">Sadia Sakharkar</a></p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer>
        <div class="footer">
            <div>
                <h3>About Me</h3>
                <p>I am a developer with a passion for creating innovative solutions and exploring new technologies. My goal is to make a positive impact through my work and continuously grow in my field.</p>
            </div>
            <div>
                <h3>Contact</h3>
                <p>Email: <a href="mailto:sakharkarsadia@gmail.com" style="color: #a4a4e1;">sakharkarsadia@gmail.com</a></p>
                <p>LinkedIn: <a href="https://www.linkedin.com/in/sadiasakharkar/" target="_blank" style="color: #a4a4e1;">Sadia Sakharkar</a></p>
            </div>
            <div>
                <h3>Follow Me</h3>
                <p><a href="https://github.com/sadiasakharkar" target="_blank" style="color: #a4a4e1;">GitHub</a></p>
                <p><a href="https://www.linkedin.com/in/sadiasakharkar/" target="_blank" style="color: #a4a4e1;">LinkedIn</a></p>
            </div>
        </div>
    </footer>
""", unsafe_allow_html=True)
