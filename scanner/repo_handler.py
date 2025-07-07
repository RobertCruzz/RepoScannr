from git import Repo
import os
from urllib.parse import urlparse



#Clone a repo if not present
#pull changes if already cloned
def clone_repo(repo_url, local_path='repo'):
    from git import Repo
    import os

    if not os.path.exists(local_path):
        print(f"Cloning repository from {repo_url} to {local_path}...")
        Repo.clone_from(repo_url, local_path)
    else:
        print(f"Repository already exists at {local_path}. Pulling latest changes...")
        repo = Repo(local_path)
        repo.remotes.origin.pull()

    return local_path
  
# Function to extract the repository name from the URL
def get_repo_name(repo_url):
  try:
      parsed_url = urlparse(repo_url)
      repo_name = os.path.basename(parsed_url.path)
    
      if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]  # Remove the .git suffix if present
      if not repo_name:
        raise ValueError("Repository name could not be determined from the URL.")
  except Exception as e:
      print(f"Error extracting repository name: {e}")
      repo_name = "unknown_repo"  
      
      
  return repo_name