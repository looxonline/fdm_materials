from git import Repo, InvalidGitRepositoryError


class GitHubConnector:
    """
    Responsible for retrieving the lates source from a GitHub project.
    Only check's out (forced) the master branch.
    """

    def __init__(self, working_dir, github_url):
        self.__working_dir = working_dir
        self.__github_url = github_url

    def getSourceFiles(self):
        """
        Connects to GitHub, clones the project if not already available, then checks out the master branch.
        """
        # Try to load the existing repository. If that fails, clone the repo instead.
        try:
            repo = Repo(self.__working_dir)
        except InvalidGitRepositoryError:
            repo = Repo.clone_from(self.__github_url, self.__working_dir)

        repo.heads.master.checkout(True)  # forced
        del repo  # see 'Limitations: Leakage of System Resources' in GitPythin documentation.
