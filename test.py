import RedBlackTree as RBT

temp = RBT.RedBlackTree()
temp.put(4, "Am")
temp.put(1, "Hello")
temp.put(2, "World")
temp.put(3, "I")
temp.put(5, "Your")
temp.put(6, "Creator")

print(temp.get(1) + " " + temp.get(2) + ", " + temp.get(3) + " " + temp.get(4) + " " + temp.get(5) + " " + temp.get(6) + ".")