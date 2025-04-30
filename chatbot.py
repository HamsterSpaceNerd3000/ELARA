import math

def answer(q):
    q = q.lower()
    
    if "hello" in q or "hi" in q:
        return "Hey there!"
    elif "your name" in q:
        return "I'm a Python-powered chatbot!"
    elif "add" in q or "plus" in q:
        return str(eval(q.replace("plus", "+")))
    elif any(op in q for op in ["+", "-", "*", "/", "**"]):
        try:
            return str(eval(q))
        except:
            return "I couldn't do that math."
    else:
        return "__wikipedia__"  # Let JavaScript handle it
