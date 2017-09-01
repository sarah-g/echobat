echo "installing sound config file..."
cp ./sound/.asoundrc ~/
echo "installing sound config file...complete"
echo ""

echo "installing echobat service..."
cp ./service/echobat.sh /usr/bin/
chmod +x /usr/bin/echobat.sh
cp ./service/echobat.service /etc/systemd/system/
systemctl enable echobat.service
systemctl daemon-reload
echo -e "installing echobat service...complete"
echo ""

systemctl start echobat

echo "***************************************"
echo "Setup Complete!"
echo "***************************************"