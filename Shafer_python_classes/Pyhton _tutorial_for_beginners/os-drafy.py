

import os
from datetime import datetime 
#print(dir(os))

#  ['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL',
#    'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT',
#      'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK',
#        'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__',
#          '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
#            '_check_methods', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close',
#              'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange',
#                'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error',
#                  'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 
# 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable',
#  'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty',
#    'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep',
#      'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir',
#        'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile',
#          'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids',
#            'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate',
#              'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write'] 


# print(len(dir(os)))# 156
#print(os.getcwd)# <built-in function getcwd>
# print(os.getcwd())# C:\Users\leo 
 

#os.chdir('/Users/ ')# change back slashes on windows = C:\Users
#print(os.getcwd())# C:\Users
# print(len(os.listdir()))# 6

# print(os.listdir())# ['All Users', 'Default', 'Default User', 'desktop.ini', 'leo', 'Public']
# os.chdir('/Users/leo')# 
# print(os.getcwd())# C:\Users\leo
# print(len(os.listdir()))# 135 print(os.listdir()) is not edited temporarily



# os.chdir('/Users/leo/resume')# 
# print(os.getcwd()) #C:\Users\leo\resume
# print(len(os.listdir()))# 6
# print(os.listdir())# ['etc', 'Include', 'Lib', 'pyvenv.cfg', 'Scripts', 'share']



# os.chdir('/Users/leo/Shafer_python_classes/')# 
# print(os.getcwd())# C:\Users\leo\Shafer_python_classes
# print(len(os.listdir()))# 3
# print(os.listdir())# ['File_objects_Reading_and_writing_to_files', 'OOP_Classes', 'Pyhton _tutorial_for_beginners']




os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners')


# print(os.getcwd())# C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners


# print(len(os.listdir()))# 16


# print(os.listdir())# ['1.rb', 'conditional_and_booleans_6.py', 'Dictionaries_Working_with_value_pairs_5.py',
# 'functions_8.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py', 'intro.py',
# 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py', 'my_module.py', 'os-drafy.py', 'os-tut.py', 'Practice.py',
# 'Strings_Working_with_textual_data_2.py', 'tempCodeRunnerFile.py', '__pycache__']








# To create a folder in C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners called 'os-demo', there are 2 ways:



#'os-demo' and 'sub-dir-1'


#os.mkdir('os-demo/sub-dir-1')# FileNotFoundError: [WinError 3] The system cannot find the path specified: 'os-demo/sub-dir-1'
#It will 'not' create a directory or folder more than one level deep


#os.makedirs('os-demo/sub-dir-1')# create a directory or folder more than one level deep
#print(os.listdir()) 
#['1.rb', 'conditional_and_booleans_6.py', 'Dictionaries_Working_with_value_pairs_5.py', 'functions_8.py',
#  'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py', 'intro.py', 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py',
# 'my_module.py', 'os-drafy.py', 'os-tut.py', 'Practice.py', 'Strings_Working_with_textual_data_2.py', 'tempCodeRunnerFile.py', 'test.txt', '__pycache__']




# To remove the is a similar procedure

#os.removedirs('os-demo/sub-dir-1')

#print(os.listdir())


#os.rmdir('os-demo/sub-dir-1')# Only one folder  
#print(os.listdir())    

 
# #os.removedirs('os-demo/sub-dir-1')  
# print(os.getcwd())
    
# #print(os.listdir()) 
# #os.removedirs('os-demo/sub-dir-1')
# #os.rmdir('os-demo/sub-dir-1')
# print(os.listdir()) 

# os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/os-demo')
# # print(os.getcwd())# C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners\os-demo
# #print(os.listdir())   

# os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/')
# print(os.getcwd())# C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners
#os.removedirs('os-demo/sub-dir-1')



# To rename a file or a folder

# os.rename()# TypeError: rename() missing required argument 'src' (pos 1)

# os.rename('test.txt', 'demo.txt')


# print(os.listdir())# ['1.rb', 'conditional_and_booleans_6.py', 'demo.txt','Dictionaries_Working_with_value_pairs_5.py', 'functions_8.py',
# 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py', 'intro.py', 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py',
# 'my_module.py', 'os-drafy.py', 'os-tut.py', 'Practice.py', 'Strings_Working_with_textual_data_2.py', 'tempCodeRunnerFile.py', '__pycache__']






# How can we look at some information about our file:

#print(os.stat('demo.txt'))# os.stat_result(st_mode=33206, st_ino=14636698789013760, st_dev=1925983599, st_nlink=1, st_uid=0, st_gid=0, st_size=1170,
# st_atime=1704248170, st_mtime=1704248169, st_ctime=1704246740)

# print(os.stat('demo.txt').st_size)# 1170, note: first time using more than one dot in the line----------------------







# For the modification time 'st_mtime' it returns a timestamp and to make it human readable format import datetime



#print(os.stat('demo.txt'))# os.stat_result(st_mode=33206, st_ino=14636698789013760, st_dev=1925983599, st_nlink=1, st_uid=0, st_gid=0, st_size=1170,
# st_atime=1704248170, st_mtime=1704248169, st_ctime=1704246740)



#print(os.stat('demo.txt').st_mtime)# 1704248169.7845247
#print(os.stat('demo.txt').st_atime)# 1704248170.6227565
# print(os.stat('demo.txt').st_ctime)# 1704246740.4199128

# mod_time =(os.stat('demo.txt').st_mtime)
# print(datetime.fromtimestamp(mod_time))# 2024-01-02 18:16:09.784525 now 7:13 pm

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))# 2024-01-02 18:16:09.784525

# mod_atime = os.stat('demo.txt').st_atime
# print(datetime.fromtimestamp(mod_atime))# 2024-01-02 18:16:10.622756

# mod_ctime = os.stat('demo.txt').st_ctime
# print(datetime.fromtimestamp(mod_ctime))# 2024-01-02 17:52:20.419913  20 mnutes earlier





#print(type(os.stat))# <class 'builtin_function_or_method'>

# print(os.listdir())


# print(os.getcwd())# # os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/')




# To see the entire tree of directories and files from the current directory or folder use the os.walk method:

# print(dir(os.walk))# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__',
# '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
# '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



# print(help(os.walk))#
# #Help on function walk in module os:

# walk(top, topdown=True, onerror=None, followlinks=False)
#     Directory tree generator.

#     For each directory in the directory tree rooted at top (including top
#     itself, but excluding '.' and '..'), yields a 3-tuple

#         dirpath, dirnames, filenames

# -- More  --

# for dirpath, dirnames, filenames in os.walk('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/'):
#     print('Current Path:' , dirpath)
#     print('Directories:', dirnames  )
#     print('files:', filenames)
#     print()

# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/
# Directories: ['Importing_Modules_And_Exploring_The_Standard_Library', '__pycache__']
# files: ['1.rb', 'conditional_and_booleans_6.py', 'demo.txt', 'Dictionaries_Working_with_value_pairs_5.py', 'functions_8.py', 'Integers_and_floats_3.py',
#  'intro.py', 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py', 'my_module.py', 'os-drafy.py', 'os-tut.py', 'Practice.py',
# 'Strings_Working_with_textual_data_2.py', 'tempCodeRunnerFile.py']
    

# os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners')

# print(os.getcwd())




#print(len())

# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/Importing_Modules_And_Exploring_The_Standard_Library
# Directories: []
# files: []

# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/__pycache__
# Directories: []
# files: ['my_module.cpython-310.pyc']





# changes made in the explorer file
    
# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/
# Directories: ['Importing_Modules_And_Exploring_The_Standard_Library', '__pycache__']
# files: ['1.rb', 'conditional_and_booleans_6.py', 'demo.txt', 'Dictionaries_Working_with_value_pairs_5.py', 'functions_8.py', 'Integers_and_floats_3.py', 'intro.py', 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py', 'os-drafy.py', 'os-tut.py', 'Practice.py', 'Strings_Working_with_textual_data_2.py']

# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/Importing_Modules_And_Exploring_The_Standard_Library
# Directories: []
# files: ['my_module.py', 'tempCodeRunnerFile.py']

# Current Path: /Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/__pycache__
# Directories: []
# files: ['my_module.cpython-310.pyc']





########################this code line went wrong

# print(os.getcwd())# os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners')

#print(os.getcwd())

#print(os.environ.get('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners'))  

#file_path = os.path.join(os.environ.get('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners'),  "texto.txt")

# print(file_path)
#######################################################################################





# print(os.path.basename('temp/test.txt'))# test.txt

# print(os.path.dirname('temp/test.txt'))# temp

# print(os.path.split('temp/test.txt'))# ('temp', 'test.txt')

# print(os.path.exists('temp/test.txt'))# False

# print(os.path.isdir('temp/test.txt'))# False

  
# print(os.path.isfile('temp/test.txt'))# False

# print(os.path.splitext('temp/test.txt'))# ('temp/test', '.txt')

# print(dir(os.path))# ['_LCMAP_LOWERCASE', '_LCMapStringEx', '_LOCALE_NAME_INVARIANT',1
# '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', '_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfinalpathname_nonstrict', '_getfullpathname',
# '_getvolumepathname', '_nt_readlink', '_readlink_deep', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir',
# 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime',
# 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep',
# 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']






  









      