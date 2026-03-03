
echo -n "Enter Commit Message:"
read commit_message

git add .
git status

read -p "Press enter to continue"


git commit -m commit_message
git push
