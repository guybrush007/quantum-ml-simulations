#!/bin/bash

papermill 01-Training.ipynb ./executed_notebooks/01-Training-CHSH.ipynb -p WITNESS_NAME "CHSH"
papermill 01-Training.ipynb ./executed_notebooks/01-Training-CONCURRENCE.ipynb -p WITNESS_NAME "CONCURRENCE"
papermill 01-Training.ipynb ./executed_notebooks/01-Training-ENTROPY.ipynb -p WITNESS_NAME "ENTROPY"
papermill 01-Training.ipynb ./executed_notebooks/01-Training-NEGATIVITY.ipynb -p WITNESS_NAME "NEGATIVITY"