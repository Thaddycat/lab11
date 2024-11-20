from mindmap_leaf import MindMapLeaf

leaf0 = MindMapLeaf("node", "circle")
leaf1= MindMapLeaf("node", "oval")
leaf2= MindMapLeaf("node", "square")
leaf3= MindMapLeaf("node", "cloud")
leaf4= MindMapLeaf("node", "hexagon")
leaf5= MindMapLeaf("node", "bang")
leaves = [leaf0,leaf2,leaf1,leaf4,leaf5,leaf3]
for l in leaves:
    print(str(l))
    l.display(3)

leaf = MindMapLeaf("Jean-Luc Picard", "circle")
print(str(leaf))  # Should display "((Jean-Luc Picard))"
leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces

print("MindMapLeaf tests completed!")