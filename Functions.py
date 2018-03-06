
# Homework 2

# Question 1
print '\nQuestion1'
import random 
print 'Play a PowerBall game by pressing <Enter>, Good Luck!'
def lottery():
    print 'Your PowerBall Game result is: '
    for i in range(1,6):
        print random.sample(range(1, 60), 5)[i-1],
    print random.randint(1,35),
    
lottery()


# Question 2

print '\n\nQuestion2'
def cornell():
    num_lines = 0
    num_words = 0
    num_cha = 0
    num_para = 1
    with open('D:\STSCI4060\AboutCornell(1).txt') as inputfile:
        for line in inputfile:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            if line in ('\n'):
                    num_para += 1
            for word in words:
                num_cha += len(word)
    print 'In the article there are ', num_lines, ' lines, ', num_words, 'words, ', num_cha, ' characters(excluding whitespaces) and ', num_para, ' paragraphs.'
    
cornell()


# Question 3
print '\nQuestion3'
def matrixmult(A,B):
    print '\nInput two matrices A and B to multiply'
    print 'Input Matrix A: ', A
    print 'Input Matrix B: ', B
    while len(A[0])!=len(B):
        print ('Error, these two matrixes cannot be multiplied since their dimensions do not match')
        A=input("Input Matrix A: ")
        B=input("Input Matrix B: ")
    ls=[[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
    for i in xrange(len(A)) :
        for j in xrange(len(B[0])): 
            for k in range(len(A[0])):
                ls[i][j]+=A[i][k]*B[k][j]
    print '\nMatrix A is : '
    for i in A:
        print i
    print '\nMatrix B is : '
    for i in B:
        print i
    print '\nMatrix C = AB is : '
    for i in ls:
        print i
def main():
    print 'Input two matrixes A and B to multiply'
    A=input("Input Matrix A: ")
    B=input("Input Matrix B: ")
    matrixMultiplication(A,B)
    
print matrixmult([[1,2,-1],[3,1,4]],[[-2,5],[4,-3],[2,1]])
