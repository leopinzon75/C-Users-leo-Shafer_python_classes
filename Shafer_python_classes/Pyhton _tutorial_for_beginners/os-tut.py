
import os

#print(dir(os))#

# ['DirEntry', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT',
# 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT',
# 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory',
# '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods',
# '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep',
# 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl',
# 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync',
# 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid',
# 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe',
# 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable',
# 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror',
# 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system',
# 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid',
# 'waitstatus_to_exitcode', 'walk', 'write']

#print(os.__file__)# C:\Program Files\Python310\lib\os.py
#print(os.getcwd())# C:\Users\leo
#print(os.get_terminal_size())# os.terminal_size(columns=261, lines=11)
#print(help(os.get_terminal_size))# get_terminal_size(...)
# Return the size of the terminal window as (columns, lines).
# os.chdir('/Users/leo/')

#print(os.getcwd())# C:\Users\leo


 

# print(os.listdir())

# ['#linkedin_py-practice.py', '.anaconda', '.android', '.conda', '.condarc', '.continuum', '.gitconfig', '.idea', '.idlerc',
# '.ipynb_checkpoints', '.ipython', '.jupyter', '.ssh', '.streamlit', '.VirtualBox', '.vscode', '.vscode-R', '15_pyhon_questions_interview', '333333', '3D Objects', 'abc',
# 'abcd', 'amimi', 'anaconda3', 'AppData', 'Application Data', 'bmi calculator.ipynb','Confirmation_court_date_arraingment_dic_18.PNG', 'Contacts', 'Cookies', 'count = 1.py', 
# 'COURT_DATE_TO_RESERVE_MONDAY_18_DIC.PNG', 'Desktop','devasc python.ipynb', 'digital resume configuration.PNG', 'digital resume configuration2.PNG', 'digital_resume', 'Documents', 'Downloads',
# 'egryetetererf', 'Fast_api', 'Favorites', 'file_demo.py', 'first_class_functions.py', 'flask api.ipynb', 'get-pip.py', 'gitlab-cicd-crash-course',
# 'gitlab-cicd-crash-course-1', 'gitlab-cicd-crash-course-2', 'gitlab-cicd-crash-course-3', 'How_to_create_python_environment_variables_in_windows.PNG',
# 'html flask code 1.PNG', 'html python code 2.PNG', 'html python code 3.PNG', 'html python code 4.PNG', 'html python code 5.PNG', 'IdeaProjects',
# 'import random.py', 'indeed_s_d', 'IntelGraphicsProfiles', 'intellij idea.PNG', 'js-basics', 'json_sample.json.ipynb', 'last_video_python_list.py',
# 'leetcode.py', 'Links', 'Local Settings', 'looking for a java spring developer.PNG', 'machine_slots_tim.ipynb', 'Music', 'My Documents',
# 'mytextfile.csv', 'mytextfile.txt', 'NetHood', 'New folder', 'New Rich Text Document.rtf', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2',
# 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.0.regtrans-ms', 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.1.regtrans-ms',
# 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.2.regtrans-ms', 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.blf',
# 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf', 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms',
# 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'number_guesser.py.ipynb', 'OneDrive',
# 'password_generator.py', 'Pictures', 'PrintHood', 'PycharmProjects', 'pycharm_xspace', 'python_defining_attributes_at_instances_self_classes.PNG',
# 'python_flask_app_active_visual_studio.PNG', 'python_so+far_ in_classes_ instances+schafer.PNG', 'python_so+far_ in_classes_ instances+schafer_2.PNG',
# 'Recent', 'resume', 'road map data structures and algorithms.PNG', 'rock sissors.ipynb', 'routerlist.csv', 'routerlist.txt', 'Saved Games', 'Searches', 'selenium features.PNG', 'selenium level sponsors.PNG',
# 'selenium_clients_and_webdriver_language_binders.PNG', 'SendTo', 'Shafer_python_classes', 'space_x.ipynb', 'Start Menu', 'Summary of regular expressions patterns.PNG', 'tempCodeRunnerFile.py', 'Templates',
# 'test.txt', 'test_sysexit.py.ipynb', 'textfile.txt', 'traffic ticket', 'traffic_court_arraingment.PNG', 'TUTORIAL', 'Tutorial_resume', 'untitled', 'Untitled-1.py', 'Untitled.ipynb', 'Untitled1.ipynb', 'Untitled11.ipynb',
# 'Untitled5.ipynb', 'Untitled6.ipynb', 'Untitled7.ipynb', 'Untitled8.ipynb', 'Untitled9.ipynb', 'upwork ci cd.PNG', 'Videos', 'vimfiles', 'VirtualBox VMs', 'VSCode Quick Start', '_viminfo']


