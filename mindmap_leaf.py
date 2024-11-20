class MindMapLeaf:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def get_shape_representation(self):
        shapes = {"circle": "(({}))", "oval": "({})", "square": "[{}]", "cloud": "){}(", "hexagon": "{{{{{}}}}}", "bang": ")){}(("}
        return shapes.get(self.shape, "{}")

    def __str__(self):
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        print(" " * indent + str(self))



