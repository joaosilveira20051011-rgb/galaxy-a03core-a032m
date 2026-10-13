# Investigação de tensão e OC: fonte oficial e imagens reais

## Confirmado por inspeção
Base oficial Samsung S7 previamente obtida/CRCvalidado. Linux4.14.199, CONFIG_ARM_SPRD_HW_CPUFREQ_SHARKL3=y. Inspeção sprd-hwdvfs-sharkl3.c: hwdvfs_mpll_table calcula postdiv/ibias/KN até VCO2000000kHz, inclusive branch>=1800000; isto permite codificar1,8GHz, não comprova estabilidade no chip. O driver comporta8 entradas de freq/volt e aciona cluster1+SCU pelo mesmo índice.

DTB original extraído do boot: contêiner Samsung com64bytes de cabeçalho antes do FDT. DTS decodificado corresponde aos OPPs e nvmem já inspecionados. DTBO original tem4 entradas; todas confirmam dcdc-controller0 reg<0 0>, ADI e dcdc-controller1 reg<1 2>, I2C. Mapeamento do overlay: cluster0->controller1; cluster1 eDSU->controller0. DTBO não alterado nesta investigação.

Tabela interna DCDC5355: mínimo603000uV, passo12826uV; conversão DIV_ROUND_UP. Cluster lento request1,10V codifica1,103214V; request1,125V codifica1,128866V. A tabela quente original1,121875V também codifica1,128866V. Valores decodificados do modelo do driver, não medição física nem garantia de identificação/calibração do CI. Overlay declara regulador externo fcs,fan53555.

Tabela interna do caminho PMICADI: mínimo400000uV, passo3125uV. Valores1,05/1,075/1,10V são representáveis. PMICbasecompatibleSC2721; nome interno do índice driver éDCDC2731_VOL0, não deve ser usado para inferir que o PMIC físico sejaSC2731.

Cluster rápido/SCU compartilham alimentação e sincronização de índices. O binCPU foi lido0x12 (cluster0bin2, cluster1bin1); binDSU ainda falta. Portanto1,05V do OPP daCPU rápida não pode ser tratado como tensão medida/exclusiva do rail. A leitura do binDSU é necessária antes de especificar como alterar sua tabela e manter coerência.

## Pesquisa pública e limites
Consultadas buscas em inglês, russo e chinês para SC9863A/a3core OC/undervolt/tensão, além de código strongtz/linux-sprd, suporte upstream SC9863A a clocks e documentação LinuxOPP. Não foi localizado nessa investigação um resultado reproduzível S7 com tensão mínima validada para1,8GHzCPU/600MHzGPU. Ocorrências em fóruns e projetos runtime de outro kernel/aparelho não comprovam compatibilidade. Algumas páginas rawGitHub falharam no navegador de busca; fonte oficial local foi usada para os detalhes do driver. Não houve acesso a grupos privados nem cobertura de toda a internet.

Fontes públicas:
https://github.com/strongtz/linux-sprd/blob/main/arch/arm64/boot/dts/sprd/sc9863a.dtsi
https://github.com/IverCoder/android_kernel_samsung_a3core/tree/stock
https://docs.kernel.org/power/opp.html
https://opensource.samsung.com/uploadSearch?searchValue=SM-A032M

## Decisão
Ainda não implementar tabela OC com tensão arbitrária. Propor ensaio incremental, CPU rápida primeiro, GPU ecluster lento originais; tensão nominal apenas como hipótese de teste; preservar mecanismos térmicos eAVB; validar clocks reais/transições/repouso/carga no hardware. Nenhuma modificação personalizada ou compilaçãoOC executada nesta fase.