# # What folders are in leo:

leo = ['#linkedin_py-practice.py', '.anaconda', '.android', '.conda', '.condarc', '.continuum', '.gitconfig', '.idea', '.idlerc',
'.ipynb_checkpoints', '.ipython', '.jupyter', '.ssh', '.streamlit', '.VirtualBox', '.vscode', '.vscode-R', '15_pyhon_questions_interview', '333333', '3D Objects', 'abc',
'abcd', 'amimi', 'anaconda3', 'AppData', 'Application Data', 'bmi calculator.ipynb','Confirmation_court_date_arraingment_dic_18.PNG', 'Contacts', 'Cookies', 'count = 1.py', 
'COURT_DATE_TO_RESERVE_MONDAY_18_DIC.PNG', 'Desktop','devasc python.ipynb', 'digital resume configuration.PNG', 'digital resume configuration2.PNG', 'digital_resume', 'Documents', 'Downloads',
'egryetetererf', 'Fast_api', 'Favorites', 'file_demo.py', 'first_class_functions.py', 'flask api.ipynb', 'get-pip.py', 'gitlab-cicd-crash-course',
'gitlab-cicd-crash-course-1', 'gitlab-cicd-crash-course-2', 'gitlab-cicd-crash-course-3', 'How_to_create_python_environment_variables_in_windows.PNG',
'html flask code 1.PNG', 'html python code 2.PNG', 'html python code 3.PNG', 'html python code 4.PNG', 'html python code 5.PNG', 'IdeaProjects',
'import random.py', 'indeed_s_d', 'IntelGraphicsProfiles', 'intellij idea.PNG', 'js-basics', 'json_sample.json.ipynb', 'last_video_python_list.py',
'leetcode.py', 'Links', 'Local Settings', 'looking for a java spring developer.PNG', 'machine_slots_tim.ipynb', 'Music', 'My Documents',
'mytextfile.csv', 'mytextfile.txt', 'NetHood', 'New folder', 'New Rich Text Document.rtf', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2',
'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.0.regtrans-ms', 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.1.regtrans-ms',
'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.2.regtrans-ms', 'NTUSER.DAT{53b39e87-18c4-11ea-a811-000d3aa4692b}.TxR.blf',
'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TM.blf', 'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000001.regtrans-ms',
'NTUSER.DAT{53b39e88-18c4-11ea-a811-000d3aa4692b}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'number_guesser.py.ipynb', 'OneDrive',
'password_generator.py', 'Pictures', 'PrintHood', 'PycharmProjects', 'pycharm_xspace', 'python_defining_attributes_at_instances_self_classes.PNG',
'python_flask_app_active_visual_studio.PNG', 'python_so+far_ in_classes_ instances+schafer.PNG', 'python_so+far_ in_classes_ instances+schafer_2.PNG',
'Recent', 'resume', 'road map data structures and algorithms.PNG', 'rock sissors.ipynb', 'routerlist.csv', 'routerlist.txt', 'Saved Games', 'Searches', 'selenium features.PNG', 'selenium level sponsors.PNG',
'selenium_clients_and_webdriver_language_binders.PNG', 'SendTo', 'Shafer_python_classes', 'space_x.ipynb', 'Start Menu', 'Summary of regular expressions patterns.PNG', 'tempCodeRunnerFile.py', 'Templates',
'test.txt', 'test_sysexit.py.ipynb', 'textfile.txt', 'traffic ticket', 'traffic_court_arraingment.PNG', 'TUTORIAL', 'Tutorial_resume', 'untitled', 'Untitled-1.py', 'Untitled.ipynb', 'Untitled1.ipynb', 'Untitled11.ipynb',
'Untitled5.ipynb', 'Untitled6.ipynb', 'Untitled7.ipynb', 'Untitled8.ipynb', 'Untitled9.ipynb', 'upwork ci cd.PNG', 'Videos', 'vimfiles', 'VirtualBox VMs', 'VSCode Quick Start', '_viminfo']
 
