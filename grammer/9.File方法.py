file = open('D:\Study\python\grammer\data.txt')

file.close()
file.flush() #刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
file.fileno()
file.isatty()
file.next()
# file.read([size]) #从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size]) #读取整行，包括 "\n" 字符。
# file.readlines([sizehint]) 
# 读取所有行并返回列表，若给定 sizeint>0，返回总和大约为 sizeint 字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence])
# 设置文件当前位置
# file.tell()
# 返回文件当前位置。
# file.truncate([size])
# 截取文件，截取的字节通过 size 指定，默认为当前文件位置
# file.write(str)
# 将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence)
# 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。