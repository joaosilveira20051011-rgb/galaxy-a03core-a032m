# Galaxy A03 Core SM-A032M — crDroid e kernel próprio

Projeto experimental para SM-A032M, firmware **A032MUBS7CZA5 / bootloader S7**, SoC Unisoc SC9863A. O objetivo é documentar uma customização reproduzível, com fontes, patches, arquivos conferidos e resultados reais. Não se presume compatibilidade com SM-A032F, SM-A035, outros firmwares ou ROMs.

## Comece aqui

1. [Guia público e downloads](docs/GUIA-PUBLICO-A03CORE.md).
2. [Tutorial do kernel de referência](docs/TUTORIAL_A03CORE_STOCK_v0.1.txt).
3. [Tutorial do OC2 térmico](docs/TUTORIAL-OC2-THERMAL.md).
4. [Releases e arquivos efetivamente publicados](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases).

A imagem de boot dos pacotes preserva o **ramdisk com Magisk do aparelho de referência**. Kernel e root são coisas diferentes; estes boots não foram entregues como versão sem root.

## Estado atual — 13/10/2026

| Etapa | Resultado real |
|---|---|
| crDroid 10.13 a64 Vanilla / Android 14 | Instalado e iniciado pelo proprietário |
| Kernel de referência Samsung S7 recompilado | Inicialização confirmada; ZIP disponível na Release |
| OC1: CPU lenta 1,4 GHz / rápida 1,8 GHz / GPU 600 MHz | Boot e reinicialização confirmados; leitura do registrador GPLL 600 MHz documentada |
| AnTuTu informado pelo proprietário | Total 137059; CPU 46901, GPU 16145, MEM 47347, UX 26666; execução relatada normal |
| OC2: controle adicional pela placa | Compilação e boot confirmados; sensor válido; máximos CPU 1,4/1,8 GHz observados |
| Redução/liberação física do OC2 em 55/60 °C | Ainda não validada sob carga nos limites |
| Estabilidade prolongada / ganhos versus referência | Ainda não comprovados |
| Tuning de RAM/ZRAM/I/O | Planejado; nenhum módulo de tuning entregue |
| GApps | LiteGapps Core ARM Android 14 recomendado; funcionamento ainda não confirmado neste projeto |

O resultado AnTuTu é um relato de uma execução. Não demonstra ganho percentual de OC nem estabilidade prolongada.

## Downloads

- [Kernel de referência stock-baseline-v0.1](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/tag/stock-baseline-v0.1): contém ZIP e tutorial.
- OC1 e OC2: artefatos reais produzidos e entregues ao proprietário; **ainda aguardam anexação às Releases deste GitHub**. Não existem links públicos de download confirmados para eles nesta atualização.
- [GSI original crDroid 10.13 a64 Vanilla](https://github.com/naz664/crDroid_gsi/releases/download/v2025.03.08/crDroid-10.13-a64_bvN-Unofficial.img.xz), do mantenedor naz664.
- [LiteGapps Core ARM Android 14](https://downloads.sourceforge.net/project/litegapps/litegapps/arm/34/core/2026-10-01/LiteGapps-core-arm-14.0-20261001-official.zip): link corrigido e abertura do ZIP verificada; instalação/funcionamento no A03 não confirmados.

**a64 significa ARM32/Binder64**, não arm64. O sistema usa armeabi-v7a/armeabi; kernel AArch64 com COMPAT.

## OC2 térmico

| Sensor de referência | CPU | GPU |
|---|---|---|
| board-thmzone, termistor da placa | Limita a 1100/1500 MHz em >=55 °C; libera abaixo de 53 °C | Limita a 384 MHz em >=60 °C; libera abaixo de 58 °C |

As frequências máximas OC1 continuam disponíveis fora da limitação adicional. As proteções térmicas internas, tabelas quentes, bateria/carregamento e thermald foram preservados. board-thmzone não foi demonstrado equivalente ao quiet_therm do Redmi 8A Dual.

O status somente leitura está em /sys/kernel/a03core_thermal/status. A GPU recebe teto interno no devfreq; max_freq pode continuar mostrando 600 MHz. Frequência efetiva e atuação térmica precisam de teste físico.

## Código e evidências

- [Base oficial e toolchain](docs/kernel-base-oficial-s7.md).
- [Compilação OC1](docs/kernel-oc1-1800-1400-600-compilacao.md).
- [Patch OC1](kernel/patches/OC1-1800-1400-600.patch).
- [Patch OC2 completo](kernel/patches/OC2-board-thermal-55-60.patch).
- [Relatório OC2](docs/kernel-oc2-thermal-compilado-e-validacao.md).
- [Boot OC2 e auditoria da ROM](docs/kernel-oc2-boot-confirmado-auditoria-rom.md).
- [Checksums OC2](artifacts/oc2-thermal-sha256.json).
- [Primeiro AnTuTu OC1](docs/kernel-oc1-antutu-primeiro-resultado.md).

As fontes completas do kernel dependem da base Samsung identificada no relatório, da atualização S7 e dos patches. Este repositório contém configuração/scripts/patches; não confundir o ZIP automático “Source code” do GitHub com uma árvore completa pronta para compilar.

## GSI e recuperação

A GSI foi integrada em super preservando vendor/product/system_ext do ambiente auditado. Não foi publicado um instalador universal partindo do firmware original. Consulte [montagem de super](docs/montagem-super-crdroid-validada.md) e [script](scripts/montar-super-crdroid.sh).

O experimento antigo com flags de vbmeta provocou bootloop; a restauração do vbmeta original permitiu inicializar. **Esse experimento não é requisito nem receita de instalação.** Os kernels posteriores preservam o ambiente AVB já usado no projeto.

Não publicar serial, IMEI, credenciais, EFS/NV nem backups pessoais. O TAR de restauração fornecido pertence à referência; outro usuário deve conservar seu próprio backup compatível.

## Telegram

Grupo de suporte em preparação. O link ainda não foi informado para publicação. Não há confirmação de postagem no Telegram nesta atualização.

## Créditos

Samsung Open Source Release Center (base do kernel); naz664 (GSI crDroid); Magisk e LiteGapps (projetos respectivos). Resultados físicos informados pelo proprietário. Links de terceiros e compatibilidade devem ser conferidos antes de reproduzir o procedimento.
