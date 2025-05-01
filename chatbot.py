import re

def answer(q):
    q = q.lower().strip()

    if re.fullmatch(r"hi|hello", q):
        return "Hello! How can I assist you today?"
    elif re.search(r"\b(your name|who are you)\b", q):
        return "My name is ELARA! I am a powerful python / JavaScript integrated chatbot meant to assist you with many tasks!"
    elif re.fullmatch(r"restart", q):
        return "__restart__"
    elif re.search(r"\b(add|plus)\b", q):
        return str(eval(q.replace("plus", "+")))
    elif re.fullmatch(r"[\d\s\+\-\*/\.\(\)]+", q):  # Only math allowed here
        try:
            return str(eval(q))
        except:
            return "I couldn't do that math."
    elif re.search(r"\b(roadmap|your future development)\b", q):
        return """Below is my roadmap:
        \n1. Increase query reading reliability
        \n2. Give more personality
        \n3. Improve my knowledge base
        \n4. Integrate more abilities (coding for example)"""
    elif "how developed" in q and "you" in q:
        return "Currently my developer says I am in 'stage 1.0' so they are focusing on increasing my query reading reliability"
    elif re.search(r"\b(how does ELARA work|how does ELARA function|how do you work)\b", q):
        return """ELARA (Engineering Logic & Analysis Relay Assistant) operates by integrating several core technologies, including artificial intelligence (AI), natural language processing (NLP), Python code execution, and access to external resources like Wikipedia. Here's a breakdown of how it functions:

        1. **User Input Capture**: When you type a question or command into the input box, the input is captured by the HTML form on the frontend. This input is then sent to the backend for processing.

        2. **Processing the Query**: 
            - ELARA uses natural language processing (NLP) techniques to understand the meaning behind the user's input. It breaks down the text, analyzes sentence structure, and extracts key pieces of information.
            - If the query matches certain keywords or patterns, ELARA identifies the intent and can respond accordingly.

        3. **Python Integration (via Pyodide)**:
            - ELARA runs Python code through Pyodide, a WebAssembly-based Python interpreter that runs in the browser. Pyodide allows ELARA to execute Python scripts directly in the user's browser without needing to rely on an external server.
            - This is particularly useful for more advanced tasks, such as data processing, running calculations, or generating responses based on logic.

        4. **Response Generation**:
            - Based on the processed query and the result from the Python script, ELARA generates a response. This could be a direct answer to a question, a suggestion, or an action prompt.
            - For example, if the query is asking for specific information (like "What is Python?"), ELARA can either generate the answer itself or fetch it from an external resource like Wikipedia.

        5. **Fallback to External Resources (e.g., Wikipedia)**:
            - If ELARA doesn't have a pre-programmed answer or requires additional information, it can access external resources such as Wikipedia. 
            - ELARA uses the Wikipedia API to retrieve summary data from articles based on the user's query. If the query results in a disambiguation (e.g., multiple topics with the same name), ELARA will present options to the user for further clarification (Note: this feature is in development and don't work yet).

        6. **Real-Time Interactivity**:
            - As ELARA processes the query, it interacts with the user in real-time. The interface updates dynamically with the latest response using the chat window.
            - If the query requires a restart (for example, reloading Pyodide or resetting the system), ELARA can initiate a restart process to refresh itself.

        **In Summary**:
        - ELARA combines Python execution in the browser via Pyodide, natural language processing, and access to external APIs like Wikipedia to provide intelligent, interactive responses. It adapts based on the user's queries and can perform complex tasks by executing Python code directly within the browser environment."""
    elif re.search(r"\b(clear)\b", q):
        return "__clear__"
    else:
        return "__wikipedia__"