# print(len(leo))# 139
#print(os.getcwd())# C:\Users\leo



# What folders are in leo/Shafer:
os.chdir('/Users/leo/Shafer_python_classes/Pyhton _tutorial_for_beginners/')# change back slashes on windows

#print(os.getcwd())# C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners

#print(os.listdir())


# ['1.rb', 'conditional_and_booleans_6.py.py', 'Dictionaries_Working_with_value_pairs_5.py.py',
#  'functions_8.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py.py', 'intro.py',
#  'lists_tuple_and_sets_4.py.py', 'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py', 'Practice.py.py',
# 'Strings_Working_with_textual_data_2.py.py', 'tempCodeRunnerFile.py', '__pycache__']

#print(len(os.listdir()))# 15
# print(type(os.listdir()))# <class 'list'>


r = os.listdir()  


# print(r)

# ['1.rb', 'conditional_and_booleans_6.py.py', 'Dictionaries_Working_with_value_pairs_5.py.py',
# 'functions_8.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py.py', 'intro.py',
# 'lists_tuple_and_sets_4.py.py', 'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py', 'Practice.py.py',
# 'Strings_Working_with_textual_data_2.py.py', 'tempCodeRunnerFile.py', '__pycache__']





# for x in r:
#     print(x)  



# # 1.rb
# # conditional_and_booleans_6.py.py
# # Dictionaries_Working_with_value_pairs_5.py.py       
# # functions_8.py.py
# # Importing_Modules_And_Exploring_The_Standard_Library
# # Integers_and_floats_3.py.py
# # intro.py
# # lists_tuple_and_sets_4.py.py
# # loop_and_iterations_7.py.py
# # my_module.py
# # os-tut.py
# # Practice.py.py
# # Strings_Working_with_textual_data_2.py.py
# # tempCodeRunnerFile.py
# # __pycache__




    
# for index, x in enumerate(r):
#     print(index, x)

# 0 1.rb
# 1 conditional_and_booleans_6.py.py
# 2 Dictionaries_Working_with_value_pairs_5.py.py
# 3 functions_8.py.py
# 4 Importing_Modules_And_Exploring_The_Standard_Library
# 5 Integers_and_floats_3.py.py
# 6 intro.py
# 7 lists_tuple_and_sets_4.py.py
# 8 loop_and_iterations_7.py.py
# 9 my_module.py
# 10 os-tut.py
# 11 Practice.py.py
# 12 Strings_Working_with_textual_data_2.py.py
# 13 tempCodeRunnerFile.py
# 14 __pycache__




    
# for index, x in enumerate(r, start= 1):
#     print(index, x)

# 1 1.rb
# 2 conditional_and_booleans_6.py.py
# 3 Dictionaries_Working_with_value_pairs_5.py.py
# 4 functions_8.py.py
# 5 Importing_Modules_And_Exploring_The_Standard_Library
# 6 Integers_and_floats_3.py.py
# 7 intro.py
# 8 lists_tuple_and_sets_4.py.py
# 9 loop_and_iterations_7.py.py
# 10 my_module.py
# 11 os-tut.py
# 12 Practice.py.py
# 13 Strings_Working_with_textual_data_2.py.py
# 14 tempCodeRunnerFile.py
# 15 __pycache__
    
#print(sorted(r))# ['1.rb', 'Dictionaries_Working_with_value_pairs_5.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library',
# 'Integers_and_floats_3.py.py', 'Practice.py.py', 'Strings_Working_with_textual_data_2.py.py', '__pycache__', 'conditional_and_booleans_6.py.py',
# 'functions_8.py.py', 'intro.py', 'lists_tuple_and_sets_4.py.py', 'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py', 'tempCodeRunnerFile.py']

f = sorted(r)

# #print(f)# 

#['1.rb', 'Dictionaries_Working_with_value_pairs_5.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py.py',
#  'Practice.py.py', 'Strings_Working_with_textual_data_2.py.py', '__pycache__', 'conditional_and_booleans_6.py.py', 'functions_8.py.py', 'intro.py', 'lists_tuple_and_sets_4.py.py',
# 'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py', 'tempCodeRunnerFile.py']


# for index, x in enumerate(f, start= 1):
#      print(index, x)

