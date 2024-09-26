CD C:\Users\daniel.sheffler\OneDrive\Website
CD C:\Users\Dan\OneDrive\Website
call taggen.py
call bundle exec jekyll build --config _config.yml
call C:\Windows\System32\bash.exe -c "rsync -avzhe ssh --delete ./_site/ dh_dts@vps49879.dreamhostps.com:~/dtsheffler.com"