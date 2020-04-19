type_list   = ["w", "rand", "file"]
length_list = [
#  0,
  4,
  16,
  256,
  4096,
  65536,
  1048576,
]

import zlib
import lz4.frame
from comp_lib import *
import time
import zstd

# lib_list = ["zlib", "lz4", "zstd"]
lib_list = ["zstd"]
# lib_list = ["lz4"]
for lib in lib_list:
  print("#####################")
  print("# " + lib)
  print("#####################")
  for data_type in type_list:
    print("# " + data_type)
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
        if(lib=="zlib"):
          t = zlib.compress(byte_data)
        elif(lib=="zstd"):
          t = zstd.compress(byte_data, 1)
        else:
          t = lz4.frame.compress(byte_data)
        comp_time = time.time() - start
        # print("# comp time[ms]: " + str(process_time*1000))
        # print("# comp time[ms]: {0:03f}".format(comp_time*1000))
  
        # printb(t)
        start = time.time()
        if(lib=="zlib"):
          s = zlib.decompress(t)
        elif(lib=="zstd"):
          s = zstd.decompress(t)
        else:
          s = lz4.frame.decompress(t)

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
  