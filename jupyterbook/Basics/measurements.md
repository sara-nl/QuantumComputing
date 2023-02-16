# Measurements

Information in a quantum computer is stored in qubits.
A qubit is a two state system with quantum properties:

- superposition
- entanglement
- interference 

As opposed to a bit that can only be in state 0 or 1 (off or on), a qubit can have any value in between (like a dimmy light). A qubit can therefore be described as a combination (superposition) of the "basis states" 0 and 1 

$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$  

where $|\psi\rangle$ (known as state vector) describes the qubit state, $|0\rangle$ and $|1\rangle$ the basis states and the coefficients $\alpha$ and $\beta$ are the contribution of each basis state to the qubit state.
We have used the bra-ket notation $| \rangle$, which is just a way to denote quantum states.

 

Before we measure a qubit there are two possible outcomes: 0 or 1 (the basis states of the measurment), but when the qubit is measured we collapse it into one of this states. For the example above, the probability of measuring one state or the other ($| 0\rangle$ or $|1\rangle$) depends on how they contribute to the total state in the first place: depends on the values of $\alpha$ and $\beta$. The larger the magnitude of these coefficients the more likely it is we measure the associated state. 
The actual probability of measuring state $|0\rangle$ is given by $|\alpha|^2$ and the actual probability of measuring state $|1\rangle$ is given by $|\beta|^2$. Since the total probability of measuring a state has to be 1.0, we also know that $|\alpha|^2 + |\beta|^2 = 1$. 

Given the basis states, a qubit state is fully described by the coefficients  $\alpha$ and $\beta$ (known as probability amplitudes. 

As an example the states $| 0 \rangle$ and $|1 \rangle$
$|0\rangle = \left(\begin{array}{c} 1 \\ 0 \end{array}\right)$

$|1\rangle = \left(\begin{array}{c} 0 \\ 1 \end{array}\right)$

## Bloch sphere

The Bloch sphere helps us visualize a qubit state and its transformations. As we mention before, if the basis states are known, the state of a qubit is fully defined by $\alpha$ and $\beta$. In their general form, these coefficients are complex numbers (of the form $a+ ib$). Hence, the state of a qubit if fully described by four number.

Since we square the probability amplitudes to find the probability of measurement, certain qubit states are equivalent to us. Hence, we can ignore the global phase and assumes for example that $\alpha$ is real and non-negative. By doing so, the qubit state is fully defined by three numbers: we can describe the state of a qubit in 3D and visualize it. 

We do so by mapping $\psi$ in term of $\theta, \phi$ as:

$|i\psi\rangle = \cos(\theta/2) |0\rangle + sin(\theta/2)\exp^{i\phi} |1\rangle$

Where $0 \lt \theta \lt \pi, 0 \lt \phi \lt 2\pi$

Under this mapping the state of a qubit is represented as a point in "Bloch sphere" a shpere of radius 1, where the poles represent the "basis states". 


```{figure} ../images/bloch.png
---
scale: 75%
align: center
---
Qubit state respresentation in Bloch sphere. Image taken from https://en.wikipedia.org/wiki/Bloch_sphere
```


