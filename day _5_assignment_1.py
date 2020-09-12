list1=[1,1,5];
list2=[1,5,6,4,1,2,3,5];
list3=[1,8,6,7,1,2,3.6];
print(list1);
print(list2);
print(list3);
set1=set(list1);
set2=set(list2);
set3=set(list3);
is_subset=set1.issubset(set2);
if(is_subset==1):
    print("it\'s a match");
else:
    print("it\'s gone");
is_subset1=set1.issubset(set3);
if(is_subset1==1):
     print("it\'s a match");
else:
     print("it\'s gone");
    
