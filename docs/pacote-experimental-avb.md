# Pacote experimental crDroid 10.13 — A032M S7

O pacote é preparado pelo projeto, sem exigir WSL ou montagem pelo usuário. A gravação e os testes físicos ainda não ocorreram.

## Conteúdo previsto do AP TAR
- super.img: montagem validada com crDroid a64 Vanilla e vendor/product/system_ext enviados.
- vbmeta.img: cópia do vbmeta principal do aparelho com flags 3.
- Nenhum boot, dtbo, recovery, modem ou vbmeta_vendor substituto.
- Nenhum kernel modificado incluído. O kernel em uso continua sendo a referência.

## Verificação AVB executada
O avbtool oficial, obtido do AOSP, verificou a assinatura SHA256_RSA2048 incorporada e a árvore sha256 da GSI. Isso confirma integridade em relação à chave incorporada, não confiança da Samsung nessa chave.

GSI: filesystem 2056237056 bytes; imagem 2089295872 bytes; rollback index 1738368000.
O vbmeta_system atual descreve system de 1381511168 bytes e product de 1184481280 bytes, diferentes dos componentes usados na nova montagem. Não reutilizar esses descritores como prova de que a nova montagem está verificada pelo firmware.

## Alteração proposta
O vbmeta principal foi alterado somente no campo flags: 0 -> 3, offset 120, uint32 big-endian. Como os bytes anteriores são zero, somente o byte 123 mudou.
SHA-256 da cópia alterada: b74dd3a53b33125fbe788015d1c5389df5b4cb2713afc81719fc10b52cc06c98.
Tamanho mantido: 1048576 bytes.

O avbtool confirmou flags 3. A assinatura Samsung da cópia alterada falha, como esperado: não possuímos a chave privada Samsung e não há nova assinatura válida. A aceitação da cópia depende do caminho de verificação do bootloader desbloqueado, ainda não testado neste A032M S7.

A documentação/código AOSP define flags 1 (hashtree disabled) e 2 (verification disabled). Flags diferentes de zero são inválidas em vbmeta encadeado. Por isso, não se aplicou a alteração indiscriminadamente a vbmeta_system/vbmeta_vendor.
Uma partição vbmeta_system pode ser tratada como raiz por determinadas rotas do fs_mgr; a identificação desse comportamento no firmware concreto permanece uma validação de instalação. O pacote mínimo altera apenas a raiz vbmeta principal.

## Limite da entrega
TAR legível e hashes corretos não garantem aceitação pelo Odin, inicialização nem compatibilidade funcional. Este é um pacote para teste, não uma distribuição homologada.
Antes de gravar: conferir backups já realizados, rota de retorno ao firmware S7 e situação do recovery. A troca de sistema pode exigir factory reset; o pacote não contém userdata.

## Fontes primárias
- https://android.googlesource.com/platform/external/avb/+/refs/heads/main/avbtool.py
- https://android.googlesource.com/platform/external/avb/+/refs/heads/main/libavb/avb_vbmeta_image.h
- https://android.googlesource.com/platform/external/avb/+/refs/heads/main/libavb/avb_slot_verify.c
- https://source.android.com/docs/core/tests/vts/gsi
- https://github.com/libxzr/vbmeta-disable-verification

O pacote mantém os arquivos originais disponíveis separadamente. Não substituir os backups pelos arquivos modificados.
