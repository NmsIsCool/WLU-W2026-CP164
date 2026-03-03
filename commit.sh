
echo -n "Enter Commit Message:"
read commit_message

git status
git add .
git status

git commit -m commit_message
git push
