def greet(language):
    if language == 'es':
        print 'Hola'
    elif language == 'fr':
        print 'Bonjour'
    else:
        print 'Hello'

greet('es')
greet('fr')
greet('hi')
    
    
def greet1(language):
    if language == 'es':
        return 'Hola'
    elif language == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

x = greet1('es')
y = greet1('fr')
z = greet1('hi')

print x,y,z

inputlang = raw_input("What language? Choices are en, es, or fr.")

greet (inputlang)


inputlang = raw_input("What language? Choices are en, es, or fr only.")
if inputlang == 'es' or inputlang == 'fr' or inputlang == 'en':
    greet (inputlang)
else:
    print "Please choose from en, es, or fr."
    

inputlang = raw_input("What language? Choices are 1:en, 2:es, or 3:fr only.")
if inputlang == '1' :
    greet ('en')
elif inputlang == '2':
    greet('es')
else:
  greet('fr')
    