# 1 1.rb
# 2 Dictionaries_Working_with_value_pairs_5.py.py
# 3 Importing_Modules_And_Exploring_The_Standard_Library
# 4 Integers_and_floats_3.py.py
# 5 Practice.py.py
# 6 Strings_Working_with_textual_data_2.py.py
# 7 __pycache__
# 8 conditional_and_booleans_6.py.py
# 9 functions_8.py.py
# 10 intro.py
# 11 lists_tuple_and_sets_4.py.py
# 12 loop_and_iterations_7.py.py
# 13 my_module.py
# 14 os-tut.py
# 15 tempCodeRunnerFile.py


#print(len(f))#15

# print(f[0])# 1.rb

# print(f[0:7])# ['1.rb', 'Dictionaries_Working_with_value_pairs_5.py.py',
# 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py.py',
# 'Practice.py.py', 'Strings_Working_with_textual_data_2.py.py', '__pycache__']


# print(f[7:])# ['conditional_and_booleans_6.py.py', 'functions_8.py.py', 'intro.py','lists_tuple_and_sets_4.py.py',
#  'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py','tempCodeRunnerFile.py']

# print(f[-1])# tempCodeRunnerFile.py

# print(f[-2])# os-tut.py

# print(f[-2:])# ['os-tut.py', 'tempCodeRunnerFile.py']

#print(f[:-2])# ['1.rb', 'Dictionaries_Working_with_value_pairs_5.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 
# 'Integers_and_floats_3.py.py', 'Practice.py.py', 'Strings_Working_with_textual_data_2.py.py', '__pycache__',
# 'conditional_and_booleans_6.py.py', 'functions_8.py.py', 'intro.py', 
# 'lists_tuple_and_sets_4.py.py', 'loop_and_iterations_7.py.py', 'my_module.py']

# print(f[15])# IndexError: list index out of range







#print(f)
  

# #['1.rb', 'Dictionaries_Working_with_value_pairs_5.py.py', 'Importing_Modules_And_Exploring_The_Standard_Library',
#  'Integers_and_floats_3.py.py', 'Practice.py.py', 'Strings_Working_with_textual_data_2.py.py', '__pycache__',
# # 'conditional_and_booleans_6.py.py', 'functions_8.py.py', 'intro.py', 
# 'lists_tuple_and_sets_4.py.py', 'loop_and_iterations_7.py.py', 'my_module.py', 'os-tut.py', 'tempCodeRunnerFile.py']


#print(type(f))# <class 'list'> 



# for index, x in enumerate(f, start= 1):
#      print(index, x)

# 1 1.rb
# 2 Dictionaries_Working_with_value_pairs_5.py.py
# 3 Importing_Modules_And_Exploring_The_Standard_Library
# 4 Integers_and_floats_3.py.py
# 5 Practice.py.py
# 6 Strings_Working_with_textual_data_2.py.py
# 7 __pycache__
# 8 conditional_and_booleans_6.py.py
# 9 functions_8.py.py
# 10 intro.py
# 11 lists_tuple_and_sets_4.py.py
# 12 loop_and_iterations_7.py.py
# 13 my_module.py
# 14 os-tut.py
# 15 tempCodeRunnerFile.py

#print(f.lower())# AttributeError: 'list' object has no attribute 'lower'
#print(f.upper())# AttributeError: 'list' object has no attribute 'upper'

#print(f.count())# TypeError: list.count() takes exactly one argument (0 given)

# print(f.count('working'))# 0

# print(f.count('Working'))# 0

# print(f.count('intro'))# 0

# print(f.count('intro.py'))# 1

# print(f.count('loop_and_iterations_7.py'))# 0 

# print(f.count('loop_and_iterations_7.py.py')) # 1

# print(f.count('os-tut.py'))# 1   

#print(f.count('h'))# 0  
  

# for index, x in enumerate(f, start= 1):
#      print(index, x)

#1 1.rb
# 2 Dictionaries_Working_with_value_pairs_5.py.py       
# 3 Importing_Modules_And_Exploring_The_Standard_Library
# 4 Integers_and_floats_3.py.py
# 5 Practice.py.py
# 6 Strings_Working_with_textual_data_2.py
# 7 __pycache__
# 8 conditional_and_booleans_6.py.py
# 9 functions_8.py.py
# 10 intro.py
# 11 lists_tuple_and_sets_4.py.py
# 12 loop_and_iterations_7.py.py
# 13 my_module.py
# 14 os-tut.py
# 15 tempCodeRunnerFile.py
# 
     
     # fixed doule file extension at file explorer then for loop again

