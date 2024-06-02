import numpy as np
from qutip import tensor, basis, rand_ket

def create_random_bell_phi():
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    state = (np.cos(theta) * tensor(basis(2, 0), basis(2, 0)) +
                 np.exp(1j * phi) * np.sin(theta) * tensor(basis(2, 1), basis(2, 1)))
    state_dm = state * state.dag()
    return state_dm

def create_random_bell_psi():
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    state = (np.cos(theta) * tensor(basis(2, 0), basis(2, 1)) +
                 np.exp(1j * phi) * np.sin(theta) * tensor(basis(2, 1), basis(2, 0)))
    state = state * state.dag()
    state_dm = state * state.dag()
    return state_dm

def create_random_separable():
    state = tensor(rand_ket(2), rand_ket(2)).unit()
    state_dm = state * state.dag()
    return state_dm

def flatten_density_matrix(state):
    return np.concatenate([np.real(state.full()).flatten(), np.imag(state.full()).flatten()])