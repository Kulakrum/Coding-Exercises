import sys

sys.argv[0]
sys.argv[1]
#sys.argv[2] 

def luke():
    relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}
    
    #print('Luke, I am your %s' %relations[sys.argv[1]])
    if sys.argv[1] == 'Darth':
        if sys.argv[2] == 'Vader':
        
            print('No, I am your father')
        else:
            print('Enter Valid Name.')
    
    #if sys.argv[1] + sys.argv[2] = 'Darth Vader':
    #    print('No, I am your %s' %(relations))
    else:
       print('Luke, I am your %s' %relations[sys.argv[1]])

luke()    
    