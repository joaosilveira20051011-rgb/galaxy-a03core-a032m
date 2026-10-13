# OC1 histórico — instalação e recuperação
Destino testado: SM-A032M / A032MUBS7CZA5 S7, crDroid 10.13 a64 Vanilla, bootloader desbloqueado, ramdisk Magisk da referência.
CPU 1,4/1,8 GHz; GPU 600 MHz. OC1 é anterior ao controle adicional OC2 de placa 55/60 °C. Voltar ao OC1 remove esse controle adicional; não é atualização do OC2.

## Download disponível
O boot OC1 está no ZIP OC2 como **AP_RESTAURAR_OC1_FUNCIONAL.tar**:
https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/a03core-OC2-thermal-55-60-experimental.1.zip
SHA-256 do ZIP: `6889c22a7dd028cf455e445fec1ebfcc0b7b4eb66b823a09ce75f01977e35dda`.
A cópia de restauração foi conferida durante o empacotamento OC2 contra o AP OC1 funcional.

## Extrair e conferir pelo CMD
```cmd
curl.exe -fL "https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/a03core-OC2-thermal-55-60-experimental.1.zip" -o "%USERPROFILE%\Downloads\a03core-OC2.zip"
certutil -hashfile "%USERPROFILE%\Downloads\a03core-OC2.zip" SHA256
"C:\Program Files\7-Zip\7z.exe" t "%USERPROFILE%\Downloads\a03core-OC2.zip"
mkdir "%USERPROFILE%\Downloads\A03_OC1"
tar -xf "%USERPROFILE%\Downloads\a03core-OC2.zip" -C "%USERPROFILE%\Downloads\A03_OC1"
tar -tf "%USERPROFILE%\Downloads\A03_OC1\a03core_OC2\AP_RESTAURAR_OC1_FUNCIONAL.tar"
certutil -hashfile "%USERPROFILE%\Downloads\A03_OC1\a03core_OC2\AP_RESTAURAR_OC1_FUNCIONAL.tar" SHA256
```
O TAR contém somente boot.img. SHA-256 do AP OC1: `69063555ac2a21d7bea73cf55ddc184778420d5eabb137cd80b2d2f0e4556ce3`. Exigir correspondência antes de usar.

## Backup, instalação e reversão
Siga backup próprio e Download Mode do [tutorial OC2](TUTORIAL-OC2-THERMAL.md), selecionando **AP_RESTAURAR_OC1_FUNCIONAL.tar** em AP.
BL/CP/CSC/USERDATA vazios; Re-Partition/Nand Erase/Flash Lock desmarcados; sem PIT, DTBO ou vbmeta. Outros firmwares/variantes não foram validados.
Para voltar ao OC2, use AP_BOOT_OC2_THERMAL_EXPERIMENTAL.tar e siga o tutorial OC2. Para voltar ao estado anterior próprio, use seu backup compatível. Para voltar à referência sem OC, consulte [tutorial de referência](TUTORIAL_A03CORE_STOCK_v0.1.txt). Nenhum desses pacotes restaura dados de usuário.

## Verificar boot
```cmd
adb devices
set "A03_SERIAL=SERIAL_DO_SEU_A03"
adb -s %A03_SERIAL% shell getprop sys.boot_completed
adb -s %A03_SERIAL% shell "su -c 'uname -a; cat /sys/devices/system/cpu/cpufreq/policy0/scaling_available_frequencies; cat /sys/devices/system/cpu/cpufreq/policy4/scaling_available_frequencies; cat /sys/class/devfreq/60000000.gpu/available_frequencies'"
```
Boot e tabelas não comprovam clocks sustentados ou estabilidade prolongada. [Relatório OC1](kernel-oc1-1800-1400-600-compilacao.md), [boot/GPLL](kernel-oc1-gpll-confirmado-boot-completo.md) e [AnTuTu](kernel-oc1-antutu-primeiro-resultado.md).

## Arquivo histórico separado
O ZIP original a03core-OC1-1800-1400-600-experimental.zip existe no trabalho local, SHA-256 `04294cc06fe1e6dc14d93e5529061fd517a71f8748e3bcb3f29a1449d8fce5a2`, mas não foi anexado à Release. A tentativa de publicação desse ZIP no Telegram em 13/10/2026 falhou; não o declarar publicamente disponível com base na mensagem pendente. O download utilizável acima é o AP OC1 dentro do OC2.
