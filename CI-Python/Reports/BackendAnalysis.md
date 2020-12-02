# Backend Unit test case

The method login_user fThe method login_user from backend.py will be used as the one backend method unit. Black box testing is based on the software’s specification and required functionality. Their methods are independent of the software.  Input coverage test are used to analyze the intended input.  One could run exhaustive input coverage testing and analyze all the possible inputs. Then create test cases based on the analysis. However Exhaustive testing is inefficient and extremely rare in practice. In our case when we are working with logging in users, there is an endless amount of possible inputs. Thus testing all possible inputs in our case is impossible.  Thus for efficiency we must partition the possible inputs into equivalence classes (classes that share with something in common).  To create good covering partitions, we want the simplest input values and to vary them as little as possible.  The advantages of input partition Testing is that it’s intuitive for testing, straightforward to identify a set of partitions and easy to verify when we are done. Note the actions of the program are not taken into account only all of its input classes.rom backend.py will be used as the one backend method unit.
Black box testing is based on the software’s specification and required functionality.
 Their methods are independent of the software.  Input coverage test are used to analyze the intended input.  One could run exhaustive input coverage testing and analyze all the possible inputs. Then create test cases based on the analysis. However Exhaustive testing is inefficient and extremely rare in practice. In our case when we are working with logging in users, there is an endless amount of possible inputs. Thus testing all possible inputs in our case is impossible.  Thus for efficiency we must partition the possible inputs into equivalence classes (classes that share with something in common).  To create good covering partitions, we want the simplest input values and to vary them as little as possible.  The advantages of input partition Testing is that it’s intuitive for testing, straightforward to identify a set of partitions and easy to verify when we are done. Note the actions of the program are not taken into account only all of its input classes.
 ## Requirement partition
* R1. Accept a  email and password as input
 * R2. Search for an user in the db by the email inputted in R1
 * R3.  If the user isn’t found output None
 * R4. If the password is not right output none
 * R5. If the user is found and the password is right output user 


## Input Partition
 
 For the sake of the analysis  lets assume that the following information is already in the data base:
Email: paulblart@mallcop.com   password: BubblySparkles99
and is a valid entry. Next lets assume the following is invalid Email: Bad@user.com and Password: Bad_pass

|Partition| Email partition| Password Partition  | Email Input| Password input |
|:----:   | :----:         |:----:             | :---:        | :----:|
|   P1 |  Valid   |  valid   |   paulblart@mallcop.com |   BubblySparkles99.    |
|  P2  |  Valid   |  Invalid     |  paulblart@mallcop.com |   Bad_pass  |
| P3   |  inValid     |  valid   | bad@user.com |   BubblySparkles99.   |
|   P4 |  Invalid     |  Invalid     |   bad@user.com  |   Bad_pass |
|