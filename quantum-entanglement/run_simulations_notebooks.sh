#!/bin/bash

papermill 00-Simulation.ipynb ./executed_notebooks/00-Simulation-CHSH.ipynb -p WITNESS_NAME "CHSH"
papermill 00-Simulation.ipynb ./executed_notebooks/00-Simulation-CONCURRENCE.ipynb -p WITNESS_NAME "CONCURRENCE"
papermill 00-Simulation.ipynb ./executed_notebooks/00-Simulation-ENTROPY.ipynb -p WITNESS_NAME "ENTROPY"
papermill 00-Simulation.ipynb ./executed_notebooks/00-Simulation-NEGATIVITY.ipynb -p WITNESS_NAME "NEGATIVITY"