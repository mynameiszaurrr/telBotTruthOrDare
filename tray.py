# new = []
# vul_ques_list = []
#
# with open('questions/vulgar_ques.txt') as f:
#     src = f.read()
#     lists = src.split('.')
# for i in lists:
#     new.append(i.strip())
#
# for j in new[:-1]:
#     if j.isnumeric():
#         continue
#     elif j[-3].isnumeric():
#         vul_ques_list.append(j[0:-3])
#         continue
#     elif j[-2].isnumeric():
#         vul_ques_list.append(j[0:-2])
#         continue
#     elif j[-1].isnumeric():
#         vul_ques_list.append(j[0:-1])
#         continue
#     else:
#         vul_ques_list.append(j)
#
import random


def questions_from_hard_list(text_file):
    new = []
    vul_ques_list = []
    finally_ques = []
    with open(text_file, 'r') as f:
        src = f.read()
        lists = src.split('.')
    for i in lists:
        new.append(i.strip())
    for j in new[:-1]:
        if j.isnumeric():
            continue
        elif j[-3].isnumeric():
            vul_ques_list.append(j[0:-3])
            continue
        elif j[-2].isnumeric():
            vul_ques_list.append(j[0:-2])
            continue
        elif j[-1].isnumeric():
            vul_ques_list.append(j[0:-1])
            continue
        else:
            vul_ques_list.append(j)
    for k in vul_ques_list:
        kk = k.strip()
        if 'n' in kk:
            elements = kk.strip('n')
            finally_ques.append(elements[0][:-1])
            finally_ques.append(elements[1])
        else:
            finally_ques.append(kk)
    return finally_ques


ques = questions_from_hard_list('questions/vulgar_ques.txt')

print(random.choice(ques))
