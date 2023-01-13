from git_status_checker import GitStatusChecker
import os

#might need a mock
def test_local_git_7_days():
    git_status_checker = GitStatusChecker(os.getcwd())
    assert git_status_checker.check_last_commit_is_within_7_days(7)

def test_local_git_0_days():
    git_status_checker = GitStatusChecker(os.getcwd())
    assert not git_status_checker.check_last_commit_is_within_7_days(0)
