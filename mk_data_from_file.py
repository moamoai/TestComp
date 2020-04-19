import random

type_list   = ["file"]
length_list = [
  0,
  4,
  16,
  256,
  4096,
  65536,
  1048576,
]

fix_data    = 0x77 # w


file_name = "../TEST_BIBLE/eng.txt"
with open(file_name, "rb") as fin:
  file_data = fin.read()
  file_size = len(file_data)
  print(file_size)

for data_type in type_list:
  for length in length_list:
    file_name = "data/data_{0}_0x{1:x}.bin".format(data_type, length)
    with open(file_name, "wb") as fout:
      bary = bytearray([])
      bary.extend(file_data[0:length])
      fout.write(bary)
