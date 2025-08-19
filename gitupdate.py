from github import Github
import pandas as pd
import json

with open("my_token.json", "r") as f:
    data = json.load(f)
    github_token = data["github_token"]


g = Github(github_token)
repo = g.get_repo("nzelinska-job/Streamlit")

# Путь до файлу у repo
file_path = "data/global_development_data.csv"
file_content = repo.get_contents(file_path)
sha = file_content.sha

# Завантаження CSV
url = "https://raw.githubusercontent.com/nzelinska/Streamlit/refs/heads/main/data/global_development_data.csv"
df = pd.read_csv(url)

# Оновлення df після редагування в Streamlit (припустимо, у вас є новий DataFrame updated_df)
updated_csv = updated_df.to_csv(index=False)

# Завантаження оновленого файлу
repo.update_file(file_path, "Update CSV via Streamlit app", updated_csv, sha)
