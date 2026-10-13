# Referência stock S7 recompilada — teste físico pendente

## Resultado
Kernel compilado realmente, a partir da base oficial Samsung SM-A032F_13_Opensource.zip e atualização explicitamente publicada para A032MUBS7CZA5. Sem alterações personalizadas de frequências, tensões, térmica ou AVB. A imagem de teste conserva o ramdisk Magisk do boot fornecido pelo proprietário; não é uma imagem integralmente stock.

## Fontes e integridade
- [Samsung Open Source](https://opensource.samsung.com/uploadSearch?searchValue=SM-A032M), uploadId12510: base attachId44242, atualização attachId44245.
- Base: 383912576 bytes; SHA256 `781c9f7108447e986074240caafae82dde605f36620140e2dc5a47359b1dcc43`; ZIP CRC aprovado.
- Atualização S7CZA5: SHA256 `acd5a4cdf9e0c74db317b6fa7838346a8652e70a53478f42839a914e0e4f4650`; ZIP CRC aprovado. Aplicadas as quatro substituições prescritas sobre a base CXE1: HID input, HID multitouch, UVC e USB audio clock.
- Clang oficial r383902, versão11.0.1, commit LLVM b397f81060ce6d701042b782172ed13bee898b79, com binutils AOSP do diretório aarch64-linux-android-4.9. Não afirmar disponibilidade do compilador GCC4.9: o pacote consultado contém binutils.
- Configuração extraída do kernel original, preservada integralmente: SHA256 `507ece72123418ae7a0511475c3051ad339f18aeec07e0ef6021fc719295fd04`. Config final byte a byte idêntica.
- Compilação: ARCH=arm64, CC=clang, LD=ld.lld, CLANG_TRIPLE=aarch64-linux-gnu-, BSP_BUILD_FAMILY=sharkl3, BSP_BUILD_ANDROID_OS=y, BSP_BUILD_DT_OVERLAY=y, targets Image/modules/dtbs, -j6.
- LOCALVERSION=-27418755 e BUILD_NUMBER=A032MUBS7CZA5 preservam o release necessário ao vendor. Coincidência de texto não foi usada como prova de ABI.
- Uma ligação simbólica do arquivo oficial apontava para modules/kernel4.14/audio fora da árvore extraída; foi excluída na extração segura e registrada. O build completo terminou sem dependência dela.

## Validação executada
- Build exit0; Image AArch64 de19884048 bytes, SHA256 `2a40851d9f96b3a0affdbc2eb3f116a0d0487e8a329d5fd88280609631d704a9`.
- Image tem mesmo tamanho do kernel original, mas não é byte idêntico:620 bytes diferem. Parte das diferenças está nos metadados de compilação; não se afirma que todas sejam cosméticas.
- Cinco módulos encontrados em /vendor/lib/modules: incrementalfs(133), kheaders(5), trace_irqsoff_bytedancy(42), trace_noschedule_bytedancy(41), trace_runqlat_bytedancy(30). Todas as251 referências CRC coincidiram com Module.symvers; vermagic correspondente. Isto não substitui testes de carregamento/runtime.
- Avisos preservados: redefinição Kconfig SEC_DEBUG, defaults de choices e APIs OpenSSL3 obsoletas no utilitário host extract-cert. Sem patches para esconder avisos.
- Boot Android header2, page2048, partição/imagem64MiB; SHA1 de identificação do header recalculado com algoritmo primeiro confirmado contra o header original.
- Ramdisk, Magisk, DTB, padding e rodapé originais preservados. DTBO do aparelho não é substituído.
- Revisão independente confirmou que ambos os TAR contêm somente boot.img, que o payload de teste corresponde ao Image compilado e que a restauração coincide com o original.

## AVB: correção explícita
O boot enviado contém rodapé AVBf e estrutura vbmeta SHA256_RSA4096. Seu descritor já não corresponde ao payload com root: digest esperado261a3c5e..., calculado67cb540b.... Esta condição preexistente foi preservada. Não há nova assinatura Samsung válida e a aceitação do novo boot precisa ser testada no aparelho desbloqueado. Nenhuma flag de vbmeta foi alterada. A presença de rodapé deve substituir qualquer registro anterior que afirmasse sua ausência.

## Artefatos
- AP_BOOT_STOCK_RECOMPILADO_TESTE.tar: SHA256 `41a70b135b5217b4ba6373439c900a19be5c7df59aab8ccbf37918affcec946f`.
- AP_RESTAURAR_BOOT_ATUAL.tar: SHA256 `1855a7bd1d56b44681392b743ed2617a71ee1f80a168c74269993fad896b856f`.
- Boot de teste: SHA256 `ee67577d2078d40b777669e2c0e8471765aee8d28583247a1dff087fcde10508`.
- Boot de restauração: SHA256 `575035d10db48692ed4c066da83a78b44b367a57d5670c3a78330ac157e497b5`.
O ZIP inclui Image, configuração, logs, Module.symvers, módulos compilados, DTB/DTBO gerados para inspeção, relatórios e verificação PowerShell. Os DTBs/DTBOs gerados são referência de compilação, não instrução para flash.

## Teste físico de referência
Acesso USB ao aparelho não existe neste ambiente; nenhuma inicialização foi executada pelo assistente.
1. Extrair ZIP e executar verificar.ps1. Exigir TODOS os hashes OK.
2. Manter o TAR de restauração disponível no PC e confirmar acesso ao Download Mode. Neste aparelho, o proprietário comprovou segurar Power+VolumeMenos continuamente até aparecer Download Mode. Não substituir este relato por uma sequência genérica de troca de botões.
3. Odin já utilizado com êxito neste projeto: selecionar somente AP_BOOT_STOCK_RECOMPILADO_TESTE.tar em AP; BL/CP/CSC vazios; Re-Partition e Nand Erase desmarcados. Não carregar vbmeta, super, PIT ou firmware completo.
4. Após PASS, observar boot completo. Em falha, retornar ao Download Mode com a sequência comprovada e instalar somente AP_RESTAURAR_BOOT_ATUAL.tar em AP. Isto restaura o boot fornecido, sem garantir recuperação de todo possível incidente.
5. Após iniciar, coletar adb shell cat /proc/version (release coincide de propósito; usuário/host/data de compilação distinguem a recompilação), adb shell uname -a, adb shell su -c id e adb shell lsmod. Testar toque/tela, WiFi, Bluetooth, chamada/dados, áudio/câmeras, carga, suspensão e novo reboot.

## Próxima fase
Somente após confirmação física da referência: investigar separadamente cluster rápido1,8GHz, lento1,4GHz e GPU600MHz. Tensões1,13–1,15V/1,05V/GPU+25mV são hipóteses. Binning, OPP térmicos, SCU/FCM, reguladores e PLL precisam ser auditados antes de escolher valores. Nenhum ganho de desempenho ou estabilidade foi medido.

## Classificação
Compilado: SIM. Verificação estática: realizada com limites descritos. Boot confirmado: NÃO. Funcionalidades no kernel recompilado: NÃO TESTADAS. Estabilidade/benchmarks: NÃO TESTADOS.
