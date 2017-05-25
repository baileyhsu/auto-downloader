# Arxiv.org Computational Physics Paper Autodownloader
This app automates the tedious downloading process from the ArXiv.org.



## Background 
We study the quantum dynamics of a nonrelativistic neutral particle with spin in inhomogeneous external magnetic fields. We first consider fields with one-dimensional inhomogeneities, both unphysical and physical, and construct the corresponding analytic propagators. We then consider fields with two-dimensional inhomogeneities and develop an appropriate numerical propagation method. We propagate initial states exhibiting different degrees of space localization and various initial spin configurations, including both pure and mixed spin states. We study the evolution of their spin densities and identify characteristic features of spin density dynamics, such as the spatial separation of spin components, and spin localization or accumulation. We compare our approach and our results with the coverage of the Stern-Gerlach effect in the literature, and we focus on nonstandard Stern-Gerlach outcomes, such as radial separation, spin focusing, spin oscillation, and spin flipping.I

## Simulation
In two matlab files, I simulate the Stern-Gerlach effect with or without a simple harmonic oscillator potential imposed on the device. In the code, we use propogator method from quantum mechanics and the Trotter's formula (as this involves noncommutativity of the Pauli matrices in spin space) to evolve the wave function.


## System Requirement
You can run this file on Mathematica 9.0 or higher on either PC or Mac with at least 2GB of RAM.


## Publication
- ["Stern-Gerlach dynamics with quantum propagators"](http://journals.aps.org/pra/abstract/10.1103/PhysRevA.83.012109) - *Bailey Hsu, Manuel Berrondo, and Jean-Francois S Van Huele*
