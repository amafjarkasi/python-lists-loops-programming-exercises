my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:

my_sample_list[1] = "Steven"
my_sample_list[-1] = "Pepe"
my_sample_list[0] = str(my_sample_list[2] + my_sample_list[4])
my_sample_list = reversed(my_sample_list)

for _ in my_sample_list:
    print(_)
