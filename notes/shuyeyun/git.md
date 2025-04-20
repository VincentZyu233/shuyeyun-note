## 从大到小 看文件
git ls-files | xargs -d '\n' du -h | sort -hr


git rev-list --objects --all | sort -k 2 | uniq -c | sort -nr | head -n 20
