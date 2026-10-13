# LiteGapps Core ARM Android 14 — instalação no projeto A03 Core

## Pacote
Versão usada: LiteGapps Core ARM 14.0, v5.0, build 01/10/2026.
Download oficial: https://downloads.sourceforge.net/project/litegapps/litegapps/arm/34/core/2026-10-01/LiteGapps-core-arm-14.0-20261001-official.zip
Página de download: https://sourceforge.net/projects/litegapps/files/litegapps/arm/34/core/2026-10-01/

Tamanho: 96005180 bytes.
SHA-256: `ea09bdbbaccb3182920d45f0af05a19a3c70ee6b30843b9f74407d18fdd7da5f`.
Verificação de 13/10/2026: download completo, CRC ZIP aprovado, module.prop ARM/sdk34/Core/v5.0 conferido. O endereço de download pode passar por uma página de seleção de espelho: uma resposta HTTP 200 sozinha não prova que você baixou o ZIP.

## Compatibilidade e estado real
Ambiente: SM-A032M S7, crDroid 10.13 a64 Vanilla Android 14, Magisk 30.7.
A64 usa usuários ARM de 32 bits: escolher ARM, não ARM64.
Coleta do aparelho confirmou módulo `litegapps` v5.0 ativo e processos de Google Play Services/Play Store. Login, sincronização completa e compatibilidade de todos os serviços não foram auditados.
Não instalar por cima de outro pacote GApps ou microG. Se o módulo já está instalado no aparelho do projeto, não reinstale por este tutorial.

## Baixar, conferir e inspecionar pelo CMD
```cmd
curl.exe -fL "https://downloads.sourceforge.net/project/litegapps/litegapps/arm/34/core/2026-10-01/LiteGapps-core-arm-14.0-20261001-official.zip" -o "%USERPROFILE%\Downloads\LiteGapps-core-arm-14.0-20261001-official.zip"
certutil -hashfile "%USERPROFILE%\Downloads\LiteGapps-core-arm-14.0-20261001-official.zip" SHA256
"C:\Program Files\7-Zip\7z.exe" t "%USERPROFILE%\Downloads\LiteGapps-core-arm-14.0-20261001-official.zip"
```
Exigir o hash acima e Everything is Ok. Se foi baixado HTML ou o hash divergir, pare e use a página oficial de download; não instale.
Extração apenas para inspecionar — a instalação usa o ZIP intacto:
```cmd
"C:\Program Files\7-Zip\7z.exe" x "%USERPROFILE%\Downloads\LiteGapps-core-arm-14.0-20261001-official.zip" -o"%USERPROFILE%\Downloads\A03_LiteGapps_Inspecao"
type "%USERPROFILE%\Downloads\A03_LiteGapps_Inspecao\module.prop"
```
Não apague arquivos do sistema para liberar espaço ou contornar erro do instalador.

## Instalar como módulo Magisk
Na pasta platform-tools, substitua o serial pelo identificador local e confira a ABI/Android:
```cmd
adb devices
set "A03_SERIAL=SERIAL_DO_SEU_A03"
adb -s %A03_SERIAL% shell getprop ro.product.cpu.abilist
adb -s %A03_SERIAL% shell getprop ro.build.version.sdk
adb -s %A03_SERIAL% shell "su -c 'magisk -v; ls /data/adb/modules'"
adb -s %A03_SERIAL% push "%USERPROFILE%\Downloads\LiteGapps-core-arm-14.0-20261001-official.zip" /sdcard/Download/
```
Esperado: armeabi-v7a/armeabi, SDK34, Magisk funcional. Backup dos dados antes de instalar componentes de sistema.

1. Magisk > Módulos > Instalar do armazenamento.
2. Selecione o ZIP intacto em Download.
3. Use o modo systemless/Magisk. Não configure instalação em recovery/non-systemless nem overrides de instalação. A documentação oficial e o instalador deste pacote suportam o modo systemless.
4. Confira o log: sem abort/error e instalação identificada como systemless (Magisk Module). Guarde o log caso falhe.
5. Reinicie, desbloqueie e aguarde concluir a preparação dos apps.

Este tutorial não requer recovery personalizado, flash de super/vbmeta nem formatação.

## Verificar
```cmd
adb -s %A03_SERIAL% shell "su -c 'cat /data/adb/modules/litegapps/module.prop; ls -l /data/adb/modules/litegapps/disable'"
adb -s %A03_SERIAL% shell pm path com.google.android.gms
adb -s %A03_SERIAL% shell pm path com.android.vending
```
A ausência do arquivo disable é esperada em módulo ativo; o ls pode informar No such file. Presença de pacotes não prova funcionamento: abra a Play Store, teste login/download, notificações e sincronização, sem publicar contas ou logs com identificadores.

## Reversão
Conforme documentação do mantenedor: remova atualizações dos aplicativos Google pertinentes antes de remover o módulo. Magisk > Módulos > LiteGapps > Remover > reiniciar. Instalação não-systemless exige outro procedimento: não presumir que desativar um módulo reverte gravações feitas diretamente no sistema.

Em falha de boot atribuída ao módulo e com ADB/root acessíveis:
```cmd
adb -s %A03_SERIAL% shell "su -c 'touch /data/adb/modules/litegapps/disable'"
adb -s %A03_SERIAL% reboot
```
Sem ADB funcional, essa rota não está disponível; não gravar um vbmeta aleatório para resolver.

## Fontes primárias
- https://litegapps.github.io/doc/installation.html
- https://litegapps.github.io/doc/uninstall.html
- ZIP oficial, module.prop e customize.sh efetivamente inspecionados.
O mantenedor registra limitações do modo systemless, incluindo sincronização de contatos. Nenhuma porcentagem de funcionalidade foi validada neste A03.
