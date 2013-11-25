echo 'installing base packages (python, git, ssh)'
 
  pacman -S --noconfirm python2 git ssh
 
echo 'installing cosmos'
 
git clone git@github.com:vyscond/vyky.git
 
  tar -xf cosmos-master.tar.gz
 
  cd cosmos-master
 
  python2 setup.py install
 
echo 'installing vyky'
 
  git clone git@github.com:vyscond/vyky.git
 
  tar -xf vyky-master.tar.gz
 
  cd vyky-master
 
  python2 setup.py install
