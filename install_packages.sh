echo '[installing base packages][python][git][cosmos][vyky]'
    
    pacman -S --noconfirm python2
    
    git clone https://github.com/vyscond/cosmos.git
    
    cd cosmos
    
    python2 setup.py install
    
    cd ..
    
    git clone https://github.com/vyscond/vyky.git
    
    cd vyky
    
    cd vyky-master
    
    python2 setup.py install
