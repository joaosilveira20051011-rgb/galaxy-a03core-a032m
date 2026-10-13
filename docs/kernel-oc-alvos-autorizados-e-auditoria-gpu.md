# OC solicitado: autorização e bloqueios técnicos
Data: 2026-10-13.
O proprietário rejeitou o ensaio intermediário de 1,7 GHz e autorizou corrigir tensões, mantendo exclusivamente os alvos CPU rápida 1,8 GHz, CPU lenta 1,4 GHz e GPU 600 MHz. Esta autorização não abrange flash. Estimativas anteriores de tensão não são requisitos.

## Auditoria executada
Base oficial A032M S7 Linux 4.14.199 já recompilada e inicializada como referência. Fontes locais examinadas:
- arch/arm64/boot/dts/sprd/sc9863a.dtsi: CPU lenta bin2 e rápida/SCU bin1, tabelas normais e quentes.
- drivers/cpufreq/sprd-hwdvfs-sharkl3.c: codificação MPLL até 2 GHz, mudança de ibias em 1,8 GHz; índices conjuntos CPU rápida/SCU; caminhos de transição assíncrona.
- drivers/cpufreq/sprd-cpufreq-common.c e sprd-cpufreqhw.c: seleção por bin/temperatura, política e inclusão de OPP.
- arch/arm64/boot/dts/sprd/sharkl3.dtsi: GPU operating-points e sprd,dvfs-lists, topo <550000 0 9 1>.
- drivers/clk/sprd/sc9863a-clk.c: GPU core/soc com pais TWPLL e GPLL programável.
- DTB real e overlays extraídos: confrontados com a base.

## Bloqueio específico da GPU
O controlador PowerVR/rogue específico não foi localizado na árvore oficial nem no espelho local. O DTS inclui índice e divisor, não apenas uma frequência. A alimentação GPU aparece como zero nas tabelas: isso não significa tensão física zero nem permite prescrever +25 mV.
Não há evidência suficiente de que apenas alterar 550000 para 600000 programe GPLL em 600 MHz.
Consultadas também árvores públicas SC9863A de Hadenix e shoulewoba, e repositórios externos GPU Motorola e jingpad-bsp. Os resultados examinados não forneceram o driver exato do Samsung. Não substituir por módulo de outro fabricante.

Próxima evidência necessária: módulos originais de /odm/lib/modules do aparelho para identificar pvrsrvkm/PowerVR, símbolos, interfaces e programação de clock do driver efetivamente em uso. Não publicar esses binários automaticamente.
Depois: definir patch real de GPU e a interação com alimentação, revisar índices/SCU e tratamento de erros, estabelecer tensões experimentais documentadas, compilar e auditar módulos/DTB/boot.
Nenhum artefato OC foi produzido ou considerado instalável nesta etapa. Clocks normais e proteções permanecem preservados na referência.
