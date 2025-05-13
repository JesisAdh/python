# comparision operator
# x==y for equal 

# value initialization
x=1
y=2

# number comparision
print("The condition for 1==2 is",x==y)  #for equal
print("The condition for 1!=2 is",x!=y)  #for not equal 

# string compariion
a= "abc"
b="xyz"
print("abc == xyz ",a==b)
print("abc != xyz ",a!=b)

c=1.2
d=2.1
print("1.2 == 2.1 ",c==d)
print("1.2 != 2.1 ",c!=d)
print("1.2 >= 2.1 ",c>=d)
print("1.2 <= 2.1 ",c<=d)

# p=int(input("Enter number"))
p=250
q=200
r=300
print(p<5 and q<5 and r<=5)  #comparision of three values using logical opertor (and)
print(p>q and p>r) 
# print(p<q and p<r and r>p)

# using or operator 
print(p>q or p>r) 

x=0
y=1
z=-1
print(x==0 or x>0)
print(x>=0)

print("x>=0 and y>=0 or z<0 s  ",(x>=0 and y>=0)or z<0)

# using not statement
print(not(x>=0))

# using identity operator
print("Using is not, the statement is ",x is not "0" or x>0)


print("Identity operator")
k = [1,2,3,4,5]#001
l = [1,2,3,4,5]#002
print(k==l)
# the location of the vairable is different so th output is false, this only works with tuples or else the value of x anf y is same the result given by ïs is true
l=k #because now the location is same the result is true 
print(k is l)
print(k is not l)


# membership operator in/not in
print("Membership  operator")
x = "hello world"
print("hello" in x) 
print("hello" not in x) 

# assignment operator
x=5
# x+=2
# x%=3
print(x:=10) #to print and initialize the value at once
