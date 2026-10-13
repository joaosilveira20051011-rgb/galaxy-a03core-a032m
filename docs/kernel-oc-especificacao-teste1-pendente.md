# Especificação proposta: testeOC1 — aguardando aprovação

## Evidência nova
Proprietário leu um byte no offset10 de sprd-efuse0/nvmem com od; resultadohex10. DTB/DTS: dvfs_bin_dsu bits4..7 =>bin1. CPUrápida bin1 eSCUbin1 têm topo nominal1,05V na tabela normal e1,071875V na variante65. Valores de OPP/driver, não medição elétrica.

## Proposta experimental
- Fonte: mesma base oficial S7 usada na referência que iniciou, com configuração original.
- Apenas cluster1 bin1: substituir o topo normal1600000kHz/1050000uV por1700000kHz/1075000uV. Número/ordem dos índices preservado. No modo normal o ponto1,6GHz é substituído, não adicionado; os demais pontos permanecem.
- SCU/FCM bin1: manter frequência1250000kHz do topo e ajustar somente sua tensão normal para1075000uV, alinhada ao domínio compartilhado. Não overclockarSCU.
- Variantes térmicas65: preservar topoCPU1600000kHz/1071875uV eSCU1250000kHz/1071875uV, mantendo a referência como fallback. Verificar transição real, coerência das tabelas e aplicação do ramo térmico antes de declarar funcionamento.
- CPU0–3: preservar1,2GHz e tabelas originais. GPU: preservar550MHz e tensão/clockoriginais. Não alterar ZRAM, I/O, governors ou outras políticas neste teste.
- Preservar AVB, ramdiskMagisk, DTBO e limites térmicos. A alteração OPP requer novo DTB do boot; não afirmar preservação byte a byte do DTB nesta versãoOC. Conferir contêiner SamsungDTB e embalagem.
- 1,075V é hipótese experimental representável (+25mV na tabela normal), não tensão mínima comprovada nem garantia de estabilidade. Não inferir segurança a partir do limite de codificação do PLL/regulador.

## Verificações antes da entrega
Revisão dos pares/índices CPU+SCU e DTBgerado; configdiff explícito; buildImage/módulos; CRCsABI; bootheader/tamanho/rodapé; diferença limitada à proposta; pacote de retorno à referência funcional. Identificação de build distinta preservando release compatívelcomvendor.

## Teste físico
Boot completo, root/módulos, frequências disponíveis e comportamento real sob carga; suspensão/reboot; testes CPU isolada e carga combinada sem aumentar outros clocks; temperatura/transições/throttling; jogos/frametimes após estabilidade básica. Sysfs solicitado não prova sozinho clock físico. Nenhum ganho percentual inventado.

## Escopo futuro
1,8GHz, clusterlento1,4GHz eGPU600MHz continuam objetivos de etapas posteriores. Não incluídos no teste1. Implementação, compilaçãoOC eflash não executados nesta proposta. Aprovação do proprietário pendente conforme sua exigência de aprovar especificação antes das alterações.
