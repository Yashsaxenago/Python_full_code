# set is a collection of well defined objects :
# it means same name value repaet na ho and it doesn't follow the order

s={2,3,2,4}
print(s)

info={"yash",12,0.12,"saaxena"}
print(info)

yash={} # its a empty dict not set
print(type(yash))

# to create empty set

yash=set()
print(type(yash))

l1={1,2,3,4}
l2={2,3,4,5,6,7}
print(l1.union(l2))
print(l1,l2)
