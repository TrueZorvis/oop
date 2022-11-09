class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, obj, *args, **kwargs):
        self.next_layer = obj
        return obj


class Input(Layer):
    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        curr_obj = self.obj
        while curr_obj:
            yield curr_obj
            curr_obj = curr_obj.next_layer


first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)
print('end')
