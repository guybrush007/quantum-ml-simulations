from entanglement_witnesses import witnesses
from simulation_utils import *
import pytest
import numpy as np

non_entropy_witnesses = {k: v for k, v in witnesses.items() if not k == 'ENTROPY'}

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_bell_state_pure_state_dm(witness):
    state = create_random_bell_psi()
    is_entangled = witness(state)
    assert is_entangled == True

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_not_entangled_pure_state_dm(witness):
    state = create_random_separable()
    is_entangled = witness(state)
    assert is_entangled == False

@pytest.mark.parametrize("witness", non_entropy_witnesses.values())
def test_is_entangled_not_entangled_mixture_separable(witness):
    state = create_mixed_not_entangled_state()
    is_entangled = witness(state)
    assert is_entangled == False

@pytest.mark.parametrize("witness", non_entropy_witnesses.values())
def test_is_entangled_not_entangled_werner(witness):
    state = create_not_entangled_werner_state_dm()
    is_entangled = witness(state)
    assert is_entangled == False

@pytest.mark.parametrize("witness", non_entropy_witnesses.values())
def test_is_not_entangled_entangled_werner_state_dm(witness):
    state = create_not_entangled_werner_state_dm()
    is_entangled = witness(state)
    assert is_entangled == False

@pytest.mark.parametrize("witness", witnesses.values())
def test_is_entangled_entangled_werner_with_chsh_violation(witness):
    state = create_entangled_werner_state_with_chsh_violation_dm()
    is_entangled = witness(state)
    assert is_entangled == True

chsh_witnesses_keys = ['CHSH', 'CHSH_OPTIMAL']
non_chsh_witnesses = {k: v for k, v in witnesses.items() if k not in chsh_witnesses_keys}
chsh_witnesses = {k: v for k, v in witnesses.items() if k in chsh_witnesses_keys}

@pytest.mark.parametrize("witness", non_chsh_witnesses.values())
def test_is_entangled_entangled_werner_without_chsh_violation(witness):
    state = create_entangled_werner_state_without_chsh_violation_dm()
    is_entangled = witness(state)
    assert is_entangled == True

@pytest.mark.parametrize("witness", chsh_witnesses.values())
def test_is_entangled_not_entangled_werner_without_chsh_violation(witness):
    state = create_entangled_werner_state_without_chsh_violation_dm()
    is_entangled = witness(state)
    assert is_entangled == False