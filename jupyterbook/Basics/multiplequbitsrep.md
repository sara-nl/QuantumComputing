# Multiple qubits systems

Lets now consider a system of many qubits. Lets start with a system of two qubits (for example the two electorn in a hydrogen atom).

Each qubit can be in either the ground (state 0)  or excited ( state 1) state. Classically the electrons are therefor in one of the following composed states: 00, 01, 10, or 11. Hpwever, due to the superposition principle, the
quantum state of the two electrons can be any linear combination of these four classical states:

$
$

As with one qubit, even though there are two complex numbers needed to describe the system and we can only measure one, here there are four complex numbers and we just get two.
\

Modifying a quantum state means modifiying the probability amplitudes that describe it, e.g. the entries in the vector [𝛼,𝛽,𝛾,𝛿]𝑇

that corrspond to a 2-qubit system:

|𝜓⟩=𝛼|00⟩+𝛽|01⟩+𝛾|10⟩+𝛿|11⟩

Measurments are a type of operation that do this. They "turn" all probability amplitudes to zero, except for one, which will have a value of 1.0 (basically they project the quantum state into one of the basis states). There are however many other operations that can modify the entries of such a vector and therefore of the quantum state of an n-qubit system. These operations (called quantum gates) can be used to manipulate the quantum state into a given outcome, we can use them to solve a problem. A quantum algorithm is just a sequence of gates with a given prupose.

A quantum gate can be represented as 2𝑛×2𝑛
unitary matrix (n - the number of qubits in the system). The application of quantum gates to qubits corresponds to the multiplication of the n-qubit quantum state vector with the quantum gate matrix and results in a modification of the 2𝑛

quantum state vector.

Some gates are comparable to classical gates. For example, the classical NOT gate can be compared to the quantum X gate. In classical computing, the NOT-gate converts a 0 into a 1 and a 1 into a 0. The quantum X-gate swaps the probability amplitudes of both states and converts |𝜓⟩=𝛼|0⟩+𝛽|1⟩
into |𝜓⟩=𝛽|1⟩+𝛼|0⟩

, which basically means the probability of measuring 0 or 1 is swapped when we apply the X gate. For more examples of quantum gates we refer the reader to this page. For a more indepth knowledge of quantum gates we also recommend paper by (Garcia-Escartin and Chamorro-Posada, 2011). How these gates are physically implemented depends on the type of qubits: superconductors, trapped ions, NV centers, photons, etc.

Most quantum gates act only in a small number of qubits (mostly due to experimental limitations). This is not a limitation as there exist sets of one- and two-qubit quantum gates which are universal for quantum computation: any operation possible on a quantum computer can be reduced to this set of gates. 
