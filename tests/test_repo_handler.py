import unittest
from scanner.repo_handler import clone_repo

class TestRepoHandler(unittest.TestCase):


  def test_clone(self):
    repo_url = "https://github.com/pallets/flask.git"
    path = clone_repo(repo_url)
    print(f"Repo cloned to: {path}")

if __name__ == "__main__":
  unittest.main()
  # Run the test
  test = TestRepoHandler()
  test.test_clone()
  
