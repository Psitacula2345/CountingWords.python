


def cw():
     # fn - file name
     fn = input ("Enter the file name")

     numberofwords = 0
     
    # f = file- opening the file and reading it(r)
     f = open (fn, 'r')
     # verifying each line in the fille(f)
     for line in f:
         # splitting each word from the line
         words = line.split()

         # starting from 1st word and ending till the length (len) of the line
         numberofwords = numberofwords + len(words)

         print("Number of words:")
         print(numberofwords)

    # calling or acknowledging the function 
     cw()
    
