import numpy as np
from qutip import tensor, basis, rand_ket, qeye

phi_plus = (tensor(basis(2, 0), basis(2, 0)) + tensor(basis(2, 1), basis(2, 1)))/np.sqrt(2)
phi_plus = phi_plus * phi_plus.dag()

phi_minus= (tensor(basis(2, 0), basis(2, 0)) - tensor(basis(2, 1), basis(2, 1)))/np.sqrt(2)
phi_minus = phi_minus * phi_minus.dag()

psi_plus = (tensor(basis(2, 0), basis(2, 1)) + tensor(basis(2, 1), basis(2, 0)))/np.sqrt(2)
psi_plus = psi_plus * psi_plus.dag()

psi_minus= (tensor(basis(2, 0), basis(2, 1)) - tensor(basis(2, 1), basis(2, 0)))/np.sqrt(2)
psi_minus = psi_minus * psi_minus.dag()

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
    state_dm = state * state.dag()
    return state_dm

def create_bell_states():
    return [phi_plus, phi_minus, psi_plus, psi_minus]

def create_random_separable():
    state = tensor(rand_ket(2), rand_ket(2)).unit()
    state_dm = state * state.dag()
    return state_dm

def create_mixed_not_entangled_state():
    not_entangled_1 = tensor(rand_ket(2), rand_ket(2)).unit()
    not_entangled_2 = tensor(rand_ket(2), rand_ket(2)).unit()
    p = np.random.rand()
    return (p * not_entangled_1 * not_entangled_1.dag() + (1-p) * not_entangled_2 * not_entangled_2.dag())

def create_entangled_werner_state_without_chsh_violation():
    p = np.random.uniform(1/3, 1/np.sqrt(2))
    return p * psi_minus * psi_minus.dag() + (1.0-p) * qeye(dimensions=[[2, 2]]) / 4.0

def create_entangled_werner_state_with_chsh_violation():
    p = np.random.uniform(1/np.sqrt(2), 1)
    return p * psi_minus * psi_minus.dag() + (1.0-p) * qeye(dimensions=[[2, 2]]) / 4.0

def create_not_entangled_werner_state_dm():
    p = np.random.rand() / 3
    return p * psi_minus * psi_minus.dag() + (1-p) * qeye(dimensions=[[2, 2]]) / 4

def flatten_density_matrix(state):
    return np.concatenate([np.real(state.full()).flatten(), np.imag(state.full()).flatten()])

def get_simulation_methods_for_witness(witness_name):
    if witness_name in ['NEGATIVITY', 'PPT', 'CONCURRENCE']:
        return [
            create_random_bell_phi,
            create_random_bell_psi,
            create_random_separable,
            create_mixed_not_entangled_state,
            create_entangled_werner_state_without_chsh_violation,
            create_entangled_werner_state_with_chsh_violation,
            create_not_entangled_werner_state_dm
        ]
    elif witness_name in ['CHSH', 'CHSH_OPTIMAL']:
        return [
            create_random_bell_phi,
            create_random_bell_psi,
            create_random_separable,
            create_mixed_not_entangled_state,
            create_entangled_werner_state_with_chsh_violation,
            create_not_entangled_werner_state_dm
        ]
    elif witness_name in ['ENTROPY']:
         return [
            create_random_bell_phi,
            create_random_bell_psi,
            create_random_separable
         ]
    else:
        raise RuntimeError(f"Unknown witness {witness_name}")