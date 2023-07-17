sudo pip3 install -r requirements.txt
sudo cp services_medicines.conf /etc/supervisor/conf.d/
sudo cp services_medicines_nginx.conf /etc/nginx/sites-enabled/
sudo supervisorctl update
sudo systemctl restart nginx
sudo certbot --nginx -d medicines.services.ai.medsenger.ru
touch config.py