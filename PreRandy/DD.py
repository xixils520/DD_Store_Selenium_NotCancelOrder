#coding:utf-8
import random

dlt=[]
new_dlt=[]
def Test():
    before_data=[]
    after_data=[]
    first_one=before_data.pop(random.randint(0,len(before_data)))
    second_one=before_data.pop(random.randint(0,len(before_data)))
    third_one=before_data.pop(random.randint(0,len(before_data)))
    fourth_one=before_data.pop(random.randint(0,len(before_data)))
    fifth_one=before_data.pop(random.randint(0,len(before_data)))

    after_one=after_data.pop(random.randint(0,len(after_data)))
    after_two=after_data.pop(random.randint(0,len(after_data)))

    new_group=[]
    new_group.append(first_one)
    new_group.append(second_one)
    new_group.append(third_one)
    new_group.append(fourth_one)
    new_group.append(fifth_one)
    sort_group=sorted(new_group)

    if after_one<after_two:
        sort_group.append(after_one)
        sort_group.append(after_two)
    else:
        sort_group.append(after_two)
        sort_group.append(after_one)

    if sort_group[:-2]!=dlt[:-2]:
        tail_group=[]
        for one in sort_group:
            tail_group.append(one%10)
        if len(set(tail_group))>=4:
            tail_ss=[]
            for i in tail_group:
                new_ss=tail_group[0:tail_group.index(i)]+tail_group[tail_group.index(i)+1:7]
                for j in new_ss:
                    if i==j:
                        tail_ss.append(i)
                        tail_ss.append(j)
                    if i+j==10:
                        tail_ss.append(i)
                        tail_ss.append(j)
            if len(set(tail_ss))>2:
                new_dlt.append(sort_group)

