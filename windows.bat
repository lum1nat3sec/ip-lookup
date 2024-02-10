@echo off
setlocal enabledelayedexpansion

rem Python'un en son sürümünü indir
echo Python'u indiriyor...
curl -O https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe

rem Python'u kur
echo Python'u kuruyor...
start /wait python-3.10.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

rem Gerekli modülleri yükle
echo Gerekli modülleri yüklüyor...
python -m pip install requests colorama

rem Temizleme
echo Temizleniyor...
del python-3.10.4-amd64.exe

echo Kurulum tamamlandı!
pause
