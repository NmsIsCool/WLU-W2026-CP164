
echo -n "Enter Commit Message:"
read commit_message

git status
git add .

read -p "Press enter to continue"

git status

git commit -m commit_message
git push
