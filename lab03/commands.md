2. tree -d -L 2 ~
3. cd /etc/
4. ls -a
    cd ..
5. ls -ls --sort='extension'
6. mkdir structure
7. mkdir -p {2018..2023}/{files,pictures,.passwords}
    ls -a structure/2019
    cd structure
8. touch {2018..2023}/files/data.md 
9. touch {2018..2023}/pictures/picture.png
10. touch {2018..2023}/.passwords/.passwords.txt
11. touch -a -t 202401010000 {2018..2023}/files/data.md
    ls -lu 2018/files
12. touch -m -t 201810060000 2018/.passwords/.passwords.txt     
    touch -m -t 201910060000 2019/.passwords/.passwords.txt     
    touch -m -t 202010060000 2020/.passwords/.passwords.txt
    touch -m -t 202110060000 2021/.passwords/.passwords.txt
    touch -m -t 202210060000 2022/.passwords/.passwords.txt
    touch -m -t 202310060000 2023/.passwords/.passwords.txt
13. cp -r structure/2023/{files,pictures,.passwords} Downloads/2025
14. touch -m -t 202510060000 2025/.passwords/.passwords.txt 
15. cp -r Downloads/2025 structure 
16. mv -n 2025/ 2024/ 
17. mv -n 2018/pictures/picture.png 2018/pictures/image.png 
    mv -n 2019/pictures/picture.png 2019/pictures/image.png 
    mv -n 2020/pictures/picture.png 2020/pictures/image.png 
    mv -n 2021/pictures/picture.png 2021/pictures/image.png 
    mv -n 2022/pictures/picture.png 2022/pictures/image.png 
    mv -n 2023/pictures/picture.png 2023/pictures/image.png 
    mv -n 2024/pictures/picture.png 2024/pictures/image.png 
18. mv 2018/ ~/Documents
    mv 2024/ ~/Documents
19. rmdir ~/Documents/2024/ 
20. rm -r ~/Documents/2024     
21. cat >> ~/structure/2019/files/data.md 
22. nano ~/structure/2020/files/data.md
23. code ~/structure/2021/files/data.md
24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md  
25. mkdir -p ~/structure/{soft_links,hard_links}
26. ln -s ~/structure/2019 ~/structure/soft_links/2019     
    ln -s ~/structure/2020 ~/structure/soft_links/2020
    ln -s ~/structure/2021 ~/structure/soft_links/2021
    ln -s ~/structure/2022 ~/structure/soft_links/2022
    ln -s ~/structure/2023 ~/structure/soft_links/2023
27. ln ~/structure/2020/files/data.md ~/structure/hard_links 
    ln ~/structure/2021/.passwords/.passwords.txt ~/structure/hard_links 
28. mkdir ~/structure/archives
30. mv ~/Downloads/image.jpg ~/structure/archives 
31. tar -c -f ~/structure/archives/image.tar ~/structure/archives/image.jpg
    tar -c -f ~/structure/archives/image.tar.gz ~/structure/archives/image.jpg 
    tar -c -f ~/structure/archives/image.tar.bz2 ~/structure/archives/image.jpg
32. zip -er structure.zip ~/structure/