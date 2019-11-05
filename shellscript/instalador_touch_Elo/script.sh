#!/usr/bin/env bash
#######################
#vamos adcionar linha
#arquivos 
rc="/etc/rc.local"
rc_arquivo="arquivos/rc.local"
rc_service="/usr/lib/systemd/system/rc-local.service"
rc_service_arquivo="arquivos/rc-local.service"
lightdm_conf="/etc/lightdm/lightdm.conf"
lightdm_confi_arquivo="arquivos/lightdm.conf"
calibrate="/usr/bin/calibrate.sh"



################################################
#arquivos_teste
input_calibrator_test="arquivos/input_calibrator.texto"
input_calibrator.file=""

###############################################


set -x
#vamos ver se /etc/rc.local exite
if [ -e $rc ]
then
	echo "Os  arquivos nescessários já exitem "
else    
	sudo cp -rp $rc_arquivo > "/etc/rc.local"
	echo "Arquivo rc.local criado"
        
	# /etc/systemd/system/rc-local.sevice
	if [ -e $rc_service ]
	then 
		echo "O segundo arquivo nescessário já exite"
	else	
        
         	sudo cp -rp $rc_service > "/usr/lib/systemd/system/rc-local.service"
		echo "Arquivo rc-local.service criado"
	
	fi

fi
###############################################
echo "vamos  configurar o touch"
# contar o numero de linhas
#arquivo --> temos que colocar
# conteudo
conteudo="/usr/bin/inputattach --daemon --always --elotouch /dev/tty55"
# pegando nlinha
nlinha=$(sudo cat $rc | wc -l)
echo "o arquivo tem de linhas"
echo $nlinha
set -x
cat $rc
read

echo "pegar linha "
mlinha=$(($nlinha -1))
echo $mlinha


read
arquivo1="arquivo1"
arquivo2="arquivo2"
# acresentando uma linha
sudo cat  $rc > $arquivo1
echo $mlinhas
sed  "${mlinha} i  ${conteudo}" $arquivo1 > $arquivo2
rm $arquivo1
cat  $arquivo2
read
sudo mv $arquivo2  $rc
sudo chmod 755 $rc

#################################################
#/etc/lightdm/lightdm.conf

sudo cp -p $lightdm_confi_arquivo  $lightdm_conf
echo "precione quaquer tecla para continuar"
read

echo "instalando o touch"
sudo apt-get install inputattach
sudo inputattach --elotouch /dev/tty55 &
echo "precione quaquer tecla para continuar"
read
sudo apt-get install aptitude
sudo aptitude install xinput-calibrator
echo "calibrando touch"
sudo apt-get install xinput-calibrator
sudo xinput_calibrator --output-type xinput | tee $input_calibrator_test
echo "precione quaquer tecla para continuar"
read
################################################
clear
echo "precione quaquer tecla para continuar"
read
cat $input_calibrator_test
# gerando arquivos calibrate : /usr/bin/calibrate.sh
sudo echo "#!/usr/bin/env bash" > $calibrate
sudo cat $input_calibrator_test | grep "xinput" |grep "Evdev" >> $calibrate
sudo chmod 755 $calibrate
read
echo "vamos reniciar o sistema, click em alguma tecla para continuar"
read
set +x
#reboot

