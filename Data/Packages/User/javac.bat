@ECHO OFF
cd %~dp1
ECHO Compiling %~nx1...
IF EXIST %~n1.class (
DEL %~n1.class
)
"C:\Program Files\Java\jdk1.8.0_161\bin\javac" -Xlint:unchecked %~nx1
IF EXIST %~n1.class (
ECHO Running %~n1...
start cmd /k java -ea %~n1
)