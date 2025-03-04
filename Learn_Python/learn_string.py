#A string is a sequence of characters
name="Diya"
print(name)
name='Vibin'
print(name)
print("Diya 'Vibin' ")
print('"Diya" Vibin')
print("Hello!\"I am Diya\".How's your bf?")
statement=""" heyy 
hello!!!!
how's it going?
hope u r fine..."""
print(statement)
temp_statement="hello!\nhii?\nlove you."
print(temp_statement)
#access
st="hello"
print(st[0])
print(st[4])
print(st[-4])
print(st[-5])
#slicing
print(st[1:4])
print(st[-5:-1])
print(st[-5:-2])
print(st[:4])
print(st[2:])
#string operators
#concatenate
first_name="Diya"
second_name="Santhosh"
name=first_name+second_name
print(name)
print("name:",first_name+second_name)
print("name:",first_name,"",second_name)
#repeat
print(5*'DE')
print("ab"*3)
print(0*"bb")#empty
print(-3*"hi")#empty
#comparison
#comparisons are case sensitive
print("Hello"=="Hello")
print("hello"=='Hello')
print("hello"!='Hello')
print("hello"<'Hello')
print("Hello"<='hello')
print("hello">'Hello')
#in
print("hello" not in "helloworld")
print("world"  in "helloworld")
print("hii" not in "helloworld")
#escape
print("Hello!\"I am Diya\".How's your bf?")
print("Hello!\n \"I am Diy\141\".How's your b\x66?")
#formatting
age=28
print("my age is %d"%(age))
print("my age is ",age)
#slicing
name="I'm DiyaSanthosh"
print(name[0:8])
print(name[0:8:2])
s=5*"abc"
print(s[::3])
print(s[1::3])
print(s[:5:3])
#reversing
print(name[8:1:-2])
print(name[15:0:-1])
print(name[::-1])
#formatting
name="Diya"
print("my name is %s"%name )
print("my age is %d"%age)
print("my name is %s age is %d"%(name,age))
print("my name is {} age is {}".format(name,age))
print("my age is {1} name is {0}".format(name,age))
a="diya"
b="attingal"
print("my name is {name} place is {place}".format(name=a,place=b))
print("I got {0:f}% mark in maths".format(80))
print("I got {0:.2f}% mark in maths".format(80))
print(f"my name is {name} age is {age}")
print(f"my name is {name.upper()} age is {age}")
intro=f"my name is {a.upper()} "\
      f"age is {age} "\
    f"place is {b.capitalize()}"
print(intro)
x=9
y=10
print(f"""result :{x+y}""")