# 1 1.rb
# 2 Dictionaries_Working_with_value_pairs_5.py
# 3 Importing_Modules_And_Exploring_The_Standard_Library
# 4 Integers_and_floats_3.py
# 5 Practice.py
# 6 Strings_Working_with_textual_data_2.py
# 7 __pycache__
# 8 conditional_and_booleans_6.py
# 9 functions_8.py
# 10 intro.py
# 11 lists_tuple_and_sets_4.py
# 12 loop_and_iterations_7.py
# 13 my_module.py
# 14 os-tut.py
# 15 tempCodeRunnerFile.py
    
#print(f.count('h'))# 0

# f.replace('Practice.py', 'abcd')# AttributeError: 'list' object has no attribute 'replace'

 
  
# leo.append('Art_new_file_00000001111111111')
# print(leo)#  file 'Art_new_file_00000001111111111' added at the end of the list
# print(len(leo))# 140
#print(os.listdir())  

# greeting = 'hello'
# name = 'Michael'
# message = name + leo
# print(message)# TypeError: can only concatenate str (not "list") to str

# print(type(r))# <class 'list'>


#print(dir(r))#

['_LCMAP_LOWERCASE', '_LCMapStringEx', '_LOCALE_NAME_INVARIANT', '__all__', '__builtins__',
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
'_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfinalpathname_nonstrict',
'_getfullpathname', '_getvolumepathname', '_nt_readlink', '_readlink_deep', 'abspath', 'altsep',
'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists',
'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize',
'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os',
'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split',
'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']

#print(type(f))# <class 'list'>

#print(dir(f))

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

#help(os)

# print(os._fspath(leo))#  line 1054, in _fspath
#     raise TypeError("expected str, bytes or os.PathLike object, "
# TypeError: expected str, bytes or os.PathLike object, not list


#print(os._fspath('leo'))# leo
#print(os.path(f))# TypeError: 'module' object is not callable
#print(os.__file__)# C:\Program Files\Python310\lib\os.py
  
#f.is_dir()# AttributeError: 'list' object has no attribute 'is_dir' 
#os.is_dir(f)# AttributeError: module 'os' has no attribute 'is_dir'. Did you mean: 'listdir'?



#print(os.listdir(f))#  TypeError: listdir: path should be string, bytes, os.PathLike or None, not list



# print(os.listdir())#


# ['1.rb', 'conditional_and_booleans_6.py', 'Dictionaries_Working_with_value_pairs_5.py',
# 'functions_8.py', 'Importing_Modules_And_Exploring_The_Standard_Library', 'Integers_and_floats_3.py', 'intro.py',
# 'lists_tuple_and_sets_4.py', 'loop_and_iterations_7.py', 'my_module.py', 'os-tut.py', 'Practice.py',
# 'Strings_Working_with_textual_data_2.py', 'tempCodeRunnerFile.py', '__pycache__']     


#print(os.name) # nt equals to windows




#print(os.path)# <module 'ntpath' from 'C:\\Program Files\\Python310\\lib\\ntpath.py'>  

# print(os.curdir)#  .  
# print(os.curdir())#  TypeError: 'str' object is not callable
# print(os.curdir(f))# TypeError: 'str' object is not callable
# print(os.pardir)# ..

#print(f.__dict__)# AttributeError: 'list' object has no attribute '__dict__'. Did you mean: '__dir__'?
#print(f.__dir__)# <built-in method __dir__ of list object at 0x0000022A007DF800>

#print(os.getcwd())# C:\Users\leo\Shafer_python_classes\Pyhton _tutorial_for_beginners




# print(dir(os.path))# ['_LCMAP_LOWERCASE', '_LCMapStringEx', '_LOCALE_NAME_INVARIANT', '__all__', '__builtins__',
#  '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_abspath_fallback', '_get_bothseps',
# '_getfinalpathname', '_getfinalpathname_nonstrict', '_getfullpathname', '_getvolumepathname', '_nt_readlink', '_readlink_deep',
# 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser',
# 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount',
# 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat',
# 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']

  






  
   











