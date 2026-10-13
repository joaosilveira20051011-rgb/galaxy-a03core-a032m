# OC2 térmico — tutorial de instalação e conferência

## Requisitos
SM-A032M com ambiente A032MUBS7CZA5/S7 compatível, bootloader desbloqueado, GSI crDroid 10.13 a64 Vanilla e rota de recuperação confirmada. Boot distribuído preserva Magisk da referência. Outras variantes/firmwares e sistema Samsung original não foram validados.

Download: [Releases do projeto](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases). O ZIP OC2 ainda aguarda anexação no momento desta documentação.

Arquivo: a03core-OC2-thermal-55-60-experimental.zip
SHA-256: 6889c22a7dd028cf455e445fec1ebfcc0b7b4eb66b823a09ce75f01977e35dda

## Conferir e extrair no Windows
Salvar o ZIP em Downloads. No CMD:

```cmd
certutil -hashfile "%USERPROFILE%\Downloads\a03core-OC2-thermal-55-60-experimental.zip" SHA256
mkdir "%USERPROFILE%\Downloads\A03_OC2"
tar -xf "%USERPROFILE%\Downloads\a03core-OC2-thermal-55-60-experimental.zip" -C "%USERPROFILE%\Downloads\A03_OC2"
tar -tf "%USERPROFILE%\Downloads\A03_OC2\a03core_OC2\AP_BOOT_OC2_THERMAL_EXPERIMENTAL.tar"
```

O hash deve coincidir. O TAR de instalação deve listar somente boot.img. Consulte SHA256SUMS.json dentro da pasta para conferir os arquivos individuais.

## Backup próprio
Para quem já tem root, na pasta platform-tools e com apenas o aparelho correto conectado:

```cmd
adb devices
adb shell "su -c 'dd if=/dev/block/by-name/boot of=/data/local/tmp/boot_antes_oc2.img bs=1048576'"
adb pull /data/local/tmp/boot_antes_oc2.img "%USERPROFILE%\Downloads\boot_antes_oc2.img"
certutil -hashfile "%USERPROFILE%\Downloads\boot_antes_oc2.img" SHA256
```

Leitura de boot, não gravação da partição. Conservar também dados pessoais fora do telefone. Preparar um TAR válido de restauração antes de gravar; renomear .img para .tar não funciona. O AP_RESTAURAR_OC1_FUNCIONAL.tar incluído restaura o OC1 da referência, não o estado anterior de qualquer usuário.

## Instalar
Com vários aparelhos, acrescentar -s SERIAL_DO_A03 ao adb, usando o identificador local.

```cmd
adb reboot download
```

Odin: aguardar ID:COM e selecionar em AP o arquivo AP_BOOT_OC2_THERMAL_EXPERIMENTAL.tar. BL, CP, CSC e USERDATA vazios. Re-Partition, Nand Erase e Flash Lock desmarcados. O proprietário usou Auto Reboot e F. Reset Time marcados. Não carregar PIT, DTBO, vbmeta, super ou firmware completo para este teste. Start, aguardar PASS e boot.

PASS confirma gravação, não inicialização. Se falhar o boot, restaurar o AP compatível previamente preparado. O proprietário recuperou Download Mode mantendo Power + Volume Menos continuamente; confirmar uma rota funcional no próprio aparelho antes do teste.

## Conferir boot e controlador
```cmd
adb shell getprop sys.boot_completed
adb shell "su -c 'cat /sys/kernel/a03core_thermal/status; uname -a; cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq; cat /sys/devices/system/cpu/cpufreq/policy4/scaling_max_freq; cat /sys/class/devfreq/60000000.gpu/cur_freq'"
adb shell "su -c 'dmesg'" > "%USERPROFILE%\Downloads\A03_OC2_Boot.txt" 2>&1
```

Esperado: sys.boot_completed=1, version=OC2, sensor_error=0. CPU limitada acima de 55 °C da placa a 1100/1500 MHz, liberada abaixo de 53 °C; GPU limitada acima de 60 °C a 384 MHz, liberada abaixo de 58 °C. Em sensor inválido, os tetos ficam ativos. Proteções originais continuam podendo limitar antes ou mais que o controlador adicional.

A GPU usa teto interno: max_freq pode continuar mostrando 600 MHz. Observar cur_freq sob carga; não confundir tabela/máximo com frequência efetiva.

## Estado observado
Boot confirmado pelo proprietário; numa coleta fria, máximos CPU 1400/1800 MHz e limites adicionais liberados. Acionamento/liberação física nos thresholds, estabilidade prolongada e ganho de FPS/autonomia ainda não comprovados. Nenhum tuning adicional instalado. Não provocar aquecimento artificial para testar.

[Relatório técnico](kernel-oc2-thermal-compilado-e-validacao.md) e [auditoria da ROM](kernel-oc2-boot-confirmado-auditoria-rom.md).
