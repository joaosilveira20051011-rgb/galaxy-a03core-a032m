# OC1 histórico — instalação e recuperação
Pacote experimental anterior ao OC2. Destino testado: SM-A032M / A032MUBS7CZA5 S7, crDroid 10.13 a64 Vanilla, bootloader desbloqueado e ramdisk Magisk da referência.
CPU 1,4/1,8 GHz e GPU 600 MHz; não contém o controlador adicional OC2 de placa 55/60 °C. Não é a recomendação atual padrão.

## Download e integridade
Baixe `a03core-OC1-1800-1400-600-experimental.zip` no tópico [GSI e Downloads do Telegram](https://t.me/A03CoreBrasilGSIKernel/9).
SHA-256 do ZIP: `04294cc06fe1e6dc14d93e5529061fd517a71f8748e3bcb3f29a1449d8fce5a2`.
Não há asset OC1 separado na Release GitHub neste registro; o índice do GitHub aponta para o arquivo Telegram. O ZIP OC2 também inclui um AP que restaura o OC1.

## Conferir e extrair no CMD
```cmd
certutil -hashfile "%USERPROFILE%\Downloads\a03core-OC1-1800-1400-600-experimental.zip" SHA256
"C:\Program Files\7-Zip\7z.exe" t "%USERPROFILE%\Downloads\a03core-OC1-1800-1400-600-experimental.zip"
mkdir "%USERPROFILE%\Downloads\A03_OC1"
tar -xf "%USERPROFILE%\Downloads\a03core-OC1-1800-1400-600-experimental.zip" -C "%USERPROFILE%\Downloads\A03_OC1"
tar -tf "%USERPROFILE%\Downloads\A03_OC1\a03core-OC1\AP_BOOT_OC1_1800_1400_600_EXPERIMENTAL.tar"
certutil -hashfile "%USERPROFILE%\Downloads\A03_OC1\a03core-OC1\AP_BOOT_OC1_1800_1400_600_EXPERIMENTAL.tar" SHA256
```
O TAR deve conter somente boot.img. SHA-256 do AP: `69063555ac2a21d7bea73cf55ddc184778420d5eabb137cd80b2d2f0e4556ce3`.
O ZIP inclui verificar.ps1 e SHA256SUMS.json. Não confundir DTB de inspeção com arquivo a gravar.

## Backup e instalação
Siga os requisitos, backup próprio e rota de Download Mode do [tutorial OC2](TUTORIAL-OC2-THERMAL.md), mas selecione **AP_BOOT_OC1_1800_1400_600_EXPERIMENTAL.tar** em AP.
BL/CP/CSC/USERDATA vazios; Re-Partition/Nand Erase/Flash Lock desmarcados; sem PIT e sem vbmeta. Não instalar este boot em variante/firmware diferente.
A instalação não é atualização automática do OC2: substitui seu kernel pelo OC1, retirando o controle térmico adicional OC2.

## Recuperação
O pacote inclui AP_RESTAURAR_BASELINE_FUNCIONAL.tar da referência (kernel recompilado sem OC, com Magisk). SHA-256: `41a70b135b5217b4ba6373439c900a19be5c7df59aab8ccbf37918affcec946f`.
Conserve seu próprio boot e TAR compatível: essa restauração não reproduz o estado anterior de qualquer aparelho.

## Verificar após boot
Na pasta platform-tools:
```cmd
adb devices
set "A03_SERIAL=SERIAL_DO_SEU_A03"
adb -s %A03_SERIAL% shell getprop sys.boot_completed
adb -s %A03_SERIAL% shell "su -c 'uname -a; cat /sys/devices/system/cpu/cpufreq/policy0/scaling_available_frequencies; cat /sys/devices/system/cpu/cpufreq/policy4/scaling_available_frequencies; cat /sys/class/devfreq/60000000.gpu/available_frequencies'"
```
Boot e tabela não comprovam clocks sustentados. [Relatório OC1](kernel-oc1-1800-1400-600-compilacao.md), [boot/GPLL](kernel-oc1-gpll-confirmado-boot-completo.md) e [AnTuTu](kernel-oc1-antutu-primeiro-resultado.md).
