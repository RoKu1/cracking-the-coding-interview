# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time, implement a method to count how many possible ways the child can run up the
# stairs.
N = int(input("Enter N => "))
# for 0 steps
a = 1  
# for 1 step
b = 1
# for 2 steps
c = 2
#for n step "d"
d = 0
for i in range(2,N):
    d = a + b + c
    a = b
    b = c
    c = d

print(d)