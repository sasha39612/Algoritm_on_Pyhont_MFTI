import Lecture_6_practice_coding_MFTI_library as lib
#from Лекция_6_МФТИ_library import foo

def printer():
    print(x)

def modifier():
    global x
    x += 10
    print(x)


print('Main module', __name__)

lib.foo(3)
lib.foo(4)
x = lib.bar(1, 5)
print(x)

lib.create_object("Круг1")
lib.create_object("Круг2")
lib.create_object("Круг3")
lib.print_objects()

for obj in lib.objects:
    if("Круг1") in obj:
        print("Найден круг 1!")
lib.objects.pop()
lib.print_objects()

print(x)


