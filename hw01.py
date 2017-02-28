Last login: Sat Feb 11 13:06:20 on ttys000
Iriss-MacBook-Air:~ iriszhang$ py hello.py
-bash: py: command not found
Iriss-MacBook-Air:~ iriszhang$ 
Iriss-MacBook-Air:~ iriszhang$ python hello.py
python: can't open file 'hello.py': [Errno 2] No such file or directory
Iriss-MacBook-Air:~ iriszhang$ 
Iriss-MacBook-Air:~ iriszhang$ hello.py
-bash: hello.py: command not found
Iriss-MacBook-Air:~ iriszhang$ ls
Applications		Downloads		Pictures
Creative Cloud Files	Library			Public
Desktop			Movies
Documents		Music
Iriss-MacBook-Air:~ iriszhang$ 
Iriss-MacBook-Air:~ iriszhang$ cd Desktop
Iriss-MacBook-Air:Desktop iriszhang$ cd Desktop
-bash: cd: Desktop: No such file or directory
Iriss-MacBook-Air:Desktop iriszhang$ cd desktop
-bash: cd: desktop: No such file or directory
Iriss-MacBook-Air:Desktop iriszhang$ cd 'Desktop'
-bash: cd: Desktop: No such file or directory
Iriss-MacBook-Air:Desktop iriszhang$ cd Desktop
-bash: cd: Desktop: No such file or directory
Iriss-MacBook-Air:Desktop iriszhang$ ls 
KAT
PRINT
Screen Shot 2017-02-11 at 1.08.49 PM.png
Screen Shot 2017-02-11 at 1.09.55 PM.png
USC 2016-17
disney
hello.py
itp125
itp125 - homework 01 - introduction to the command line.docx.7z
zinc.JPG
~$ 10-13 IR339 REFLECTION.docx
~$ GROUP RESEARCH.docx
~$es 10-11 SOCI 242 MIDTERM.docx
Iriss-MacBook-Air:Desktop iriszhang$ cd Desktop
-bash: cd: Desktop: No such file or directory
Iriss-MacBook-Air:Desktop iriszhang$ ls
KAT
PRINT
USC 2016-17
disney
hello.py
itp125
itp125 - homework 01 - introduction to the command line.docx.7z
zinc.JPG
~$ 10-13 IR339 REFLECTION.docx
~$ GROUP RESEARCH.docx
~$es 10-11 SOCI 242 MIDTERM.docx
Iriss-MacBook-Air:Desktop iriszhang$ 
Iriss-MacBook-Air:Desktop iriszhang$ python hello.py
Hello world!
What is your name?
Iris     
Traceback (most recent call last):
  File "hello.py", line 4, in <module>
    myName = input ()
  File "<string>", line 1, in <module>
NameError: name 'Iris' is not defined
Iriss-MacBook-Air:Desktop iriszhang$ 
Iriss-MacBook-Air:Desktop iriszhang$ 
Iriss-MacBook-Air:Desktop iriszhang$ 
Iriss-MacBook-Air:Desktop iriszhang$ python hello.py
Hello world!
What is your name?
Iris
It is good to meet you, Iris
The length of your name is:
4
What is your age?
19
You will be 20 in a year.
Iriss-MacBook-Air:Desktop iriszhang$ 
Iriss-MacBook-Air:Desktop iriszhang$ 
