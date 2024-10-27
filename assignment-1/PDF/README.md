# PESUIO Assignment-1
## PDF Based RAG system
## Objective

Create and evaluate two RAG (Retrieval-Augmented Generation) systems using LlamaIndex - one for PDF documents and another for website content.

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

# Questions and Responses for 'mixtral-8x7b-32768' model:

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



# Questions and Responses for 'llama-3-1-70b-versatile' model:


