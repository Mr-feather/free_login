import os
import sys
import shutil
from py_compile import compile

# print "argvs:",sys.argv
if len(sys.argv) == 3:
    comd = sys.argv[1]  # 输入的命令
    path = sys.argv[2]  # 文件的地址
    if os.path.exists(path) and os.path.isdir(path):
        for parent, dirname, filename in os.walk(path):
            for cfile in filename:
                fullname = os.path.join(parent, cfile)
                if comd == 'clean' and cfile[-4:] == '.pyc':
                    try:
                        os.remove(fullname)
                        print("Success remove file:%s" % fullname)
                    except:
                        print("Can't remove file:%s" % fullname)
                if comd == 'compile' and cfile[-3:] == '.py':  # 在这里将找到的py文件进行编译成pyc，但是会指定到一个叫做__pycache__的文件夹中
                    try:
                        compile(fullname)
                        print("Success compile file:%s" % fullname)
                    except:
                        print("Can't compile file:%s" % fullname)
                if comd == 'remove' and cfile[-3:] == '.py' and cfile != 'settings.py' and cfile != 'wsgi.py':
                    try:
                        os.remove(fullname)
                        print("Success remove file:%s" % fullname)
                    except:
                        print("Can't remove file:%s" % fullname)
                if comd == 'copy' and cfile[-4:] == '.pyc':
                    parent_list = parent.split("/")[:-1]
                    parent_up_path = ''
                    for i in range(len(parent_list)):
                        parent_up_path += parent_list[i] + '/'
                    shutil.copy(fullname, parent_up_path)
                    print('update the dir of file successfully')
                if comd == 'cpython' and cfile[-4:] == '.pyc':
                    cfile_name = ''
                    cfile_list = cfile.split('.')
                    for i in range(len(cfile_list)):
                        if cfile_list[i] == 'cpython-35':
                            continue
                        cfile_name += cfile_list[i]
                        if i == len(cfile_list) - 1:
                            continue
                        cfile_name += '.'
                    shutil.move(fullname, os.path.join(parent, cfile_name))
                    print('update the name of the file successfully')

    else:
        print("Not an directory or Direcotry doesn't exist!")
else:
    print("Usage:")
    print("\tpython compile_pyc.py clean PATH\t\t#To clean all pyc files")
    print("\tpython compile_pyc.py compile PATH\t\t#To generate pyc files")
    print("\tpython compile_pyc.py copy PATH\t\t#To clean all pyc files")
    print("\tpython compile_pyc.py remove PATH\t\t#To remove py files")
