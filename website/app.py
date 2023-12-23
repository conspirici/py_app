import streamlit as st

# ---assets---
nothing = "assets/co.png"
cat = "assets/cat.png"

st.set_page_config(page_title="me", page_icon="👌", layout="wide")

# ---header---
with st.container():
    st.subheader("Hii! my name is Mansoor :wave:")
    st.title("Software Engineering Student 🧑‍💻")
    st.write("I am passionate about learning Python; this is my first Python project")
    st.write("[my instagram 👽](https://www.instagram.com/mansoor_trimzi)")
    st.write("[my Git Hub 👾](https://github.com/conspirici)")

# ---what I do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do:")
        st.write("##")
        st.write("""It's my third semester in COMSATS University Abbottabad Campus, 
                 I am doing Major in Software Engineering, up till now I have learned basics of C++, 
                 and OOP in Java, apart from coding I like Sketching, Singing and going to Gym""")
    with right_column:
        st.image(cat, width=400)

with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(nothing, width=200)
    with text_column:
        st.subheader("I created nothing up till now 💀")
        st.write("##")
        st.write("but I will definitely create something after a while")

# ---contact form---
with st.container():
    st.write("---")
    st.header("Lets Connect")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/sydmnsur@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

st.markdown(
    """
    <style>
        /* Style inputs with type="text", select elements, and textareas */
        input[type=message], input[type=email], input[type=text], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #333;
            border-radius: 4px;
            box-sizing: border-box;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
            color: white;
            background-color: #111;
        }

        /* Style the submit button with a specific background color, padding, etc. */
        button[type=submit] {
            background-color: #111;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        /* When moving the mouse over the submit button, add a darker green color */
        button[type=submit]:hover {
            background-color: white;
            color: #111;
        }

        /* Solid Black Background */
        body {
            background-color: #000;
        }

        /* Hide Streamlit Branding */
        #MainMenu, footer, header {
        visibility: hidden;

        
        }
    </style>
    """,
    unsafe_allow_html=True,
)
