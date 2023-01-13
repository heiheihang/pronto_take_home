from git import Repo
import os
from datetime import datetime, timedelta, timezone

blame_name = "Rufus"


class GitStatusChecker:
    def __init__(self, git_dir):
        self.repo = Repo(git_dir)
        self.head_commit = self.repo.head.commit

    def get_active_branch(self):
        return str(self.repo.head.ref)

    def check_local_changes(self):
        return self.repo.is_dirty()

    def check_last_commit_is_within_7_days(self, days):
        commit_date_time = self.head_commit.committed_datetime.replace(tzinfo=timezone.utc)
        current_date_time = datetime.now().replace(tzinfo=timezone.utc)
        return commit_date_time + timedelta(days=days) >= current_date_time

    def get_commit_author_name(self):
        return self.head_commit.author.name

    def author_name_is_not_to_blame(self):
        return self.get_commit_author_name() != blame_name
