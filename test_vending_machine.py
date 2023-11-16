from vending_machine import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    vending =  VendingMachine()
    
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())
    
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    
    vending.event = 'toonie'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200
    vending.event = 'toonie'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 400
    
    
    vending.event = 'chips' 
    vending.update()
    assert vending.state.name == 'count_change'
    assert vending.change_due == 250
    assert vending.coin_values == [200, 100, 25, 10, 5]
    
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    vending.event = 'loonie'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 100
    vending.event = 'RETURN'
    vending.update()
    assert vending.state.name == 'count_change'
    assert vending.change_due == 100
    
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    vending.event = 'loonie'
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 100
    vending.event = 'beer'
    vending.update()
    assert vending.state.name == 'count_change'
    assert vending.state.name == 'waiting'
    
