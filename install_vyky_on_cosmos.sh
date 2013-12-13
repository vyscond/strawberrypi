if [ "@#" -lt 1 ]; then
    
    echo -e 'Wrong usage!\ninstall_vyky_on_cosmos.sh [absolute_moon_directory]'
    exit
fi

echo '[setup][copying .map file]'
cp `pwd`/strawberrypi/slave/vyky.map $1/moon/app_profiles

echo '[setup][copying app folder]'
cp -r `pwd`/strawberrypi/slave/vyky $1/moon/apps
