from django.shortcuts import render
from django.http import HttpResponse


def chatbot_home(request):
    return render(request, 'index.html')


def get_response(request):
    user_input = (request.GET.get('msg') or '').strip()
    if not user_input:
        return HttpResponse('Please send a message.')

    uq = user_input.lower()
    
    # Simple rule-based Q&A - General AI Assistant Chatbot
    responses = {
        # Greetings
        'hello': 'Hello! I\'m an AI Assistant here to help you. What can I do for you?',
        'hi': 'Hi! I\'m your AI assistant. Ask me anything!',
        'hey': 'Hey there! How can I help you today?',
        'greetings': 'Greetings! Welcome. How may I assist you?',
        
        # Thanks
        'thanks': 'You\'re welcome! Happy to help. Anything else?',
        'thank': 'My pleasure! Feel free to ask more questions.',
        'appreciate': 'I appreciate that! Is there anything else I can assist with?',
        
        # Goodbye
        'bye': 'Goodbye! Have a great day!',
        'goodbye': 'See you later! Take care!',
        'exit': 'Thank you for chatting. Goodbye!',
        'quit': 'Bye! Come back anytime!',
        
        # Identity
        'name': 'I\'m an AI Assistant Chatbot, here to provide helpful information and assist you with various topics.',
        'who are you': 'I\'m an AI Assistant designed to help answer questions and have helpful conversations.',
        'what are you': 'I\'m an AI Assistant Chatbot that can help you with information, advice, and problem-solving.',
        
        # Help & General
        'help': 'I can assist with a wide range of topics including technology, general knowledge, problem-solving, and more. What\'s on your mind?',
        'what can': 'I can help with questions about technology, science, history, writing, coding, and much more!',
        'capabilities': 'I can answer questions, provide information, discuss ideas, help with coding, explain concepts, and have conversations.',
        
        # General Knowledge
        'world': 'The world is full of amazing places, cultures, and people. Is there something specific you\'d like to know?',
        'life': 'Life is a journey of learning and growth. Is there something specific I can help you with?',
        'tell me': 'I\'d be happy to tell you about something! What topic interests you?',
        'how': 'I can explain how many things work! What would you like to understand?',
        'why': 'Great question! Feel free to ask why about anything specific.',
        'what': 'I\'m here to answer what questions you have. Ask away!',
        
        # Technology & Science
        'technology': 'Technology is constantly evolving! Ask about AI, software, hardware, or any tech topic.',
        'science': 'Science is fascinating! I can discuss physics, chemistry, biology, astronomy, and more.',
        'artificial intelligence': 'AI is transforming the world. I can explain machine learning, neural networks, and how AI works.',
        'computer': 'Computers are powerful tools. Ask about hardware, software, networking, or cybersecurity.',
        'internet': 'The internet connects billions of devices. It uses protocols, servers, and networks to transfer data.',
        'data': 'Data is valuable information. It\'s collected, processed, analyzed, and used to make decisions.',
        
        # Education & Learning
        'learn': 'Learning is a lifelong journey! Start with curiosity, ask questions, and practice consistently.',
        'study': 'Effective studying: take notes, practice problems, teach others, and review regularly.',
        'education': 'Education opens doors. Never stop learning and exploring new topics!',
        'book': 'Books are wonderful sources of knowledge! Recommend some based on your interests.',
        'school': 'School provides foundation knowledge. Learning continues throughout life in many forms.',
        'university': 'University offers advanced education and specialization in various fields.',
        
        # Math & Logic
        'math': 'Math is the language of the universe! Ask about algebra, geometry, calculus, or statistics.',
        'calculate': 'I can help with calculations and math problems. What would you like to solve?',
        'logic': 'Logic helps us think clearly and solve problems systematically.',
        'number': 'Numbers are fundamental. They represent quantity, position, measurement, and more.',
        
        # History & Culture
        'history': 'History teaches us about the past to understand the present. What era interests you?',
        'culture': 'Culture encompasses art, music, traditions, values, and ways of life of different groups.',
        'country': 'Every country has unique history, culture, and characteristics. Which interests you?',
        'language': 'Languages are fascinating ways people communicate. There are thousands worldwide!',
        
        # Writing & Communication
        'write': 'Good writing requires clarity, organization, and revision. Practice daily for improvement.',
        'story': 'Stories captivate us with characters, plots, and emotions. Would you like to discuss a story?',
        'poem': 'Poetry expresses emotions and ideas in creative ways using rhythm, rhyme, and imagery.',
        'article': 'Articles inform readers on specific topics. They follow structure: intro, body, conclusion.',
        'speech': 'Great speeches inspire and persuade. They use clear language, emotion, and powerful ideas.',
        
        # Business & Economics
        'business': 'Business involves creating value, managing resources, and serving customers profitably.',
        'money': 'Money is a medium of exchange. Economics studies how resources are produced and distributed.',
        'job': 'Finding a good job requires skills, networking, and persistence. What field interests you?',
        'career': 'A successful career requires passion, skill development, and continuous learning.',
        'finance': 'Finance involves managing money through budgeting, investing, and financial planning.',
        
        # Art & Creativity
        'art': 'Art expresses creativity and emotion through various mediums like painting, sculpture, music.',
        'music': 'Music brings joy and emotion! Different genres and styles resonate with different people.',
        'creativity': 'Creativity flourishes when you explore ideas freely without fear of judgment.',
        'design': 'Good design balances aesthetics, functionality, and user experience.',
        
        # Entertainment & Hobbies
        'movie': 'Movies are entertaining and can tell powerful stories across many genres.',
        'game': 'Games provide fun, challenge, and social connection. What type of games do you enjoy?',
        'sport': 'Sports promote fitness, teamwork, and competition. What\'s your favorite sport?',
        'hobby': 'Hobbies are enjoyable activities that help you relax and express yourself.',
        
        # Python & Programming
        'python': 'Python is a popular, versatile language. Ask about syntax, libraries, or projects!',
        'code': 'Programming requires logic, patience, and practice. Start with fundamentals and build!',
        'hello world': 'Basic Python hello world: print("Hello, World!") - Just 1 line! Run with: python script.py',
        'print': 'Print function outputs text: print("Hello") or print("Text1", "Text2"). Use print() for new lines.',
        'hello': 'Simple hello world program:\nprint("Hello, World!")\nSave as hello.py and run: python hello.py',
        'print hello': 'print("Hello, World!") - Basic print statement that displays Hello, World! to console.',
        'print world': 'Print world example: print("Welcome to the World!") outputs text to the screen.',
        'print statement': 'Python print statement: print(value) outputs text. Example: print("Hello") prints Hello',
        'print multiple': 'Print multiple lines:\nprint("Line 1")\nprint("Line 2")\nprint("Line 3")',
        'print variable': 'Print variable: name = "Alice"; print(name) outputs Alice. Or: print("Hello", name)',
        'print formatting': 'Print with f-string: name = "Bob"; print(f"Hello {name}") outputs Hello Bob',
        'print string': 'Print string example: message = "Python"; print(message) outputs Python to console.',
        'string output': 'Output strings: print("text") displays text. Use quotes for string literals.',
        'console output': 'Print to console: print("Message") displays output. Can print numbers, strings, variables.',
        'hello program': 'Hello world program:\nprint("Hello, World!")\nThis is the simplest Python program!',
        'simple program': 'Simplest program: print("Hello, World!") - One line displays text to the console.',
        'first program': 'First Python program:\nprint("Hello, World!")\nSave and run: python filename.py',
        'basic print': 'Basic print: print("Hello") outputs Hello. Add multiple arguments: print("A", "B")',
        'print text': 'Print text to screen: print("Your text here") displays the text in the console/terminal.',
        'output text': 'Output text using print(): print("This is text") displays text to standard output.',
        'basic program': 'Basic Python programs: print(), variables, if-else, loops. Start simple and build complexity!',
        'if else': 'If-else statement: if age >= 18: print("Adult") else: print("Minor")',
        'arithmetic': 'Basic arithmetic: a = 10; b = 5; print(a + b) outputs 15. Supports +, -, *, /, //, %, **',
        'input': 'Get user input: name = input("Enter name: ") stores user input in a variable.',
        'for loop': 'For loop example: for i in range(5): print(i) prints 0 through 4.',
        'while loop': 'While loop example: i = 0; while i < 5: print(i); i += 1',
        'list loop': 'Loop through list: my_list = [1,2,3]; for item in my_list: print(item)',
        'addition': 'Simple addition program: a = 10; b = 20; print(a + b) outputs 30',
        'calculator': 'Simple calculator: a = int(input("Number: ")); b = int(input("Number: ")); print(a + b)',
        'even odd': 'Check even/odd: n = int(input()); print("Even" if n % 2 == 0 else "Odd")',
        'factorial': 'Factorial program: n = 5; result = 1; for i in range(1, n+1): result *= i; print(result)',
        'fibonacci': 'Fibonacci: a, b = 0, 1; for _ in range(5): print(a); a, b = b, a+b',
        'function': 'Define functions: def greet(name): print(f"Hello {name}") then call greet("John")',
        'loop': 'Loops repeat actions: for loops iterate through collections, while loops run while condition is true.',
        'import': 'Import libraries: import numpy or from django import forms.',
        'pip': 'Install packages: pip install package_name. Update: pip install --upgrade package_name.',
        'variable': 'Variables store data: name = "John", age = 30. Python infers types automatically.',
        'list': 'Lists hold multiple items: my_list = [1, 2, 3]. Access with indexing, modify with methods.',
        'dictionary': 'Dicts store key-value pairs: person = {"name": "John", "age": 30}.',
        'string': 'Strings are text: "hello" or \'world\'. Combine with +, format with f-strings.',
        'django': 'Django is a Python web framework for building web applications quickly.',
        'venv': 'Virtual environment: python -m venv .venv, then activate for isolated packages.',
        'class': 'Classes define objects with attributes and methods. Use for organizing code.',
        'error': 'Errors are learning opportunities! Read error messages carefully to understand issues.',
        'debug': 'Debugging: use print statements, debuggers, or log files to trace issues.',
        
        # Web Development
        'web': 'Web development involves frontend (HTML, CSS, JS) and backend (servers, databases).',
        'html': 'HTML structures web pages with tags like <div>, <p>, <a>, <img>.',
        'css': 'CSS styles web pages with colors, fonts, layouts, and responsive design.',
        'javascript': 'JavaScript adds interactivity to web pages and can run on servers too.',
        'database': 'Databases store and manage data. SQL is common for relational databases.',
        'api': 'APIs allow applications to communicate and share data.',
        
        # Problem Solving
        'problem': 'To solve problems: understand the issue, break it down, brainstorm solutions, test.',
        'solution': 'Finding solutions requires creative thinking, research, and persistence.',
        'advice': 'I\'m happy to provide advice! Share more details about your situation.',
        'opinion': 'I can share perspectives on many topics, but encourage you to think critically too.',
        
        # Math & Logic
        'algorithm': 'Algorithms are step-by-step procedures to solve problems or complete tasks.',
        'optimize': 'Optimization improves efficiency. Consider time complexity, memory, and performance.',
        'security': 'Security protects data and systems from unauthorized access and attacks.',
    }
    
    # Check for keyword matches (prioritize longer matches)
    matched_response = None
    matched_length = 0
    
    for keyword, response in responses.items():
        if keyword in uq and len(keyword) > matched_length:
            matched_response = response
            matched_length = len(keyword)
    
    if matched_response:
        return HttpResponse(matched_response)
    
    # Default fallback response
    default = 'That\'s an interesting question! I\'m learning more about many topics. Try asking me about technology, programming, science, or general knowledge!'
    return HttpResponse(default)

