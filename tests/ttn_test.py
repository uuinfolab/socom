from socom import *

def test_ttnet():
    net = TemporalTextNetwork()
    
    assert num_layers(net._network) == 2
    assert 'M' in layers(net._network)
    assert 'U' in layers(net._network)

    assert num_actors(net._network) == 0
    assert num_edges(net._network) == 0
