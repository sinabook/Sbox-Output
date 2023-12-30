#Sina Mollazadeh 4001223247 Differential Cryptoanalysis
from SBoxDES import SboxDES
from SBoxAES import SboxAES
from SboxBabyAES import SboxBabyAES
from SboxOutput import OutputGenerator

def generator(list,n,m):
#This function generates an n*m matrix with an input list and two n,m Integers
    res=[]
    k=0
    for idx in range(0, n):
        sub = []
        for jdx in range(0, m):
            sub.append(list[k])
            k += 1
        res.append(sub)    
    return res
print("***************************************Welcome to My Sbox Cracker***************************************")
print("Choose one of the following")
print("1.AES Sbox")
print("2.DES Sbox")
print("3.Baby AES Sbox")
print("4.BabyAES")
c=int(input())
list=[]
matrix=[]
AESmatrix=[]
DESmatrix=[]
BabyAESmatrix=[]
if(c==1):
    print("Please Enter 16*16 bits")
    input_string=input()
    user_list = input_string.split(" ")
    for i in range (0,len(user_list)):
        user_list[i]=int(user_list[i])
    AESmatrix=generator(user_list,16,16)
    matrix=OutputGenerator(AESmatrix,SboxAES,c)
if(c==2):
    print("Please Enter 8*8 bits")
    input_string=input()
    user_list = input_string.split(" ")
    for i in range (0,len(user_list)):
        user_list[i]=int(user_list[i])
    DESmatrix=generator(user_list,8,8)
    matrix=OutputGenerator(DESmatrix,SboxDES,c)
if(c==3):
    print("Please Enter 1*16 bits")
    input_string=input()
    user_list = input_string.split(" ")
    for i in range (0,len(user_list)):
        user_list[i]=int(user_list[i])
    BabyAESmatrix=user_list
    matrix=OutputGenerator(BabyAESmatrix,SboxBabyAES,c)
# if(c==1):
#     print(AESmatrix)
# if(c==2):
#     print(DESmatrix)
# if(c==3):
#     print(BabyAESmatrix)
# print(matrix)
# print("Number of Bits that are exactly the same")
