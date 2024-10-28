student=[
{"firstname":"reza" , "lastname":"paktinat" , "SID":"8113"   } ,
{"firstname":"arvin" , "lastname":"hatef" , "SID":"8102"   } ,






 ]
sorted_student=sorted(student,key=lambda x : (x["firstname"],x["lastname"],x["SID"]))


print("Sorted students info:")
for student in sorted_student:
   print(student)
