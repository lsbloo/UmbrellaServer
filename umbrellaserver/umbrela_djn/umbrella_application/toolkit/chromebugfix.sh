#!/bin/bash
	#-> correção de bug instagramPy causado pela lib Chrome driver;
	#-> Como usar? -> copie e cole esse arquivo dentro de uma pasta qualquer fora do projeto
	#-> vai ser criado um diretorio chamado bugfix, com a atualização do driver baixada
	#-> depois disso é so colar o arquivo na pasta assets do instapy e da permissao de execução
	#-> caso o script nao consiga encontrar o caminho especificado acima.

function getDeb(){
	cd 
	mkdir bugfix
	cd bugfix/
	wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
	sudo dpkg -i google-chrome-stable_current_amd64.deb
	sudo apt-get install -y -f
}
function getInstPy(){
	git clone https://github.com/timgrossmann/InstaPy.git
	ultima_versao= $(wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O)
	wget https://chromedriver.storage.googleapis.com/${ultima_versao}/chromedriver_linux64.zip
	unzip chromedriver_linux64
	mv chromedriver InstaPy/assets/chromedriver
	chmod 755 InstaPy/assets/chromedriver
}


getDeb()
getInstPy()
