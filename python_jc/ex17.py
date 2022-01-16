from sys import argv
# isso retornará TRUE se existir um arquivo com base em seu nome em uma string como argumento
from os.path import exists

script, from_file, to_file = argv

print(f"Copyng from {from_file} to {to_file}")

# poderíamos fazer esses dois com uma linha, como?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} byter long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
