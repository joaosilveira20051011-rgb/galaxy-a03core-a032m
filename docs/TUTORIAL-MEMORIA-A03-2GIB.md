# Perfil permanente de memória — A03 Core SM-A032M S7

## Resultado confirmado em 13/10/2026
No aparelho de referência com crDroid 10.13 a64 Vanilla, kernel OC2 e Magisk 30.7, a leitura após reiniciar confirmou:

| Parâmetro | Valor |
|---|---|
| ZRAM lógica | 2147483648 bytes (2,0 GiB) |
| Compressão ativa | lzo-rle |
| swappiness | 70 |
| page-cluster | 1 |
| watermark_scale_factor | 5 |
| Swap | zram0 ativo; 2097148 KiB utilizáveis |

A diferença de 4 KiB entre o tamanho lógico e SwapTotal corresponde ao cabeçalho do swap. Os 2 GiB são capacidade lógica de páginas antes de compressão, não reserva fixa de 2 GiB de RAM.

Confirmado: criação do módulo, sintaxe do script, inicialização e valores após um reboot. Não medidos: ganhos de fluidez, FPS, autonomia ou estabilidade prolongada. Não se declara este perfil superior ao original.

## Como funciona
O vendor original ativa o swap por `/vendor/etc/init/init.ramplus.rc` em `sys.boot_completed=1`, usando `/vendor/etc/fstab.ramplus`.
Magisk sobrepõe apenas esse fstab, trocando o tamanho de 2684354560 para 2147483648 bytes. O service.sh espera boot completo, aguarda cinco segundos e aplica os três parâmetros VM. A espera tem limite de aproximadamente seis minutos.

Nenhum swapoff/reset é executado com Android em uso. Vendor físico, kernel, clocks, tensões, AVB e controles térmicos não são alterados. A compressão não é forçada pelo módulo: preserva lzo-rle do ambiente testado. Se outra ROM selecionar outro algoritmo, esta versão não garante lzo-rle.

## Requisitos e escopo
- SM-A032M com firmware A032MUBS7CZA5/S7, crDroid 10.13 e ambiente Magisk funcional correspondente ao projeto.
- PC Windows, platform-tools, curl e depuração USB autorizada.
- Outro aparelho/firmware/ROM exige auditoria própria; este módulo não foi validado em SM-A032F.
- Para quem já instalou este perfil pelo chat e confirmou os valores, não é necessário reinstalar.
- Confira outros módulos/scripts de memória: podem sobrescrever os parâmetros posteriormente.

## Downloads fixados
Versão dos arquivos: commit `b5d11dd17c598fb16d7b88ae599176313b5bf984`.
- [module.prop](https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/module.prop)
- [service.sh](https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/service.sh)
- [fstab.ramplus](https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/system/vendor/etc/fstab.ramplus)

Esta entrega disponibiliza arquivos e instalação por ADB. Não é um ZIP instalável pela interface do Magisk nem um novo asset da Release.

## Instalação pelo CMD
Abra CMD na pasta platform-tools. Execute cada linha separadamente. Não cole dentro de adb shell.

Identifique o aparelho:
```cmd
adb devices
set "A03_SERIAL=SERIAL_DO_SEU_A03"
adb -s %A03_SERIAL% shell getprop ro.product.vendor.model
adb -s %A03_SERIAL% shell getprop ro.bootloader
adb -s %A03_SERIAL% shell "su -c 'cat /vendor/etc/init/init.ramplus.rc; cat /vendor/etc/fstab.ramplus'"
```
Substitua o placeholder pelo serial local; não o publique. Confira modelo SM-A032M, bootloader A032MUBS7CZA5 e o mesmo gatilho/fstab acima. Se divergirem, pare e audite.

Baixe os três arquivos; se curl retornar erro, não prossiga:
```cmd
mkdir a03_memoria
mkdir a03_memoria\system\vendor\etc
curl.exe -fL "https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/module.prop" -o a03_memoria\module.prop
curl.exe -fL "https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/service.sh" -o a03_memoria\service.sh
curl.exe -fL "https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/b5d11dd17c598fb16d7b88ae599176313b5bf984/modules/a03_memoria/system/vendor/etc/fstab.ramplus" -o a03_memoria\system\vendor\etc\fstab.ramplus
type a03_memoria\module.prop
type a03_memoria\service.sh
type a03_memoria\system\vendor\etc\fstab.ramplus
```

Instale:
```cmd
adb -s %A03_SERIAL% push a03_memoria /data/local/tmp/
adb -s %A03_SERIAL% shell "su -c 'test ! -e /data/adb/modules/a03_memoria && mkdir -p /data/adb/modules && cp -R /data/local/tmp/a03_memoria /data/adb/modules/a03_memoria && chmod 0755 /data/adb/modules/a03_memoria /data/adb/modules/a03_memoria/system /data/adb/modules/a03_memoria/system/vendor /data/adb/modules/a03_memoria/system/vendor/etc /data/adb/modules/a03_memoria/service.sh && chmod 0644 /data/adb/modules/a03_memoria/module.prop /data/adb/modules/a03_memoria/system/vendor/etc/fstab.ramplus && sh -n /data/adb/modules/a03_memoria/service.sh && echo SCRIPT_OK'"
```
A instalação recusa sobrescrever um módulo existente. Só reinicie se aparecer SCRIPT_OK e os arquivos conferidos tiverem tamanho 2147483648 e parâmetros 70/1/5.
```cmd
adb -s %A03_SERIAL% reboot
```

## Conferência depois de reiniciar
Desbloqueie o aparelho, confira que adb devices mostra device e aguarde dez segundos após completar o boot:
```cmd
adb -s %A03_SERIAL% shell "su -c 'cat /sys/block/zram0/disksize; cat /sys/block/zram0/comp_algorithm; cat /proc/sys/vm/swappiness; cat /proc/sys/vm/page-cluster; cat /proc/sys/vm/watermark_scale_factor; cat /proc/swaps'"
```
Esperado: 2147483648; `lzo [lzo-rle] lz4 deflate`; 70; 1; 5; zram0 listado em /proc/swaps. Se não corresponder, instalação não está validada; não use swapoff/reset para forçar.

## Reversão
Desative A03 Core - Memoria 2GiB no Magisk e reinicie. Alternativa por CMD:
```cmd
adb -s %A03_SERIAL% shell "su -c 'touch /data/adb/modules/a03_memoria/disable'"
adb -s %A03_SERIAL% reboot
```
O fstab original reaparece e o script deixa de executar. No ambiente original auditado: ZRAM 2,5 GiB, swappiness 60, page-cluster 0, watermark_scale_factor 10. Outros ajustes persistentes podem mudar esses valores; confira após o reboot.

## Changelog
1.0: perfil solicitado pelo proprietário, aplicado via Magisk e confirmado após reinício no A03 de referência. Correção do transporte do script: o primeiro comando com aspas no CMD falhou; transferência por Base64 resolveu. Os arquivos publicados usam texto LF e dispensam esse problema de quoting.
