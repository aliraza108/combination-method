


n = int(input("enter the number of teams : "))
r = int(input("nter the combo : "))




#         n!
#   ______________
#   (n-r)! * r!



#      5*4*3*2*1  1*2*3*4*5
#   ______________
#   (n-r)! * r!



 # Implementing this function n!
 
ntotal = 1
for x in range(1,n+1):
    # print(x)
    ntotal = ntotal * x
    # print(ntotal)
   
rtotal = 1
for x in range(1,r+1):
    # print(x)
    rtotal = rtotal * x
    # print(rtotal) 

#(n-r)!
# z= n-r
z = n-r    
ztotal = 1
for x in range(1,z+1):
    # print(x)
    ztotal = ztotal * x
    # print(ztotal)  
    
final = ntotal / (ztotal * rtotal)
print(final)
# n_r = n-r
# n_rtotal = 1
# for y in range(1,n_r+1):
#     n_rtotal = n_rtotal * y
    




# rtotal = 1
# for z in range(1,r+1):
#     rtotal = rtotal * z
    
# combos = ntotal / (n_rtotal * rtotal)

# print(combos)



