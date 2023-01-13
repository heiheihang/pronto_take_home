from git_status_checker import GitStatusChecker
import os


#need to add a mock for get_commit_author_name
def test_blame_name():
    git_status_checker = GitStatusChecker(os.getcwd())
    assert git_status_checker.author_name_is_not_to_blame()
