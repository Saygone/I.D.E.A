import First, Second, Third
c=len(Second.Second_w)

if Second.Second_w[c-1] == 'а' and 'я':
    First.First_w = First.First_w[:-2]
    First.First_w = First.First_w + 'ая'

print(First.First_w, Second.Second_w, Third.Third_w)
