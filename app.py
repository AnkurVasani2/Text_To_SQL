import streamlit as st
import PyPDF2
import google.generativeai as ai

# Initialize Google generative AI client
ai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = ai.GenerativeModel("gemini-1.5-flash")

# Set page configuration with title and favicon
st.set_page_config(
    page_title="Text To SQL Generator",
    page_icon="📝",
    layout="wide"
)

# Sidebar for file upload
file_content = ''
with st.sidebar:
    st.header("Upload the SQL Schema")

    # File uploader accepting .sql, .txt, and .pdf files
    uploaded_file = st.file_uploader("Choose a SQL Schema file", type=["sql", "txt", "pdf"])

    if uploaded_file is not None:
        try:
            # If it's a .txt or .sql file, read and decode the content
            file_content = uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            # If it's a PDF, use PyPDF2 to extract the text
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            file_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                file_content += page.extract_text()
        
        # Display success message for file upload
        st.write("File Uploaded Successfully")
    else:
        st.write("No file uploaded yet")

# Title of the app
st.title("Text To SQL Generator")

# Generate context from the uploaded SQL schema
if file_content:  # Ensure file content is not empty
    context_template = f"""I am working with the following SQL file content:

    {file_content}

    Based on the content above, please assist me with the following task:

    Give me the context of the SQL file. Respond only with the main context like what the database is all about, for example: an e-commerce store, a garage, a sales database, etc.

    Respond stricly in the following format: 
    
    The database appears to be designed for: 
    """
    
    try:
        context_reply = model.generate_content(context_template)
        if context_reply:
            st.chat_message("assistant").markdown(context_reply.text)
            
    except Exception as e:
        st.error(f"An error occurred while generating context: {e}")

# Initialize session state to hold chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input from chat
prompt = st.chat_input("Ask Anything")
st.chat_message("assistant").markdown("Hello, User!")
# Generate a prompt for the Google AI model based on the SQL schema and user input
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Create the template for the AI request
    template = f"""
    I am working with the following SQL file content:

    file_content:
    {file_content}

    Based on the content above, please assist me with the following task:

    {prompt}

    The task could involve:
    - Writing new SQL queries based on the given schema or tables.
    - Optimizing existing SQL queries for performance.
    - Debugging SQL syntax errors.
    - Modifying the structure of SQL queries to suit specific use cases.
    - Generating insights from the data structure.

    Ensure that the SQL output is efficient and follows best practices.

    If you encounter anything not related to SQL in the prompt variable, just say "Not Acceptable" or "Unacceptable Input".

    If your response include a explanation just give the explanation in bullet points and no extra text after that.

    Also if you encounter any error for example a table asked is not really present then respond Table Not Available in the Database Schema.

    For any Errors or Confusions reply only in one sentence.

    If your response gets a reply like: It does not work, generate another ,etc then dont ask for the file contents again. instead use your memmory to 
    recollect the file_contents provided earlier
    """

    # Call Google AI API using the specified syntax
    try:
        # Generate a response based on the user's prompt
        reply = model.generate_content(template)
        st.chat_message("ai").markdown(reply.text)
        st.session_state.messages.append({"role": "ai", "content": reply.text})

    except Exception as e:
        st.error(f"An error occurred: {e}")
