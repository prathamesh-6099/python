# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute
class Sample:
    a=1


obj=Sample()
obj.a=0 # Instant attr is set 
print(obj.a) # It prints Instant attr bcz priorities of object attr>>class attr !!
print(Sample.a) # it prints class attr bcz it called !!
 # So answer of the above qestion is false !!