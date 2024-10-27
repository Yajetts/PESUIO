# PESUIO Assignment-1
## PDF Based RAG system
## Objective-1

Create and evaluate a RAG (Retrieval-Augmented Generation) systema using LlamaIndex for PDF documents.

## PDF Selection Rationale
For the PDF Based RAG system, a 114 page PDF text document is used as the knowledge base.

## Implementation Details 
RAG implemented using:    
    
    - LlamaIndex (orchestration)
    - Groq (LLM provider)
    - Qdrant (vector store)
    - Jina (embeddings)


Groq Models used for comparision: 
    
    - llama-3-1-70b-versatile 
    - mixtral-8x7b-32768
    - gemma-7b-it 

## Questions and Responses for 'mixtral-8x7b-32768' model:

1.Enter your question (or 'quit' to exit): What is the primary difference between a discrete emission line spectrum and an absorption line spectrum?

Answer: A discrete emission line spectrum consists of bright, distinct lines against a mostly dark background. These lines correspond to specific wavelengths of light that are emitted when electrons in atoms transition to lower energy levels. On the other hand, an absorption line spectrum features a continuous spectrum with dark, discrete lines. These lines occur when light of specific wavelengths is absorbed by atoms, causing electrons to transition to higher energy levels. In summary, the primary difference between the two spectra lies in the presence or absence of light at specific wavelengths. Emission line spectra have light at specific wavelengths, while absorption line spectra have darkness at those same wavelengths within a continuous spectrum.


2.Enter your question (or 'quit' to exit): what is the Compton shift and how does it depend on the scattering angle?

Answer: The Compton shift is the difference in wavelength before and after an interaction, denoted as χᑎ - χᑐ. It represents the change in the wavelength of the photon due to its collision with a particle, such as an electron. The shift is independent of the incident wavelength and solely depends on the scattering angle. As the scattering angle increases, the Compton shift also increases. This phenomenon is significant in the field of engineering physics and is widely utilized in various applications.


3.Enter your question (or 'quit' to exit): Why can't electrons exist within the nucleus?

Answer: The uncertainty principle states that there is a fundamental limit to the precision with which certain pairs of physical properties, such as position and momentum, can be simultaneously known. If an electron were to exist within the nucleus, it would be confined to a very small space, leading to a large uncertainty in its position. This, in turn, would result in a significant uncertainty in the electron's momentum, which cannot be smaller than this uncertainty in momentum.

If we make a non-relativistic estimation for the energy of the electron based on this minimum momentum, we find that it is approximately 96 MeV. This is significantly higher than the energies of electrons typically observed in radioactive beta decay, which are on the order of 8 MeV. Relativistic calculations yield even higher energies for an electron confined within the nucleus.

Therefore, it is not possible for electrons to exist within the nucleus, as their energy would be much higher than what is typically observed.


4.Enter your question (or 'quit' to exit): What does de Broglie’s hypothesis suggest about the wave nature of moving matter?

Answer: De Broglie's hypothesis proposes that moving matter should exhibit wave characteristics. This means that particles, just like waves, have a wavelength associated with them. The wavelength is given by the formula 𝝀=𝒉/𝒑, where p is the momentum of the particle. However, the wavelengths of macro particles are extremely small to be measured, while the wavelengths of moving subatomic particles   
 can be in the measurable range (~10-10 m).

 5.How does the wave function Ψ(��,��,��,��)Ψ(x,y,z,t) describe the state of a system in motion?

Answer: The wave function Ψ(x,y,z,t)Ψ(x,y,z,t) contains all the possible information about the system, representing its state in motion. It accounts for the wave-like properties of a particle, and its periodic variation corresponds to the probability of finding the particle in a particular region of space at a specific time. Moreover, when this wave function satisfies all the required conditions, it becomes a state function, providing detailed information about the state of the system.



## Questions and Responses for 'llama-3-1-70b-versatile' model:

