# Avaliação e proposta de OC — aprovação pendente

## Escolhas recebidas
Usuário prioriza fluidez diária, jogos/FPS, multitarefa e bateria. Solicita testar CPU 1,8 GHz e GPU 600 MHz, sugerindo +25 a +50 mV, e delega a avaliação técnica.
Não há implementação nem build personalizado iniciado. A especificação concreta ainda depende de aprovação conforme a diretiva anterior.

## Evidências inspecionadas
Árvore comunitária de referência IverCoder/android_kernel_samsung_a3core, commit 81da2968a777556d20847e30b618658905af67a3, não tratada como correspondência binária comprovada do S7.
arch/arm64/boot/dts/sprd/sc9863a.dtsi: CPU cluster0 CPU0-3 e cluster1 CPU4-7; cluster1 com OPP de 1600000 kHz. Tabelas por bin via nvmem, incluindo 1050000, 1100000 e 1150000 uV no ponto 1,6 GHz; tabela genérica 1121875 uV. Há seleção por temperatura 65 e acoplamento de DVFS com domínio FCM/SCU. 65 é limiar específico de seleção de tabelas, não temperatura de bateria nem teto universal de segurança.
arch/arm64/boot/dts/sprd/sharkl3.dtsi: GPU sprd,rogue com 256000, 384000 e 550000 kHz; sprd,dvfs-lists associa frequência a índice e divisor de clock. O campo uV é zero nessas entradas; isso NÃO significa alimentação física de zero volts e não prova controle de tensão GPU disponível.
Driver drivers/cpufreq/sprd-hwdvfs-sharkl3.c programa frequências/tensões e MPLL e converte tensão para os passos do regulador.

## Julgamento
+25/+50 mV não é uma tensão mínima demonstrada, garantia de estabilidade nem limite seguro. É uma hipótese cuja adequação depende de bin, tensão absoluta, regulador, temperatura, carga e implementação.
1,8 GHz CPU e 600 MHz GPU são alvos experimentais, sem estabilidade comprovada. Referência mostra 1,6 GHz/550 MHz, mas valores/tabelas efetivamente usados no aparelho devem ser conferidos no DT e interfaces runtime.
Ganhos de FPS/autonomia não foram medidos. OC e tensão maior podem aumentar consumo/throttling e comprometer o objetivo de bateria.

## Proposta para aprovação
- Primeiro compilar/testar referência compatível com frequências e tensões originais; Magisk, módulos, vbmeta e proteções preservados.
- Depois estudar OC CPU apenas no cluster rápido CPU4-7, mantendo cluster lento original. Meta 1,8 GHz condicionada a PLL/DVFS/bin e validação incremental; não habilitar automaticamente em uso diário.
- OC GPU como experimento separado, depois do CPU, condicionado ao driver, clock/divisor/PLL e caminho de tensão. Meta 600 MHz, sem alegar que editar somente o número na tabela é suficiente.
- Nenhum acréscimo global fixo de tensão aprovado ou implementado. Propor ajustes apenas após mapear tensões absolutas, limites do regulador e domínios compartilhados.
- Manter perfis normal e experimental separados, com caminho de reversão e instalação somente mediante autorização explícita.
- Não modificar limites térmicos/charging/bateria, nem aplicar undervolt ao mesmo tempo.

Fontes: https://github.com/IverCoder/android_kernel_samsung_a3core/tree/81da2968a777556d20847e30b618658905af67a3
Samsung atualização S7 foi inspecionada no projeto; base completa oficial continua sem download válido. Essa lacuna impede declarar base compilável pronta.
