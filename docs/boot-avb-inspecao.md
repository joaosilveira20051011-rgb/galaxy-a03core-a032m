# Inspeção do boot atual

Inspeção offline do boot enviado; nenhum arquivo do aparelho foi alterado.

O ramdisk gzip contém `.backup/.magisk` com `KEEPVERITY=true`, `KEEPFORCEENCRYPT=true`, `RECOVERYMODE=false` e `VENDORBOOT=false`.

A `fstab.m168` identifica partições dinâmicas Non-A/B. Para system usa `avb=vbmeta_system`, `logical`, `first_stage_mount` e chaves alternativas `/avb/q-gsi.avbpubkey`, `/avb/r-gsi.avbpubkey`, `/avb/s-gsi.avbpubkey`. Vendor e product também usam AVB; system_ext não apresenta a opção AVB nessa fstab.

Conclusão confirmada: root Magisk não significa que dm-verity foi removido. Não basta gravar uma nova super mantendo qualquer vbmeta sem conferir a cadeia. As imagens vbmeta enviadas têm flags 0; o aparelho relata verity enforcing.

Pendente: comparar os descritores/raízes de verificação com a GSI e definir o conjunto necessário para instalação, sem presumir que o fato de a Lineage atual iniciar garante a inicialização de outra imagem. O bootloader está desbloqueado segundo as propriedades coletadas, mas a aceitação exata pelo firmware deve ser validada no procedimento.
