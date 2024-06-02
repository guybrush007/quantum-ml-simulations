from entanglement_witnesses import witnesses
import pytest
from qutip import basis, tensor, rand_ket
import numpy as np

def  create_bell_pure_state():
    return (tensor(basis(2, 0), basis(2, 0)) + tensor(basis(2, 1), basis(2, 1)))/np.sqrt(2)

def  create_bell_pure_state_dm():
    pure_state = create_bell_pure_state()
    return pure_state * pure_state.dag()

def create_not_entangled_pure_state():
    return tensor(rand_ket(2), rand_ket(2)).unit()

def create_not_entangled_pure_state_dm():
    pure_state = create_not_entangled_pure_state()
    return pure_state * pure_state.dag()

def create_mixed_bell_state_dm():
    phi_plus = (tensor(basis(2, 0), basis(2, 0)) + tensor(basis(2, 1), basis(2, 1)))/np.sqrt(2)
    phi_minus = (tensor(basis(2, 0), basis(2, 0)) - tensor(basis(2, 1), basis(2, 1)))/np.sqrt(2)
    p = np.random.rand()
    return (p * phi_plus * phi_plus.dag() + (1-p) * phi_minus * phi_minus.dag())

def create_mixed_not_entangled_state_dm():
    not_entangled_1 = tensor(rand_ket(2), rand_ket(2)).unit()
    not_entangled_2 = tensor(rand_ket(2), rand_ket(2)).unit()
    return (0.5 * not_entangled_1 * not_entangled_1.dag() + 0.5 * not_entangled_2 * not_entangled_2.dag())


@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_chsh_bell_state_pure_state(witness):
    state = create_bell_pure_state()
    is_entangled = witness(state)
    assert is_entangled is True

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_chsh_bell_state_pure_state_dm(witness):
    state = create_bell_pure_state_dm()
    is_entangled = witness(state)
    assert is_entangled is True

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_not_entangled_pure_state(witness):
    state = create_not_entangled_pure_state()
    is_entangled = witness(state)
    assert is_entangled is False
    
@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_not_entangled_pure_state_dm(witness):
    state = create_not_entangled_pure_state_dm()
    is_entangled = witness(state)
    assert is_entangled is False

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_bell_states_mixed(witness):
    state = create_mixed_bell_state_dm()
    is_entangled = witness(state)
    assert is_entangled is True 

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_not_entangled_states_mixed(witness):
    state = create_mixed_not_entangled_state_dm()
    is_entangled = witness(state)
    assert is_entangled is False