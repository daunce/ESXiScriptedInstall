while IFS=, read hostname MAC IP SUBNETMASK GATEWAY
do
    echo "I got:$read $hostname $MAC $IP $SUBNETMASK $GATEWAY"
done < file.csv
