#Третья задача

import os

base_path=os.getcwd()
dir_name = 'task'
dict={}
for filename in os.listdir(dir_name):
    full_path = os.path.join(base_path, dir_name, filename)
    with open(full_path) as file_obj:
        count=0
        review={}
        for line in file_obj:
            count+=1
            review[file_obj.name] = count
            dict.update(review)

sorted_values=sorted(dict.values())

sorted_review_dict={}
for i in sorted_values:
    for key in dict.keys():
        if dict[key]==i:
            sorted_review_dict[key]=dict[key]

for key_ in dict:
    with open(key_) as donor_obj:
        data=donor_obj.read()
    result_file = open('result.txt', 'w')
    result_file.write(data)




