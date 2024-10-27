# PESUIO Assignment-1
## PDF Based RAG system
## Objective

Create and evaluate a RAG (Retrieval-Augmented Generation) systema using LlamaIndex for Website based content.

## Website Selection Rationale
For the Website Based RAG system, a url link from GeekforGeeks.com is used.

## Implementation Details 
RAG implemented using llamaIndex and llama-3.1-70b-versatile Groq Cloud LLM model.


##Questions and Responses:

1.What is OOPs in python?

Answer: Python fully supports object-oriented programming (OOP) concepts. Classes, objects, inheritance, encapsulation, and polymorphism are fundamental features of Python.

2.What is a python Class?

Answer: A Python class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.

3. What are python Object and what are they used for?

Answer: Objects in Python are instances of classes, which represent real-world entities or concepts. They are used to hold and manipulate data in a program. Objects have attributes, which are data members that describe the object, and methods, which are functions that perform actions on the object. They are used to organize code, promote modularity, and facilitate code reuse.

4. How do i create a Class in python? 

Answer: A class in Python is created using the 'class' keyword, followed by the name of the class. For example, to create a class named 'Dog', the syntax would be:   

class Dog:

5. Can you give another example?

Answer: Unfortunately, I don't have enough information to provide another example. The context provided seems to be a list of tutorials and programming concepts related to Python and Java, but it doesn't contain a specific example that I can expand on. Could you please provide more context or clarify what you would like another example of?

6. What is Python inheritance, and what are its types?            

Answer: Python inheritance refers to the ability of one class to inherit properties from another class. There are four main types of inheritance in Python:

1. Single Inheritance, which enables a derived class to inherit characteristics from a single-parent class.
2. Multilevel Inheritance, which enables a derived class to inherit properties from an immediate parent class that in turn inherits properties from its parent class. 
3. Hierarchical Inheritance, which enables more than one derived class to inherit properties from a parent class.
4. Multiple Inheritance, which enables one derived class to inherit properties from more than one base class.




## Performance Analysis 

From the above question-response set it can be assesed that the answers are simple and to the point. The model will only provide a detailed explanation if the query is asking for it. It can also be seen that the model cannot provide information on topics that are not listed in the given webpage and can only generate responses for information that is available to it.


## Problems and Solutions 


#Some issues that can possibly be encountered in this RAG system:

1. Incorrect answers
2. Limited knowledge
3. Low efficiency

#Solutions

1. Making sure the information provided to that model is correct and is from a trusted source.
2. To expand the models knowledge we need to give it more data to work with so it can generate responsed for a larger variety of questions.
3. Using up to date code and libraries that are relevant to the present day needs of the users.
