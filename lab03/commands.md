tree -d */ -L 2 ~
cd /etc/
ls -a
cd
ls -ls --sort='extension'
mkdir -p structure/{2018..2023}/{files,pictures,.passwords}
ls -a structure
touch {2018..2023}/files/data.md
touch {2018..2023}/pictures/picture.png
touch {2018..2023}/.passwords/.passwords.txt


touch -a -t 202401010000 {2018..2023}/files/data.md
ls -lu 2018/files
touch -m -t 201810060000 2018/.passwords/.passwords.txt
touch -m -t 201910060000 2019/.passwords/.passwords.txt
touch -m -t 202010060000 2020/.passwords/.passwords.txt
touch -m -t 202110060000 2021/.passwords/.passwords.txt
touch -m -t 202210060000 2022/.passwords/.passwords.txt
touch -m -t 202310060000 2023/.passwords/.passwords.txt

cp -r structure/2023/{files,pictures,.passwords} Downloads/2025
touch -m -t 202510060000 2025/.passwords/.passwords.txt 
cp -r Downloads/2025 structure 
mv -n 2025/ 2024/
mv -n 2018/pictures/picture.png 2018/pictures/image.png 
mv -n 2019/pictures/picture.png 2019/pictures/image.png 
mv -n 2020/pictures/picture.png 2020/pictures/image.png 
mv -n 2021/pictures/picture.png 2021/pictures/image.png 
mv -n 2022/pictures/picture.png 2022/pictures/image.png 
mv -n 2023/pictures/picture.png 2023/pictures/image.png 
mv -n 2024/pictures/picture.png 2024/pictures/image.png
