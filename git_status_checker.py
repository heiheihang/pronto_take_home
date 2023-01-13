from git import Repo
import os


class GitStatusChecker:
    def __init__(self, git_dir):
        self.repo = Repo(git_dir)

    def get_active_branch(self):
        return str(self.repo.head.ref)

    def check_local_changes(self):
        return self.repo.is_dirty()
