def mutation(input):
  value=[]
  value=input.split(",")
  first=value[0].lower()
  second=value[1].lower()
  if len(first)>len(second):
    for letter in second:
        if letter in first:
            first.replace('letter', '')
        else:
          return False
    return True
  else:
    return False
#print(mutation('hello,hel0000'))