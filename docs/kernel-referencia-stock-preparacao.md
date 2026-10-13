# Referência stock antes do overclock — 2026-10-13

## Escolha do proprietário
Primeiro produzir e validar um kernel nas frequências e tensões originais. Apenas após boot e testes físicos investigar CPU cluster rápido 1,8 GHz, cluster lento 1,4 GHz e GPU 600 MHz. As tensões propostas (1,13–1,15 V / 1,05 V / GPU padrão ou +25 mV) são hipóteses, não requisitos validados nem garantia de estabilidade.

## Evidências obtidas
- Configuração original extraída do kernel A032MUBS7CZA5, SHA-256 `507ece72123418ae7a0511475c3051ad339f18aeec07e0ef6021fc719295fd04`.
- Árvore stock pública obtida: https://github.com/IverCoder/android_kernel_samsung_a3core/commit/3b5c5894347a78e1cf608180e4f851aa97e00a6e . O autor declara origem A032FXXS6CXE2. Não afirmar equivalência byte a byte com CXE1 sem comparação.
- `olddefconfig` executado com Clang r383902 e a configuração original: diff vazio, configuração final byte a byte idêntica. Avisos Kconfig de SEC_DEBUG e defaults de choice preservados no log. Isto não é compilação do kernel nem teste de boot.
- Dependências bison, flex, bc, cpio, libelf-dev, libfl2 e libfl-dev conferidas contra SHA-256 do índice Ubuntu antes de extração.
- 133 CRCs de símbolos importados extraídos de `incrementalfs.ko` do vendor para futura comparação com Module.symvers. Comparação ainda não executada.
- Pacote oficial Samsung de atualização S7CZA5 íntegro, SHA-256 `acd5a4cdf9e0c74db317b6fa7838346a8652e70a53478f42839a914e0e4f4650`. Sua instrução exige base A032FXXS6CXE1 mais atualização A032FXXS9CZA1. Quatro arquivos atualizados: drivers/hid/hid-input.c, drivers/hid/hid-multitouch.c, drivers/media/usb/uvc/uvc_driver.c, sound/usb/clock.c.

## Pendências
O download do pacote base oficial foi interrompido duas vezes antes de 383912576 bytes. O servidor respondeu HTTP 200 à tentativa de Range e não retomou; nenhum byte foi anexado ao arquivo incompleto. Nova transferência em verificação. Não usar pacote incompleto nem declarar a cópia CXE2 compatível com S7 sem concluir a validação.

Nenhuma alteração personalizada de OPP, PLL, tensão, térmica ou AVB foi aplicada. Nenhum novo kernel foi instalado. Boot e estabilidade do novo kernel não foram testados.

Fonte oficial: https://opensource.samsung.com/uploadSearch?searchValue=SM-A032M
