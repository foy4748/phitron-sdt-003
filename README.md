# Index

- [Instructions](#instructions)
    - [Course Credentials](#course-credentials)
    - [Necessary Links](#necessary-links)  
    - [Running the project](#running-the-project)   
	- [For using pipenv](#for-using-pipenv)
	- [ **How it works** **[`Important`]**](#how-it-works)

# Instructions

## Course Credentials

- Name  : AB. MD. FAISAL RAHMAN
- Email : faisal.rahman.4748.ph@gmail.com

## Necessary Links
- Requirements : [Google Doc](https://docs.google.com/document/d/1KXJ72TsrQeO91X5Izua_DbKylof8xg0Qej1TUiU6s8s/edit)
- GiHub Link : [GitHub](https://github.com/foy4748/phitron-sdt-003)


## Running the project

Simply run

```console
python main.py
```
OR

```console
python3 main.py
```



## For using pipenv

Run this command below to activate or initialize a pipenv virtual environment
```console
pipenv shell
```

This will require python version 3.11  

**If you are not running python 3.11, then don't need this**

## How it works  

- The main.py script creates 2 test Users and Admins.  

- To access the User/Admin menu, it will ask the id/account\_no to login as that account. Since there is **NO AUTHENTICATION SYSTEM** , simply enter 1 or 2 , since two users are created automatically for both types.  

- I could've printed user/admin list while choosing User/Admin menu for loggin in. But Printing this list would be a high security vulnerability.  

- Created User and Admin instances are stored within the corresponding class attributes. The attributes are simple python list data structure.  

- User/Admin accounts are stored in different list.  

- **[`Important`]** The id/account\_no is simply the 1\-based index of the corresponding list.  

- User input will always be 1-based index for better user experience (UX). Under the hood it will be changed to 0-based index  

- Whatever menu appears, Enter 1-based index in range to go further.  

