from qutip import basis, tensor, sigmax, sigmay, sigmaz, concurrence, entropy_vn, partial_transpose
import numpy as np

def is_entangled_chsh(state, tolerance=1e-10):
    A_1 = sigmaz()
    A_2 = sigmax()
    B_1 = (sigmaz() + sigmax()) / np.sqrt(2)
    B_2 = (sigmaz() - sigmax()) / np.sqrt(2)
    CHSH_ZX = tensor(A_1, B_1) + tensor(A_1, B_2) + tensor(A_2, B_1) - tensor(A_2, B_2)
    
    A_1 = sigmay()
    A_2 = sigmaz()
    B_1 = (sigmay() + sigmaz()) / np.sqrt(2)
    B_2 = (sigmay() - sigmaz()) / np.sqrt(2)
    CHSH_YZ = tensor(A_1, B_1) + tensor(A_1, B_2) + tensor(A_2, B_1) - tensor(A_2, B_2)
    
    A_1 = sigmax()
    A_2 = sigmay()
    B_1 = (sigmax() + sigmay()) / np.sqrt(2)
    B_2 = (sigmax() - sigmay()) / np.sqrt(2)
    CHSH_XY = tensor(A_1, B_1) + tensor(A_1, B_2) + tensor(A_2, B_1) - tensor(A_2, B_2)
    
    chsh_operators ={"CHSH_ZX": CHSH_ZX, "CHSH_YZ": CHSH_YZ, "CHSH_XY": CHSH_XY}

    for chsh_basis, chsh_operator in chsh_operators.items():
        violation = np.abs(state.dag() * chsh_operator * state)
        if violation > (2 + tolerance):
            return True
    return False

def is_entangled_concurrence(state):
    state_dm = state * state.dag() 
    conc = concurrence(state_dm)
    return conc != 0.0

def is_entangled_entropy(state, tolerance=1e-10):
    state_dm = state * state.dag() 
    ptrace = state_dm.ptrace(0) 
    entropy = entropy_vn(ptrace, base=2)
    return entropy > tolerance and entropy <= (1+tolerance)

def is_entangled_negativity(state, tolerance=1e-10):
    state_dm = state * state.dag()
    partial_transposed_state = partial_transpose(state_dm, [0, 1])
    eigenvalues = partial_transposed_state.eigenenergies()
    negativity = sum(abs(e) for e in eigenvalues if e < 0)
    return negativity > tolerance

all_entanglement_witnesses = {
    "CHSH": is_entangled_chsh,
    "CONCURRENCE": is_entangled_concurrence,
    "ENTROPY": is_entangled_entropy,
    "NEGATIVITY": is_entangled_negativity
    }


