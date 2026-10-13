# Kernel próprio — base oficial identificada

Consulta efetiva ao Samsung Open Source Release Center em 2026-10-13:
https://opensource.samsung.com/uploadSearch?searchValue=SM-A032M

A página retorna 3 entradas para SM-A032M. A entrada de uploadId 12510 associa SM-A032F e SM-A032M e oferece a base Android 13 e atualizações, incluindo explicitamente A032MUBS7CZA5 no nome do pacote mais recente.

## Arquivos listados no modal oficial
- SM-A032F_13_Opensource.zip — 383912576 bytes, attachId 44242.
- SM-A032F_13_Opensource_A032FXXS7CYA3_A032FXXS7CYA4_A032MUBS5CYA6_A032MUBS5CYA7_A032MUBS5CYA8_A032MUBS5CYA9_A032MUBS5CYAA_A032MUBU5CYB1.zip — 34759 bytes, attachId 44243.
- SM-A032F_13_Opensource_A032FXXS8CYF3_A032MUBS6CYF3_A032FXXS8CYF4_A032MUBS6CYF4_A032MUBS6CYF5_A032MUBS6CYF6_A032MUBS6CYF7.zip — 46644 bytes, attachId 44244.
- SM-A032F_13_Opensource_A032FXXS9CZA1_A032MUBS7CZA1_A032FXXS9CZA2_A032MUBS7CZA2_A032MUBS7CZA3_A032MUBS7CZA4_A032MUBS7CZA5.zip — 46797 bytes, attachId 44245.

O prefixo A032F da base não significa que se deve instalar um boot pronto de A032F: a própria Samsung associa os modelos neste lançamento de fontes. As diferenças de configuração/DTS e instruções de integração deverão ser lidas antes de compilar.
Os tamanhos pequenos dos ZIPs de atualização sugerem complementos/deltas, ainda sujeitos à inspeção. Não tratá-los como árvores completas sem abrir.

## Referência extraída do boot funcional
Kernel 4.14.199-27418755-abA032MUBS7CZA5.
IKCONFIG recuperado do kernel no boot_atual.img, cujo SHA256 é 575035d10db48692ed4c066da83a78b44b367a57d5670c3a78330ac157e497b5.
Config confirma ARM64=y, COMPAT=y, MODULES=y, MODVERSIONS=y, HZ=250, governor padrão schedutil, LOCALVERSION vazio e LOCALVERSION_AUTO desativado.
Isso orienta a primeira compilação; não garante equivalência de símbolos/ABI dos módulos externos.

## Sequência autorizada
1. Obter base e atualizações oficiais e verificar arquivos.
2. Identificar README, defconfig, ferramentas, DTS e diferenças do S7.
3. Comparar a configuração recuperada e os módulos vendor (MODVERSIONS).
4. Compilar uma referência sem overclock e registrar logs/versões/hashes.
5. Preparar boot de teste preservando componentes necessários e oferecer rollback do boot funcional.
6. Só após teste físico, implementar alterações de kernel isoladas e medir resultado.

Estado deste registro: catálogo e modal oficial consultados; download/inspeção/compilação em andamento, nenhuma compilação declarada pronta e nenhum kernel novo instalado.
O vbmeta original deve ser mantido. O teste anterior de flags 3 terminou em bootloop e não deve ser repetido como padrão.
