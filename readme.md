# Text to SQL Generator 📄 ➡️ 🗃️

### A powerful tool that allows users to upload SQL schema files and ask questions to automatically generate SQL queries and solve related problems using AI!

---

## 🚀 Project Overview

The **Text to SQL Generator** is a web-based application that leverages the power of Google's Generative AI (`gemini-1.5-flash`) to help users interact with SQL schemas and generate relevant SQL queries. By simply uploading an SQL schema in `.sql`, `.txt`, or `.pdf` format, users can ask natural language questions and get structured SQL queries in response. This tool is perfect for developers, database administrators, and anyone who wants to optimize SQL queries, troubleshoot issues, or generate insights from a database structure.

## ✨ Features

- **File Upload**: Users can upload SQL schema files in `.sql`, `.txt`, or `.pdf` format.
- **AI-Powered Query Generation**: Get context-aware SQL queries based on your schema and the question you ask.
- **Supports Multiple Tasks**:
  - Writing new SQL queries based on schema structure.
  - Optimizing existing SQL queries for performance.
  - Debugging SQL syntax errors.
  - Modifying query structures for specific use cases.
  - Generating insights based on the schema data structure.
- **Contextual Responses**: The AI analyzes your schema to understand its context, like whether it’s an e-commerce store, garage management system, sales database, etc.
- **Interactive Chat Interface**: Chat-based interface to interact with the AI, allowing users to ask natural language questions and get real-time SQL responses.

---

## 🛠️ Technologies Used

- **Streamlit**: For building an interactive web interface.
- **Google Generative AI (`gemini-1.5-flash`)**: For generating SQL queries and context from uploaded files.
- **PyPDF2**: For extracting text from uploaded PDF files.
- **Python**: Backend language for integrating file processing and AI interactions.

---

## 📥 Installation and Setup

Follow these steps to get the project up and running locally:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/text-to-sql-generator.git
cd text-to-sql-generator
```

### 2. Set Up Virtual Environment (Optional but Recommended):
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use: env\Scripts\activate
    ```

### 3. Install Required Packages:
    ```bash
    pip install -r requirements.txt
    ```

### 4. Set Up Google Generative AI API Key:
    You will need access to Google's Generative AI API (Gemini). Store your API key in Streamlit secrets.

    Create a .streamlit/secrets.toml file and add your API key:
    ```bash
    [GEMINI_API_KEY]
    api_key = "your_google_generative_ai_api_key"
    ```

### 5. Run the Application:
    ```bash
    streamlit run app.py
    ```

---

## 💡 Usage

### 1. Upload an SQL Schema:
   - On the sidebar, upload an .sql, .txt, or .pdf file containing your SQL schema.
   - The app will parse and extract the content from the file.

### 2. Understand the Schema:
   - The AI automatically generates a contextual overview of your SQL schema, explaining its structure (e.g., e-commerce, sales, etc.).

### 3. Ask Questions:
   - Enter a natural language question like:
     - "Generate a query to list all users who made a purchase."
     - "Show me the products with the highest rating."
     - "What are the total sales for each product category?"
   - The AI will provide you with efficient SQL queries based on your schema.

### 4. Interactive Chat:
   - All previous interactions are saved in the chat history, allowing users to see prior questions and SQL query responses.

---

## 🧪 Example

### 1. Upload a Sample SQL Schema:
    ```sql
    CREATE TABLE users (
        user_id INT PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE orders (
        order_id INT PRIMARY KEY,
        user_id INT,
        total_amount DECIMAL(10, 2),
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    ```

### 2. Ask the AI: 
    "Generate a query to find the total amount spent by each user."

### 3. SQL Response:
    ```sql
    SELECT u.username, SUM(o.total_amount) AS total_spent
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.username;
    ```

---

## 🛡️ License

This project is licensed under the MIT License. Feel free to contribute, fork, and enhance!

---

## 🙌 Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add a feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Open a Pull Request.

---

## ✉️ Contact

For any questions or issues, feel free to reach out:

- [Personal Portfolio Website](ankurvasani.netlify.app)
- GitHub: [AnkurVasani2](https://github.com/yourusername)

Happy coding! 🎉
"""