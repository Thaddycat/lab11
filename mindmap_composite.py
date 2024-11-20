import os

class MindMapComposite:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("Child not found in children list.")

    def __str__(self):
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        shapes = {"circle": "(({}))", "oval": "({})", "square": "[{}]", "cloud": "){}(", "hexagon": "{{{{{}}}}}", "bang": ")){}(("}
        return shapes.get(self.shape, "{}")