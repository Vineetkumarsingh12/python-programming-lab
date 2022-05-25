se="the quick brown fox jumps over the lazy dog"
sen=se.lower()
n=0
sen1=[]
for i in range(len(sen)):
 if sen[i]!=" " and sen[i] not in sen1 :
    sen1.append(sen[i])       
for i in range(len(sen1)):
      if ord(sen1[i]) in range(97,123):
           n+=1
if n==26 :
     print("pangram")  
