This is to learn and develop Python language with small steps.
###################


These commands work for github

git config --global user.name "Sam Smith"
git config --global user.email sam@example.com

#######################################################################################################

$ git init      
$ git add .     
$ git commit -m "Changes"

or
#######################################################################################################

Common usages and options for git init
git init: Transform the current directory into a Git repository
git init <directory>: Transform a directory in the current path into a Git repository
git init --bare: Create a new bare repository (a repository to be used as a remote repository only, that won't contain active development)
#######################################################################################################
some commands

git pull
git clone username@host:/path/to/repository
git clone /path/to/repository
git add <filename>
git commit -m "Commit message"
git add *
git commit -a
git push origin master
git status
git remote add origin <server>
git remote -v
git checkout -b <branchname>
git checkout <branchname>
git branch
git branch -d <branchname>
git push --all origin

git diff
git diff --base <filename>
git diff <sourcebranch>
git log


#######################################################################################################
Basic functions
print() -> output stuff

input() -> get stuff FROM user

Variable Types
variable -> container to store information

string -> a piece of text (eg: "Mary had a little lamb")

integer -> number, no decimals (eg: 2017)

float -> number, decimals allowed (eg: 3.14)

char -> single character (eg: 'a', 'B', '1', etc.)

bool -> True or False
Basic arithmetics
+ -> addition; works with strings, but only combines them

- -> subtraction, does not work with strings

* -> multiplication, does not work with strings

/ -> division, does not work with strings

% -> modulo(find the remainder after division)
Conversion
str() -> convert to string

float() -> convert to float

int() -> convert to int

bool() -> convert to bool

#######################################################################################################
