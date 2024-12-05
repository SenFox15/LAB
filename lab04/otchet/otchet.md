1. echo -n "Zahar" 
2. touch ~/otchet/files/2.txt
   pwd > ~/otchet/files/2.txt
   whoami >> ~/otchet/files/2.txt
3. touch ~/otchet/files/3.txt
   ls -li > ~/otchet/files/3.txt 
4. touch ~/otchet/files/4.md
   touch ~/otchet/files/4.txt
   cat ~/otchet/files/4.txt 
   cat ~/otchet/files/4.txt > ~/otchet/files/4.md
5. chmod go -r ~/otchet/files/4.txt
6. chmod 775 ~/otchet/files/4.txt
7. mv ~/otchet/4.txt ~/otchet/files/4.txt 
   mv ~/otchet/4.md ~/otchet/files/4.md
8. sudo chown -c root ~/otchet/files/4.md
   ls -lR ~/otchet
9. sudo useradd -m test_user 
   sudo groupadd wheel   
   sudo usermod -g wheel test_user
   sudo chsh -s /bin/zsh test_user
10. sudo passwd test_user
11. yzhe v grype
12. cat /etc/passwd > ~/otchet/files/12.txt 
13. chmod a+w ~/otchet/files/12.txt
14. su -p test_user
15. whoami >> /home/rubashko/otchet/files/12.txt
    pwd >> /home/rubashko/otchet/files/12.txt
16. exit
17. sudo su 
18. whoami >> /home/rubashko/otchet/files/12.txt
    pwd >> /home/rubashko/otchet/files/12.txt
19. tail -n 2 ~/otchet/files/12.txt
20. sudo groupdel wheel
    sudo userdel -r test_user