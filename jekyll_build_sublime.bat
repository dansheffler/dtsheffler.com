CD C:\Users\dansh\Dropbox\dansheffler
call taggen.py
call jekyll build --config _config.yml,_config_win.yml --verbose
call bash -c "rsync -avzhe ssh --progress --delete ./_site/ dts@dansheffler.com:~/public_html"