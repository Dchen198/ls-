import os,time,sys,stat,argparse


def cmd(fun):

    def wapper(*args):

        path = input('please input your want to see the path:\n')

        fun(path)

    return wapper

# @cmd
#
# def ls(*args):
#
#     f = os.listdir(*args)
#
#     for i in f:
#
#         print(i)
#
#
# ls()  #改进装饰器H逼格写法

@cmd

def ls_l(*args):

    f = os.listdir(*args)

    for i in f:

        f_stat = os.stat(*args)

        f_time = time.mktime(f_stat)

        print(stat.filemode(f_stat.st_mode),f_time,f_stat.st_size,f_stat.st_gid,i)
ls_l()










