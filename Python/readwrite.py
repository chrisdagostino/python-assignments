# reads name.txt into a variable my_name"

with open('output/name.txt') as f:
    my_name = f.read()

# writes a new file named output/hello.txt

with open('output/hello.txt', 'w') as f:
    f.write('hello, my name is ' + my_name)
    f.write('\n')