import random

type_list   = ["w", "rand"]
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

for data_type in type_list:
  for length in length_list:
    file_name = "data/data_{0}_0x{1:x}.bin".format(data_type, length)
    with open(file_name, "wb") as fout:
      bary = bytearray([])
      # bary.append(fix_data)
      if(data_type=="w"):
        bary.extend([fix_data for i in range(length)])
      else:
        bary.extend([random.randint(0,255) for i in range(length)])
      fout.write(bary)
