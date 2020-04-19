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

import zlib
from comp_lib import *

import time


for data_type in type_list:
  for length in length_list:
    file_name = "data/data_{0}_0x{1:x}.bin".format(data_type, length)
    with open(file_name, "rb") as fin:
      byte_data = fin.read()
      data_size = len(byte_data)
      # print(data_size)
      # print(type(byte_data))
      # printb(byte_data)

      # Calc compression time
      start = time.time()
      # t = zlib.compress(byte_data, -1)
      t = zlib.compress(byte_data)
      comp_time = time.time() - start
      # print("# comp time[ms]: " + str(process_time*1000))
      # print("# comp time[ms]: {0:03f}".format(comp_time*1000))

      # printb(t)
      start = time.time()
      s = zlib.decompress(t)
      decomp_time = time.time() - start

      if(data_size==0):
        comp_ration = len(t)
      else:
        comp_ration = len(t)/data_size
      # print("# decomp time[ms]: {0:03f}".format(decomp_time*1000))

      if(s!=byte_data):
        printb(byte_data)
        printb(s)
        print("NG Data")
        exit()
      else:
        print("{0} {1} {2:03f} {3:03f}".format(len(t), comp_ration, comp_time*1000, decomp_time*1000))
