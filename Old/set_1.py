input_list=[1,2,3,1]
set_a=set()
dup_flag=False

for i in input_list:
    if i in set_a:
        dup_flag=True
    else:
        set_a.add(i)  

print(dup_flag)
