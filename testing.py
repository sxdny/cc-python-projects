# Testing file ;)

class Grade:
    pass

grade = Grade()

# verificar que es del tipo grade

print(type(grade))

if isinstance(3, Grade):
    print("Es del tipo Grade...")
else:
    print("No es del tipo Grade.")