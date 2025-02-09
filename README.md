***SQLite Chat Assistant***

A simple chatbot for interacting with an SQLite database using natural language queries.

This project is designed to understand and process user queries related to employees and departments stored in an SQLite database. Instead of using an AI model, the chatbot follows a rule-based approach to convert user queries into SQL statements.

***How It Works***

1. User inputs a natural language query (e.g., "Show me all employees in the Sales department.").
2. The chatbot matches the query to predefined patterns using regular expressions.
3. It converts the query into an SQL statement (e.g., SELECT * FROM Employees WHERE Department = 'Sales';).
4. The chatbot executes the SQL query on an SQLite database (database.db).
5. The result is displayed in the chat interface.

***Alternative Approach Using Phi3Mini (Still in Progress)***

I originally planned to use Meta’s Phi3Mini model via Ollama to dynamically generate SQL queries. However, I encountered some solvable technical issues (e.g., incorrect SQL formatting, multi-statement execution errors).
Due to time constraints, I am submitting this rule-based approach for now, but I am still working on integrating Phi3Mini and plan to improve this assistant with LLM support.

***Running the Project Locally***

1. Install the depenencies : flask sqlite3
2. Clone the repo
3. Run the app.py file
4. Ask the query in the dialog box like : 'List all employees hired after 2021-01-01'

***Limitations and improvements***
   1. Current version is rule based approch
   2. No support ot nested conditions(complex queries)
   3. Phi3mini model integration is in progress. Once complete, it will be able to do more natural and dynamic query generation.
