from git_status_checker import GitStatusChecker
import os


def test_local_git():
    git_status_checker = GitStatusChecker(os.getcwd())
    assert git_status_checker.check_local_changes()
