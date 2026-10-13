# Kernel de referência stock: execução física confirmada

Evidência: captura de CMD enviada pelo proprietário em 2026-10-13, após Odin PASS com AP_BOOT_STOCK_RECOMPILADO_TESTE.tar. Não foi um teste USB executado diretamente pelo assistente.

## Confirmado pela saída
- ADB: estado device (identificador pessoal omitido).
- /proc/version: Linux4.14.199-27418755-abA032MUBS7CZA5, compilador Android6443078/r383902 clang11.0.1, identificação root@02bf778456de, build#1 SMP PREEMPT Tue Oct13 09:55:43 PDT2026. A identificação distingue a recompilação do kernel Samsung anterior dpi@SWDMC214/build#2/dataJan15.
- uname -a: release correspondente e armv8l. Este campo reflete o ambiente compat32; o binário foi verificado AArch64 no build.
- su -c id: uid0/root, contexto u:r:magisk:s0. Root preservado.
- lsmod mostra módulos carregados: sprdwl_ng, sprdbt_tty, pvrsrvkm, sprd_camera, sprd_sensor, incrementalfs e outros módulos de flash/touch. A lista inclui módulos além dos cinco encontrados anteriormente em /vendor/lib/modules; não alegar que a análise estática anterior cobria todos os módulos do aparelho.

## Limites
Carregamento de módulo não comprova funcionamento completo de WiFi, Bluetooth, GPU, câmeras ou sensores. ADB e kernel em execução confirmados; tela inicial/boot_completed, novo reboot, suspensão, testes funcionais e estabilidade prolongada ainda precisam de confirmação. Nenhum OC ou tensão personalizada aplicado.

Próximo: confirmar sys.boot_completed, uso básico e nova inicialização; depois auditar binning, OPP, reguladores e clocks para a especificação experimental1,8/1,4GHz CPU e600MHz GPU.

[Compilação e pacote](kernel-stock-compilado-2026-10-13.md)
