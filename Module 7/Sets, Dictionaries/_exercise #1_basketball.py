#Challenge Exercise #1 Basketball
#This program demonsrates various set operations
baseball = set(['Jodi', 'Carmen','Aida', 'Alicia'])
basketball = set(['Eva','Carmen','Alicia','Sarah'])

print('The following students are on the baseball team:') #display members of the baseball set
for name in baseball:
    print(name)
print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)
print()
print('The following studnets play both baseball and basketball:') #demonstrates intersection
for name in baseball.intersection(basketball):
    print(name)
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)
print()
print('The following students play baseball, but not basketball:') #diff of baseball and basketball
for name in baseball.difference(basketball):
    print(name)
print()
print('The following students play basketball, but not baseball:')
for name in basketball.difference(baseball):
    print(name)
print()
print('The following students play one sport, but not both:')
for name in baseball.symmetric_difference(basketball):
    print(name)