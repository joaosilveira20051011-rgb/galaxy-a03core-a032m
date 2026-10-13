# Identificação de binning para o OC

Evidência enviada pelo proprietário: leitura somente do byte9 de /sys/bus/nvmem/devices/sprd-efuse0/nvmem com od retornou12 em hexadecimal. O DTS sharkl3 atribui bits0..3 a dvfs_bin_cpu0 e bits4..7 a dvfs_bin_cpu1. Assim CPU0/bin2 e CPU1/bin1, condicionado ao mesmo mapeamento DT do aparelho de referência.

Nas tabelas sc9863a correspondentes, limite original do cluster0 (núcleos0–3)1,2GHz tem OPP1,10V em operating-points-2; cluster1 (núcleos4–7)1,6GHz tem OPP1,05V em operating-points-1. Estes são valores de tabela, não uma medição elétrica. As variantes térmicas -65 diferem (respectivamente1,121875V e1,071875V no topo).

A proposta do usuário de cluster lento1,4GHz/1,05V combinaria aumento de frequência com tensão inferior ao OPP original1,2GHz/1,10V. Não adotá-la como incremento positivo. Faixa1,13–1,15V para cluster rápido elevaria nominalmente80–100mV sobre1,05V, não25–50mV.

Coletas runtime confirmaram CPUs0–3 até1200000kHz; CPUs4–7 até1600000kHz. GPU /sys/class/devfreq/60000000.gpu tem256/384/550MHz, mínimo256, máximo550MHz. O nome60000000 é endereço, não frequência.

DEBUG_FS está desativado no config original, explicando ausência de debug/opp. Logdmesg recebido registra trecho tardio com mensagens AVC e não identifica o binning inicial. Nenhuma modificação OC aplicada nem tensão OC validada. Próxima fase: analisar capacidade real das tabelas HW-DVFS, PLL, reguladores e acoplamento SCU/FCM; apresentar especificação experimental para aprovação antes das alterações.
