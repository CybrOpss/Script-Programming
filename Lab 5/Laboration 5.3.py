# Problem 5.3: Doing things

import csv

csv_dict = {}

with open("configuration-values.csv","r") as conf_values:

    for line in conf_values: 

        key_values = line.split(",")
        key = key_values[0]

        value = key_values[1:]
        csv_dict[key] = value 
        
with open("configuration-template.config","r") as template_file:
    template_string = template_file.read()

for i in range(5):
    new_template_string = template_string
    for key in csv_dict: 
        new_template_string = new_template_string.replace("{"+key+"}", csv_dict[key][i])        
    with open("new_template" +str(i)+".config","w") as new_temp:
        new_temp.write(new_template_string)


