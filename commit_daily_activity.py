# import os
# from github import Github
# from datetime import datetime

# # Your GitHub username and repository name
# github_username = "abaabak"
# repo_name = "--"

# # Your GitHub access token
# github_token = "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"

# try:
#     # Create GitHub object
#     g = Github(github_token)

#     # Get repository
#     repo = g.get_user(github_username).get_repo(repo_name)

#     # Generate file name for today's activity
#     file_name = "test.txt"

#     # Get current time
#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Read existing file content
#     try:
#         contents = repo.get_contents(file_name)
#         existing_content = contents.decoded_content.decode("utf-8")
#     except Exception as e:
#         print(f"The file {file_name} doesn't exist yet. Creating a new file.")
#         existing_content = ""

#     # Update content with current time
#     updated_content = existing_content + f"\n{current_time}"

#     # Write updated content to file
#     with open(file_name, 'w') as file:
#         file.write(updated_content)

#     # Commit the changes to GitHub
#     repo.update_file(contents.path, f"Updating daily activity file {file_name}", updated_content, contents.sha)
#     print(f"Daily activity updated in {repo_name} repository.")

# except Exception as e:
#     print(f"An error occurred: {e}")
#     print("Please ensure the following:")
#     print("- Your GitHub username and repository name are correct.")
#     print("- Your GitHub token has the necessary permissions.")
#     print("- The repository exists under your GitHub account.")
#     print("- You have not reached any GitHub API rate limits.")
#     print("If the problem persists, please double-check your GitHub settings and try again.")

import os
from github import Github
from datetime import datetime

# 定义变量
multiple = 1

def check_if_multiple_of_three():
    # 获取当前日期
    current_date = datetime.now().day
    # 检查日期是否为的倍数
    if current_date % multiple == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    if check_if_multiple_of_three():
        print(f"当前日期是{multiple}的倍数。")
        # 这里可以放置您原来的批处理脚本的内容
        
        # 您的 GitHub 用户名和仓库名称
        github_username = "abaabak"
        repo_name = "--"

        # 您的 GitHub 访问令牌
        github_token = ""

        try:
            # 创建 GitHub 对象
            g = Github(github_token)

            # 获取仓库
            repo = g.get_user(github_username).get_repo(repo_name)

            # 生成今天活动的文件名
            file_name = "test.txt"

            # 获取当前时间
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 读取现有文件内容
            try:
                contents = repo.get_contents(file_name)
                existing_content = contents.decoded_content.decode("utf-8")
            except Exception as e:
                print(f"文件 {file_name} 尚不存在。创建新文件。")
                existing_content = ""

                # 创建新文件
                repo.create_file(file_name, f"Committing daily activity file {file_name}", current_time)
                print(f"已创建新文件 {file_name}。")

            # 更新内容，添加当前时间
            updated_content = existing_content + f"\n{current_time}"

            # 将更新后的内容写入文件
            with open(file_name, 'w') as file:
                file.write(updated_content)

            # 提交更改到 GitHub
            repo.update_file(contents.path, f"更新每日活动文件 {file_name}", updated_content, contents.sha)
            print(f"每日活动已更新到 {repo_name} 仓库。")

        except Exception as e:
            print(f"发生错误：{e}")
            print("请确保以下内容：")
            print("- 您的 GitHub 用户名和仓库名称是否正确。")
            print("- 您的 GitHub 令牌具有必要的权限。")
            print("- 仓库存在于您的 GitHub 帐户下。")
            print("- 您尚未达到任何 GitHub API 的使用限制。")
            print("如果问题仍然存在，请仔细检查您的 GitHub 设置并重试。")

        print("脚本执行完毕。")

    else:
        print(f"当前日期不是{multiple}的倍数。不允许执行脚本。")
