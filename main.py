from scanner import python_scanner, repo_handler, report_generator

def main():
  repo_url = input("Enter the repository URL: ")
  repo_path = repo_handler.clone_repo(repo_url)
  deprecated_items = python_scanner.scan_repo(repo_path)
  report_generator.generate_report(deprecated_items)
  

if __name__ == "__main__":
  main()
  