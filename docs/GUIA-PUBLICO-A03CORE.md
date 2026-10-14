# Guia público do projeto A03 Core

**[Central atual de downloads, tutoriais, hashes e recuperação](CENTRAL-DOWNLOADS-E-INSTALACOES.md)**. Inclui GSI anexada à Release, perfil de memória confirmado e tutorial de LiteGapps.

## Destino confirmado
SM-A032M / A032MUBS7CZA5 (S7), crDroid 10.13 Android 14 a64 Vanilla. Conferir vendor e bootloader por ADB; o modelo mostrado pela GSI pode diferir.

```cmd
adb devices
adb shell getprop ro.product.vendor.model
adb shell getprop ro.bootloader
adb shell getprop ro.product.cpu.abilist
```

Com vários aparelhos, usar adb -s SERIAL_DO_A03 em cada comando, substituindo o placeholder pelo identificador local. Não publicar esse identificador.

## Downloads e caminhos
| Componente | Onde obter | Estado |
|---|---|---|
| Kernel referência | [Release stock-baseline-v0.1](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/tag/stock-baseline-v0.1) | ZIP publicado, boot confirmado |
| OC1 | [Lista de Releases](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases) | AP OC1 disponível dentro do ZIP OC2; [tutorial](TUTORIAL-OC1-HISTORICO.md) |
| OC2 térmico | [Download ZIP](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/a03core-OC2-thermal-55-60-experimental.1.zip) | Publicado; boot confirmado; validação térmica prolongada pendente |
| GSI | [Release naz664](https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08) | Usar crDroid-10.13-a64_bvN-Unofficial.img.xz |
| Platform-tools | [Android Developers](https://developer.android.com/tools/releases/platform-tools) | Ferramentas ADB para Windows |
| 7-Zip | [Site oficial](https://www.7-zip.org/) | Extração de .xz |
| GApps opcional | [LiteGapps Core ARM14](https://downloads.sourceforge.net/project/litegapps/litegapps/arm/34/core/2026-10-01/LiteGapps-core-arm-14.0-20261001-official.zip) | Módulo e processos presentes; [tutorial de instalação e reversão](TUTORIAL-GAPPS-LITEGAPPS-ARM14.md) |

Link da Release de referência: https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/tag/stock-baseline-v0.1 (usar esta URL absoluta se o link relativo acima não abrir).

## Sequência de leitura

**[Instalação da GSI com bootloader desbloqueado](TUTORIAL-GSI-BOOTLOADER-DESBLOQUEADO.md)**: procedimento detalhado para o ambiente correspondente, com backup próprio, preparação e recuperação. A rota documentada requer root para extração; divergências de firmware/partições exigem análise.
1. [Tutorial de referência](TUTORIAL_A03CORE_STOCK_v0.1.txt): requisitos, backup, Odin e recuperação.
2. [GSI e super](montagem-super-crdroid-validada.md): integração usada, hashes e dependências.
3. [Tutorial OC2](TUTORIAL-OC2-THERMAL.md): instalação de boot no ambiente correspondente e diagnóstico.
4. [Resultados OC2](kernel-oc2-boot-confirmado-auditoria-rom.md): o que foi observado e o que falta testar.

Não existe nesta entrega um guia integral validado para partir de qualquer firmware original, desbloquear e instalar uma super universal. O tutorial de kernel pressupõe ambiente compatível previamente preparado. Não gravar a GSI bruta no Odin nem usar fastboot flash system por analogia.

Os pacotes preservam o ramdisk Magisk do aparelho de referência; não há imagem sem root validada. Os TARs de restauração incluídos não substituem backup próprio de outro usuário.

## Distribuição
Manter os pacotes na Release existente, conforme decisão do responsável; não criar outra Release apenas para este índice. Manter checksums e informar o estado de validação. Uma Release OC2 não deve ser chamada estável com base apenas em boot. Nenhum ganho percentual foi demonstrado.

## Suporte
Informar modelo/vendor, firmware, ROM, versão do pacote, erro exato e logs sanitizados. Remover serial/IMEI/contas antes de publicar. Não enviar EFS, NV ou credenciais.

Telegram: https://t.me/A03CoreBrasilGSIKernel/1
