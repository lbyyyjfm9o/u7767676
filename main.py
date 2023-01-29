temperature_file = open("temperatures.txt")

temps_dictionary = {}

for line in temperature_file:
    split_line = line.split()
    city = split_line[0]
    temps = [int(x) for x in split_line[1:]]
    temps_dictionary[city] = temps

#print temps_dictionary["SF"][3]
#print temps_dictionary["NY"][3]
#print temps_dictionary["LA"][3]

output_file = open("temps_out.txt", "w")
output_file.write(str(temps_dictionary["SF"][3]) + "\n")
output_file.write(str(temps_dictionary["NY"][3]) + "\n")
output_file.write(str(temps_dictionary["LA"][3]) + "\n")
output_file.close()