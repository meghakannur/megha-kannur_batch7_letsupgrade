lst=['123','xyz','sara','abc','@345'];
print(lst)
## to add some objects to the list
lst.append('abc');
print("list after appending :",lst)
lst.append(586);
print("updated list:",lst)
## to add some list of objects to the previous list
lst1=['camel',900,'12gf'];
lst.extend(lst1);
print("extended list:",lst)
## to insert the object at perticular index
lst.insert(1,786);
lst.insert(4,'code');
print("list with new objects:",lst)
## to remove object from list
lst.remove('abc');
lst.remove(786);
print("list after removing some objects:",lst)
## to know the index value of object in list
print(" index of sara in list:",lst.index('sara'))
print(" index of 900 in list:",lst.index(900))
print("............................................................")
## tuple methods
tuple1=('abc','xyz','sara');
tuple2=(35.93,1000,2);
## to find length of tuple
print("length of tuple1:",len(tuple1))
print("length of tuple2:",len(tuple2))
## to find maximum object in tuple
print("maximum of tuple1:",max(tuple1))
print("maximum of tuple2:",max(tuple2))
## to find minimum object in tuple
print("minimum of tuple1:",min(tuple1))
print("minimum of tuple2:",min(tuple2))
## to convert list into tuple
lst=['$nbx',350,'work']
tuple3=tuple(lst)
print("tuple3 elements:",tuple3)
print("............................................................")
## Some methods on strings
s1="letsupgrade";
s2="batch7";
## to capitalize the first character of string
print("s1 with capitalize:",s1.capitalize())
print("s2 with capitalize:",s2.capitalize())
## to find wether string contains any digits
print("s1 contains any digits or not:",s1.isdigit())
print("s2 contains any digits or not:",s2.isdigit())
## to find all characters in string are lower case or not
print("s1 contains all lower case characters:",s1.islower())
print("s2 contains all lower case characters:",s2.islower())
## to join the sequence of elements as string
s="-";
seq=("x","y","z");
print(" joined sequence",s.join(seq))
## to find length of string
print("length of the s1:",len(s1))
print("length of the s2:",len(s2))
print(".......................................................")
## some methods on dictionary
dict1={'name':'megha','class':10,'age':16}
dict2={'name':'deepa','class':8,'age':14}
## to remove a particular object from dictionary by key
del dict1['name'];
print("after removing name from dict1:",dict1)
## to delete all entries in dictionary and delete entire dictionary
dict1.clear();
del dict1;
## to find length of dictionary
print("length of dict2:",len(dict2))
## to convert dictionary into printable string
print("equivalent string: %s" % str(dict2))
## to find the type of variable we passed
print("variable type: %s" % type(dict2))
print("..............................................")
## methods on sets
my_set1={1,2,3,4}
my_set2={1.0,'happy',(1,4,6),890} ## set of mixed data type
## to find data type
print(type(my_set2))
## add an element to a set
my_set1.add(5)
my_set2.add('abc')
print("updated set:",my_set1,my_set2)
## to add sequence of elements or list to set
my_set1.update([1,2,3,4,5])
print("udpated set1:",my_set1)
my_set2.update([4,5],{8,9,0})
print("updated set2:",my_set2)
## to discard a element from set
my_set1.discard(2)
print("set after removing 2:",my_set1)
## to pop an random element from set
print(my_set1.pop())
## to clear all elements in set
my_set1.clear()
print(my_set1)
## we can perform union and intersection of sets
my_set1={1,2,3,4,5,6}
my_set2={3,4,5,6,7}
print("union of two sets:",my_set1.union(my_set2)) ## or we can use print(my_set1|my_set2)
print("intersection of two sets:",my_set1.intersection(my_set2)) ## or we can use print(my_set1&my_set2)







