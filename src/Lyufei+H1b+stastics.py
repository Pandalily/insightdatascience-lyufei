
# coding: utf-8

# In[2]:

import csv

with open(r"./input/h1b_input.csv") as f:
    data = []
    for line in f:
        data_line = line.rstrip().split(';')
        data.append(data_line)
headerlist = data[0]


# In[3]:

status_index=headerlist.index('CASE_STATUS')
occupation_index=headerlist.index('SOC_NAME')
occupationcode_index=headerlist.index('SOC_CODE')
state_index=headerlist.index('WORKSITE_STATE')
print(status_index,occupation_index,occupationcode_index,state_index)


# In[4]:

occupation_list = []
occupationcode_list = []
state_list = []
for i,x in enumerate (data):
    if 'CERTIFIED' in x:
            occupation_list.append(data[i][occupation_index])
            occupationcode_list.append(data[i][occupationcode_index])
            state_list.append(data[i][state_index])


# In[5]:

All_occupationcode = set(occupationcode_list)
occupationcode_dict = dict((x, occupationcode_list.count(x)) for x in All_occupationcode)
sum_occupationcode_dict = sum(occupationcode_dict.values())
occupationcode_dict_sorted_keys = sorted(occupationcode_dict, key=lambda k: (occupationcode_dict[k], k), reverse=True)
Top_10_occupationcode = {r: occupationcode_dict[r] for r in occupationcode_dict_sorted_keys[:10]}
print (Top_10_occupationcode)


# In[6]:

Top_10_occupationcode_list = [x for x in Top_10_occupationcode.items()]
Final_Top_10_occupationcode_list = []
for i in range(len(Top_10_occupationcode_list)):
    a = list(Top_10_occupationcode_list[i])
    Final_Top_10_occupationcode_list.append(a)
    Final_Top_10_occupationcode_list[i].insert(3,"{:.1%}".format(Top_10_occupationcode_list[i][1]/sum_occupationcode_dict))
Final_Top_10_occupationcode_list


# In[7]:

All_occupation = set(occupation_list) 
occupation_dict = dict((x,occupation_list.count(x)) for x in All_occupation)
sum_occupation_dict = sum(occupation_dict.values())
occupation_dict_sorted_keys = sorted(occupation_dict, key=lambda k: (occupation_dict[k], k), reverse=True)
Top_10_Occupations = {r: occupation_dict[r] for r in occupation_dict_sorted_keys[:10]}
Top_10_occupation_list = [x for x in Top_10_Occupations.items()]


# In[8]:

for i in range(len(Top_10_occupation_list)):
    print(Top_10_occupationcode_list[i][0])


# In[9]:

for i in range(len(Top_10_occupationcode_list)):
    Final_Top_10_occupationcode_list[i][0]=Top_10_occupation_list[i][0]
Final_Top_10_occupationcode_list


# In[10]:

Top_10_occupations_result = []
for t in Final_Top_10_occupationcode_list:
    for x in t:
        Top_10_occupations_result.append(x)
Top_10_occupations_result.insert(0,'TOP_OCCUPATIONS')
Top_10_occupations_result.insert(1,'NUMBER_CERTIFIED_APPLICATIONS')
Top_10_occupations_result.insert(2,'PERCENTAGE')
Top_10_occupations_result


# In[11]:
number_lines = len (Top_10_occupationcode_list) + 1
with open('./output/top_10_occupations.txt','w') as out:
    for i in range(number_lines):
            out.write("{};{};{};\n".format(Top_10_occupations_result[3*i],Top_10_occupations_result[3*i+1],Top_10_occupations_result[3*i+2]))


# In[12]:

All_state = set(state_list)
state_dict = dict((x,state_list.count(x))for x in All_state)
sum_state_dict = sum(state_dict.values())
state_dict_sorted_keys = sorted(state_dict, key=lambda k: (state_dict[k], k), reverse=True)
Top_10_states = {r: state_dict[r] for r in state_dict_sorted_keys[:10]}
print(Top_10_states)


# In[13]:

Top_10_states_list = [x for x in Top_10_states.items()]
Final_Top_10_states_list = []
for i in range(len(Top_10_states_list)):
    a = list(Top_10_states_list[i])
    Final_Top_10_states_list.append(a)
    Final_Top_10_states_list[i].insert(3,"{:.1%}".format(Top_10_states_list[i][1]/sum_state_dict))
Final_Top_10_states_list


# In[48]:

Top_10_states_result = []
for t in Final_Top_10_states_list:
    for x in t:
        Top_10_states_result.append(x)
Top_10_states_result.insert(0,'TOP_STATES')
Top_10_states_result.insert(1,'NUMBER_CERTIFIED_APPLICATIONS')
Top_10_states_result.insert(2,'PERCENTAGE')
Top_10_states_result


# In[53]:

with open('./output/top_10_states.txt','w') as out:
    for i in range(number_lines):
            out.write("{};{};{};\n".format(Top_10_states_result[3*i],Top_10_states_result[3*i+1],Top_10_states_result[3*i+2]))


# In[ ]:



