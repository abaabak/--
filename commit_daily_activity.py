import os
from github import Github
from datetime import datetime, timedelta

# 你的GitHub用户名和仓库名称
github_username = "abaabak"
repo_name = "huoyue"

# 你的GitHub访问令牌
github_token = "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"

# 创建GitHub对象
g = Github(github_token)

# 获取仓库
repo = g.get_user(github_username).get_repo(repo_name)

# 生成每天提交的文件名（可以根据需要修改）
file_name = f"activity_{datetime.now().strftime('%Y-%m-%d')}.txt"

# 创建一个空文件
with open(file_name, 'w') as file:
    file.write("")

# 提交文件到GitHub
repo.create_file(file_name, f"Committing daily activity file {file_name}", "")

# 删除本地文件
os.remove(file_name)

print(f"Daily activity committed to {repo_name} repository.")

# 生成每天提交的文件名（可以根据需要修改）