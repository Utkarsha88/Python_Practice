def less_two(user):
    user=user[::-1]
    return user

def more_two(user):
      ran1="frf"
      ran2="ske"
      temp=user[0]
      c=""
      for i in range(1,len(user)):
         c=c+user[i]
      user=ran1+c+temp+ran2
      return user

def deco_more_two(user):
   c=""
   moded=""
   for i in range(3,len(user)-3):
      c=c+user[i]
   for j in range(len(c)):
      if(j!=len(c)-1):
         moded=moded+c[j]
      else:
         c=c[j]+moded
   return c
  

def main_code(string, decision):
      user=""
      final=""
      string= string+"!"
      for i in range(len(string)):

         if(string[i]!=" " and i!=len(string)-1):
            user=user+string[i]
         else:
            if(len(user)<3):
               modified=less_two(user)
               
            elif(decision==True):
                modified=deco_more_two(user)
                
            else:
               modified=more_two(user)
            user=""   
            final=final+modified+" "
      return final

   
string=input("Enter a string: ")
final=main_code(string,False)
print(f"your secret code is {final}","\n")
decision=input(" Do you want to decode this code again (y/n): ")
if(decision=="y"):
    final=main_code(final,True)
    print(f"Decoded code: {final}")
    print("\n")
else:
    print("Thank you")
    
 

    
   


      
         

                  

