import os
import re
from git import Repo

def find_string_in_file(repo, search_string):
    result = []
    
    for root, dirs, files in os.walk(repo.working_dir):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file is a text file (you can modify this condition based on your needs)
            if file_path.endswith(".txt") or file_path.endswith(".py"):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if re.search(search_string, content):
                        last_commit = repo.git.log('-n', '1', '--', file_path, format='%an')
                        result.append((file_path, last_commit.strip()))

    return result

def main():
    # Replace 'your_repo_path' with the path to your Git repository
    repo_path = 'your_repo_path'
    repo = Repo(repo_path)

    # Replace 'search_string' with the string you want to search for
    search_string = 'your_search_string'

    result = find_string_in_file(repo, search_string)

    if result:
        print(f"Files containing '{search_string}':")
        for file_path, last_commit_user in result:
            print(f"File: {file_path}, Last Commit by: {last_commit_user}")
    else:
        print(f"No files containing '{search_string}' found.")

if __name__ == "__main__":
    main()
