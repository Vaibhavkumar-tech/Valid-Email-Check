email=input("Enter Your Email:")
k=0
l=0
j=0
if len(email)>=6:
   if email[0].isalpha():
      if ("@" in email) and (email.count("@")==1):
         if (email[-3]==".") ^ (email[-4]=="."):
            for i in email:
               #digit,space,uppercase,@ . _
               if i==i.isspace:
                  k=1
               elif i==i.isdigit:
                  continue
               elif i==i.isupper():
                  l=9
               elif i=="@" or "." or "-":
                  continue
               else:
                  j=9
                  
            if (k==1) or (l==9) or (j==9):
               print("space wrong")
            else:
               print("Valid Email")
         else:
            print("Wrong Email 4")
      else:
         print("Wrong Email 3")
   else:
      print("Wrong Email 2")
else:
   print("Wrong Email 1")