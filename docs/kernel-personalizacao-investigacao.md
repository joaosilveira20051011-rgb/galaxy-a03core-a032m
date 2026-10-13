# Investigação para personalização do kernel — escolhas pendentes

Nenhuma modificação personalizada ou compilação foi iniciada. A diretiva do usuário exige entrevista e aprovação da especificação antes dessas etapas.

## Atualização oficial inspecionada
Arquivo baixado individualmente do Samsung Open Source Release Center, attachId 44245, associado no catálogo ao A032MUBS7CZA5.
Tamanho: 46797 bytes.
SHA256: acd5a4cdf9e0c74db317b6fa7838346a8652e70a53478f42839a914e0e4f4650.
CRC de todos os membros do ZIP passou.
Contém A032FXXS9CZA1_kernel.tar.gz (45775 bytes) e A032FXXS9CZA1_kernel.txt (2094 bytes).
O README manda usar a base A032FXXS6CXE1 e sobrepor a atualização A032FXXS9CZA1. Não exige aplicar cegamente todas as atualizações intermediárias.
Toolchains prescritas: GCC aarch64-linux-android-4.9 e Clang clang-r383902; CC=clang, LD=ld.lld, ARCH=arm64, CLANG_TRIPLE=aarch64-linux-gnu-, BSP_BUILD_FAMILY=sharkl3, BSP_BUILD_ANDROID_OS=y e BSP_BUILD_DT_OVERLAY=y. Referência de defconfig: a3core_eur_open_defconfig. Deve-se comparar a configuração/variante com o boot A032M antes de adotá-la.
Delta inspecionado: drivers/hid/hid-input.c, drivers/hid/hid-multitouch.c, drivers/media/usb/uvc/uvc_driver.c e sound/usb/clock.c.

O download grande anterior do conjunto de fontes ficou incompleto (cerca de 312 MiB) e não abre como ZIP. Foi rejeitado como base validada; não há árvore oficial completa verificada nem build concluído.

## Recursos confirmados na configuração original
- ARM64, COMPAT, MODULES e MODVERSIONS; HZ=250.
- WALT, SCHED_TUNE, schedutil padrão; performance/powersave/userspace também habilitados.
- PSI habilitado; não está desativado por padrão.
- ZRAM/ZSMALLOC, writeback/LRU writeback; LZO e LZ4 disponíveis na configuração.
- CFQ e noop habilitados, padrão CFQ. Deadline e BFQ desabilitados.
- ext4 e F2FS habilitados; F2FS compression desabilitado.
- TCP BIC habilitado e padrão; CUBIC/BBR/Westwood desabilitados.
- SELinux e gerenciamento térmico presentes.

Configuração permite afirmar recursos compilados, não quais algoritmos/governadores estão ativos em cada dispositivo de runtime.

## Possibilidades a escolher
CPU/GPU OC e undervolt: não confirmados para A032M S7; apenas investigação experimental, sem frequências inventadas ou promessa de artefato.
Governadores/scheduler: base existente; ajustes exigem auditoria de DVFS e testes de latência/calor/consumo.
Memória: preservar PSI e avaliar mudanças justificadas de reclaim/compressão. Tamanho zRAM e swappiness são políticas runtime; LMKD é daemon userspace, não recurso resolvido apenas por recompilar o kernel.
I/O: preservar CFQ/noop ou investigar habilitar deadline; benchmark real exigido. Não trocar filesystem sem decisão separada.
Root: Magisk atual funciona; KernelSU alternativo demanda compatibilidade própria e não equivale a ganho de desempenho.
Temperatura: preservar proteções; ajustes de limites/tensões exigem escolha específica e hardware testado.
Rede: algoritmos extras dependem de carga e condições; habilitar opções não acelera automaticamente internet.
Depuração: conservar meios de diagnóstico/recuperação; não remover drivers ou hardening para reduzir tamanho sem necessidade.

## Cobertura e limites
Samsung catálogo/modal/README/delta efetivamente consultados; configuração extraída do boot funcional; repositórios IverCoder, almondnguyen, physwizz e MarsXZ já investigados no projeto. Buscas adicionais em inglês, russo e chinês não identificaram demonstração reprodutível de OC neste S7. Não significa inexistência mundial de tal implementação.
AOSP: https://source.android.com/docs/core/perf/lmkd
Driver de referência comunitário em investigação: IverCoder/android_kernel_samsung_a3core, commit 81da2968a777556d20847e30b618658905af67a3.
Grupos privados e histórico completo de Telegram/Discord não foram acessados; a pesquisa não cobre toda a internet.

Próximo gate: escolher perfil/funcionalidades e aprovar uma especificação concreta antes de modificar ou compilar.
