# Enter your code here. Read input from STDIN. Print output to STDOUT

mat_size = input().split()
down = int(mat_size[0])*2
right = int(mat_size[1])

pattern = '.|.'


for i in range (1, int(down/2), 2):
    print ((pattern*i).center(right,"-"))
        
print("WELCOME".center(right,"-"))

for i in range (int(down/2),1, -2):
    print ((pattern*(i-2)).center(right,"-"))
