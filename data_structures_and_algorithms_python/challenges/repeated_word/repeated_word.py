def repeated_word(input):

    arr = input.split(' ')

    output = set()
    for i in arr:
        i = i.replace(',', '').lower()
        i = i.replace('...', '').lower()
        if i in output:
           return(i)
      
        output.add(i) 

repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")        

