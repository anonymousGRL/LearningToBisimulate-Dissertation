# Learning to Bisimulate

This repository comprises the full implementation of the algorithms presented in the dissertation **Learning Bisimulation Quotients**. The dissertation submitted in Trinity Term 2023 at the University of Oxford, for the degree **Master of Science in Advanced Computer Science**. 

The notebook contains the implementation of our CEGIS approach for the synthesis of bisimulation quotients, the extraction of subquotients and the extraction of polytopic regions for which the obtained abstractions are exact.

The code is contained in two Jupyter Notebooks. One contains the implementation of all employed algorithms. The second one contains the code used for visualization of dynamical systems and partitions.

We utilize the following external libaries: 

- **Z3Py** - SMT Solver employed in the CEGIS loop: https://github.com/Z3Prover/z3
- **NumPy** - Array and matrix operations: https://github.com/numpy
- **NetworkX** - Visualization of extracted quotients: https://github.com/networkx/networkx
- **MathPlotLib** - Visualizations of synthesized partitions and trajectories: https://github.com/matplotlib/matplotlib
 

