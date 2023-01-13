import sys
from git import NoSuchPathError

from git_status_checker import GitStatusChecker

try:
    git_dir = sys.argv[1]
    git_status_checker = GitStatusChecker(git_dir)
    git_status_checker.print_git_dir_report()
except IndexError:
    print("Argument is not provided")
except NoSuchPathError:
    print("Provided Git Dir is not a valid git directory")