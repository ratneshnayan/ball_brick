

order =int(input("enter the order of matrix :"))


for i in range (0,order):
    for j in range (0,order ):
        if(i==0 or j==0 or j==order-1):
            print('W',end =' ')
        elif(i==order -5 and j==order-5):
            print('1',end=' ')
        elif(i==order -4 and j==order-4):
            print('1',end=' ')
        
        elif (i==order -5 and j==order-4):
            print('1',end=' ')
        elif (i==order -4 and j==order-3):
            print('1',end=' ')
        elif (i==order -5 and j==order-3):
            print('1',end=' ')
        elif (i==order -4 and j==order-5):
            print('1',end=' ')
        
        elif(i== order-1 and j==(order-1)/2):
            print('O',end =' ')
        elif(i==order-1):
            print('G',end =' ')
        else:
            print(' ',end =' ')
    print()
print("Ball count is 3")
# level 1
# def st(x=enter the direction u need to go):

# def straight()
# x=input("enter the direction in whicg the ball is traverse")  
# if x==(ST):
    
#     for i in range (0,order):
#             for j in range (0,order ):
#                 if(i==0 or j==0 or j==order-1):
#                     print('W', end =' ')
#                 elif(i==order -5 and j==order-5):
#                     print('1',end=' ')
#                 # elif(i==order -4 and j==order-4):
#                 #     print('1',end=' ')
                    
#                 elif (i==order -5 and j==order-4):
#                     print('1',end=' ')
#                 elif (i==order -4 and j==order-3):
#                     print('1',end=' ')
#                 elif (i==order -5 and j==order-3):
#                     print('1',end=' ')
#                 elif (i==order -4 and j==order-5):
#                     print('1',end=' ')
                    
#                 elif(i== order-1 and j==(order-1)/2):
#                     print('O',end =' ')
#                 elif(i==order-1):
#                     print('G',end =' ')
#                 else:
#                     print(' ',end =' ')
#             print()
#     print("the ball count 3")


    
# # st()  
# # print()
# # print("Ball count is 2")         
# elif (X==LD):
    
#     for i in range (0,order):
#             for j in range (0,order ):
#                 if(i==0 or j==0 or j==order-1):
#                     print('W',end =' ')
#                 elif(i==order -5 and j==order-5):
#                     print('1',end=' ')
            
            
#                 elif (i==order -5 and j==order-4):
#                     print('1',end=' ')
#                 elif (i==order -4 and j==order-3):
#                     print('1',end=' ')
#                 elif (i==order -5 and j==order-3):
#                     print('1',end=' ')
#                 elif (i==order -4 and j==order-5):
#                     print('1',end=' ')
            
#                 elif(i== order-1 and j==(order-1)/2):
#                     print('O',end =' ')
#                 elif(i==order-1):
#                     print('G',end =' ')
#                 else:
#                     print(' ',end =' ')
#             print()
#     print ("the ball count is 2")
# else (X==RD): 
