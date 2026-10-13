# Plano de compilação da referência

Pedido autorizado: produzir primeiro um kernel em clocks/tensões originais para teste de boot; somente depois investigar OC.

Ordem: fontes verificadas -> ambiente/toolchains -> configuração/ABI -> build -> inspeção -> pacote/rollback -> teste físico.

Base: Samsung SM-A032F_13_Opensource.zip, atualização que lista A032MUBS7CZA5. O README da atualização exige a base A032FXXS6CXE1. Comparar defconfig eur com a configuração extraída do boot A032M.

Ferramentas prescritas: Clang r383902, GCC aarch64-linux-android 4.9, ARCH=arm64, BSP_BUILD_FAMILY=sharkl3. Preservar .config final e logs.

A imagem de boot original possui ramdisk Magisk; a substituição do kernel deverá preservar os demais componentes necessários. Não modificar AVB. Produzir TAR de retorno ao boot funcional antes da instalação.

Riscos: divergências da fonte pública com firmware, CRCs de módulos, layout/assinaturas específicas do boot e disponibilidade de toolchains antigas no host. Tratar separadamente; build concluído não implica instalação validada.

Tarefas em tasks/todo.md. Referência verificável em kernel/reference/A032MUBS7CZA5.config. Critérios em CONSTRAINTS.md.
