echo 'Moon Server - build config'
echo 'Name' $1
echo 'Number'   $2

echo 'setting up Ssh Welcome Message'

echo 'Arch Linux ARM - Strawberry-Pi - '$1' Node' > /etc/issue

echo 'setting up Network'

echo "
Description='A basic static ethernet connection'
Interface=eth0
Connection=ethernet
IP=static
Address=('10.10.10."$2"/24' '6.6.6."$2"/24' '192.168.1.4/29')
SkipNoCarrier=yes
" > /etc/netctl/strawberry_node

echo 'refreshing network config'
netctl reenable strawberry_node

echo 'setting up moon.cfg'

echo '
{

    "name" : "'$1'" ,
    "ip"   : "6.6.6.'$2'",
    "port" : 666 ,
    "pid" : "/root/moon/pid" ,
    "stream" : 
    {
        "stdin" : "default" ,
        "stdout" : "/root/moon/moonserver.std" ,
        "stderr" : "/root/moon/moonserver.std" 
    }
    
    ,
    
    "directorys" : 
    {
        "applications"     : "/root/moon/apps" ,
        "application_profiles" : "/root/moon/app_profiles"
    }

}
' > /root/moon/moon.cfg