1. Enter your question (or 'quit' to exit): What is the primary difference between a discrete emission line spectrum and an absorption line spectrum?

Answer: The primary difference between a discrete emission line spectrum and an absorption line spectrum is that a discrete emission line spectrum consists of discrete lines that are emitted, whereas an absorption line spectrum consists of discrete lines that are absent, having been absorbed from a continuous spectrum.

2. Enter your question (or 'quit' to exit):  What is the Compton shift and how does it depend on the scattering angle?

Answer: The Compton shift is the difference between the modified and unmodified wavelength components, denoted as λf - λi. It is also represented as Δλ. The Compton shift increases with the increasing scattering angle θ, and it depends only on the angle of scattering, not on the incident wavelength

3.Why can't electrons exist within the nucleus?

Answer: Electrons cannot exist within the nucleus because, if confined to the diameter of the nucleus, the uncertainty principle would imply a minimum momentum, and consequently, a very high energy, roughly estimated to be more than 20 MeV, from relativistic calculations, and approximately 96 MeV from a non-relativistic estimation. This is contradictory to the energies observed in radioactive β decay where electrons are emitted from the nucleus with energies of the order of 8 MeV.

4.What does de Broglie’s hypothesis suggest about the wave nature of moving matter?

Answer: De Broglie’s hypothesis suggests that moving matter should exhibit wave characteristics and that the wavelength of the associated waves (λ) is equal to Planck's constant (h) divided by the momentum (p) of the particle.

5.How does the wave function Ψ(x,y,z,t) describe the state of a system in motion?               

Answer: The wave function Ψ(x,y,z,t) contains all the possible information about the system. It represents the state of a system in motion, accounting for the wave-like properties of a particle

## Questions and Responses for 'gemma-7b-it' model:

1.What is the primary difference between a discrete emission line spectrum and an absorption line spectrum?

Answer: The primary difference between a discrete emission line spectrum and an absorption line spectrum is the presence of discrete lines in the emission spectrum and their absence in the absorption spectrum.

2.What is the Compton shift and how does it depend on the scattering angle?

Answer: The Compton shift is the difference between the wavelengths of scattered and unscattered photons, indicating an enhancement in wavelength. It increases with the increasing scattering angle.

3.Why can't electrons exist within the nucleus?

Answer: The provided text suggests that the high energy and confinement of electrons within the nucleus violate the principles of quantum mechanics, leading to an uncertainty in their momentum that cannot be reconciled with their presence within the nucleus.

4.What does de Broglie’s hypothesis suggest about the wave nature of moving matter?

Answer: According to de Broglie's hypothesis, moving matter exhibits wave characteristics. The hypothesis suggests that every moving particle, regardless of its size or mass, possesses wave-like properties.

5.How does the wave function Ψ(x,y,z,t) describe the state of a system in motion?

Answer: The provided text suggests that the wave function Ψ(x,y,z,t) contains all the possible information about the state of a system in motion.


## Model Comparision Results:

 As we can see from the question-response sets mixtral-8x7b-32768 is the most accurate and well performing model as it provides detailed answers to the questions using simple language that is easily understable and clear. 

 The llama-3-1-70b-versatile model can provide good answers as well but with brief explanation that can be helpful for a quick brush-up of the topic, which in this case are physics concepts, for a person that already has a good level of knowledge of these topics.

 gemma-7b-it is the most under performing model out of the three, giving one-line. short answers with little explanation. Some of the answers are also deviating from the context of the question asked.

 ## Challenges and Solutions 

#Some challenges that may arise while utilising this model

1. Inaccurate answers 
2. Time-taking responses
3. Inability to generate an answer

#Solutions to these example challenges: 

1. Use a larger dataset as the models knowledge base
2. Make the model more efiicient by using the latest clouds and libraries
3. Check the program for bugs or mistakes and fix them, try using laternate coding syntax to see if it can bring a change.



# PESUIO Assignment-1
## Website Based RAG system
## Objective-2

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
