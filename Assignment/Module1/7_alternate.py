"""Write a Python program to print every alternate character from the 
 string starting from index 1"""

str = '_h_e_l_l_o_p_y_t_h_o_n'

for i in range(1, len(str), 2):
    print(str[i],end="")

