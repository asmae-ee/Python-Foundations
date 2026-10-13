#Day 2: 30 Days of python programming
first_name = "asmaa"
last_name = "elhassnaoui"
full_name = "asmaa elhassnaoui"
country = "AMERICA"
city = "NEWYORK"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name, last_name, full_name  = "asmaa" , "elhassnaoui", "asmaa elhassnaoui" 
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp)

radius = 30
area_of_circle = 3.14 * (radius ** 2)
print(area_of_circle)
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)
radius =int(input("enter the radius: "))
print(area_of_circle)

first_name = input("enter your name: ")
last_name = input("enter your lasy name: ")
country = input("enter your country: ")
age = int(input("enter your age: "))


#day 3 of the challenge
age = 19
height = 1.71

base_triangle = int(input("enter the base of the triangle: "))
height_triangle = int(input("enter the height of the triangle: "))
area_of_triangle = 0.5 * base_triangle * height_triangle
print("the area of the triangle is: ",area_of_triangle )

a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
perimeter = a + b + c
print("the perimeter is:", perimeter)