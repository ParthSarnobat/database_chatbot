import sqlite3
import re
from flask import Flask, request, jsonify

app = Flask(__name__, static_folder=".", static_url_path="")

def generate_sql_query(user_query):
    """Rule-based approach to generate SQL from natural language."""
    
    user_query = user_query.lower()

    match = re.search(r"employees in the (\w+) department", user_query)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT * FROM Employees WHERE Department = '{department}';"

    match = re.search(r"manager of the (\w+) department", user_query)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT Manager FROM Departments WHERE Name = '{department}';"

    match = re.search(r"hired after (\d{4}-\d{2}-\d{2})", user_query)
    if match:
        date = match.group(1)
        return f"SELECT * FROM Employees WHERE Hire_Date > '{date}';"

    match = re.search(r"total salary expense for the (\w+) department", user_query)
    if match:
        department = match.group(1).capitalize()
        return f"SELECT SUM(Salary) FROM Employees WHERE Department = '{department}';"

    return "SELECT 'Invalid Query: Unable to process your request';"

def query_db(sql_query):
    """Executes the generated SQL query on SQLite database."""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        result = str(e)
    conn.close()
    return result

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/query", methods=["GET"])
def chat_assistant():
    user_query = request.args.get("q")
    
    sql_query = generate_sql_query(user_query)
    
    result = query_db(sql_query)

    return jsonify({"query": sql_query, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
