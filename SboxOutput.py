def OutputGenerator(matrix,Sbox,choice):
    rows=0
    cols=0
    listMatrix=[]
    listSbox=[]
    if(choice==1):
        rows=16
        cols=16
        for i in range(0,rows):
            for j in range(0,cols):
                listMatrix.append(matrix[i][j])
        for i in range(0,rows):
            for j in range(0,cols):
                listSbox.append(Sbox[i][j])
    if(choice==2):
        rows=8
        cols=8
        for i in range(0,rows):
            for j in range(0,cols):
                listMatrix.append(matrix[i][j])
        for i in range(0,rows):
            for j in range(0,cols):
                listSbox.append(Sbox[i][j])
    if(choice==3):
        rows=1
        cols=16
        listMatrix=matrix
        listSbox=Sbox
    result=listSbox
    
    for i in range(0,len(listSbox)):
     
        result[i]=listMatrix[listSbox[i]-1]
    
    return result

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64








