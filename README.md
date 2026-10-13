# Galaxy A03 Core — A032M S7

Projeto experimental de customização do Galaxy A03 Core SM-A032M S7. A crDroid 10.13 a64 Vanilla iniciou após restaurar o vbmeta original; o proprietário relatou funcionamento normal dos testes básicos. A próxima etapa é compilar um kernel próprio a partir das fontes compatíveis.

## Aparelho e base confirmados

- Vendor/modelo: SM-A032M; a GSI apresenta SM-A032F.
- Bootloader: A032MUBS7CZA5; modem: A032MUBS7CZA1.
- Sistema atual: crDroidAndroid-14.0-20250307-v10.13 (a64_bvN Vanilla), Android 14.
- Sistema anterior: LineageOS 21.0-20250125-UNOFFICIAL-a3core.
- Sistema e vendor: armeabi-v7a/armeabi (32 bits).
- Kernel: 4.14.199-27418755-abA032MUBS7CZA5; configuração ARM64 com COMPAT, PSI, ZRAM, LZ4 e MODVERSIONS.
- Root: Magisk 30.7; nenhum módulo listado.
- GSI escolhida: crDroid 10.13 a64_bvN Vanilla, release v2025.03.08 de naz664.

## Estado do trabalho

1. Identificação por ADB concluída.
2. Boot e DTBO extraídos e inspecionados; configuração do kernel recuperada.
3. Cópia de super concluída no computador do proprietário.
4. Vendor, product e system_ext recebidos; ZIP do vendor passou na verificação CRC. Assinaturas ext4 reconhecidas nas três imagens.
5. Super montada, extraída novamente e conferida por hashes; Odin reportou PASS.
6. Vbmeta principal com flags 3 causou bootloop no conjunto testado; após restaurar somente o backup original, o usuário relatou inicialização e ADB confirmou sys.boot_completed=1.
7. Root Magisk 30.7 preservado; nenhum módulo. Kernel original e zRAM de aproximadamente 2,5 GiB mantidos.
8. Funções básicas: usuário relatou tudo normal; isso não substitui testes de estabilidade prolongados.
9. Kernel próprio: fontes/configuração em investigação; nenhuma nova compilação ou instalação confirmada.
10. Nenhum ganho de desempenho medido ou prometido.

## Metadados de super

- Tamanho físico: 3303014400 bytes.
- Metadata version: 10.0; máximo: 65536 bytes; slots: 2.
- Grupo main: máximo 3298820096 bytes.
- Partições: system, vendor, product, system_ext; readonly.
- O vendor e os metadados devem ser conferidos antes de empacotar uma substituição.

## SHA-256 das cópias

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| boot_atual.img | 67108864 | 575035d10db48692ed4c066da83a78b44b367a57d5670c3a78330ac157e497b5 |
| dtbo_atual.img | 8388608 | 44e4a901747134c74745379cde7fa762734b03d5d7b3e97a44c63cf4a224a75f |
| vendor_atual.img | 407756800 | 6594a216453065b3b02efba11a20b2f12c6b6397e52e4014c1f3dbc0355e1451 |
| product_atual.img | 2621440 | 88808d75976626d278006e97bbe09e0a5e75601c874df1d4e75900712b5a5075 |
| system_ext_atual.img | 2621440 | f69cae008ab17cb767e535df6e331f6c0659c710c4d92782ebf917a3ddc7cfad |
| super_atual.img | 3303014400 | 4b2c2545989492d41040050cd70df01ab47d0836dfd9fa3b5bfebaf0d27aa605 |

Hash de super informado pelo comando no aparelho; os demais calculados a partir dos arquivos recebidos. As cópias não incluem userdata e não constituem backup completo.

## Fontes

- https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08
- https://github.com/IverCoder/android_kernel_samsung_a3core
- https://github.com/almondnguyen/android_kernel_samsung_a3core
- https://github.com/physwizz/a032m-T-u3
- https://github.com/MarsXZ-Official/LineageOs-Samsung-Galaxy-A03Core-gsi-adaptation

## Organização

Scripts, documentação e alterações de código serão versionados em Git. Binários grandes poderão ser associados a Releases após conferência do conteúdo e das condições de distribuição. Não publicar identificadores pessoais, credenciais ou partições EFS/NV. Arquivos de outras variantes não são automaticamente compatíveis com A032M/S7.

## Objetivo público e reprodução

Este repositório pretende permitir que outras pessoas reproduzam a customização, com créditos aos projetos originais, scripts de preparação, versões das ferramentas, hashes, instruções de recuperação e resultados de testes. Compatibilidade será registrada por modelo e firmware; não se presume suporte a qualquer A03 Core.

Estado: primeiro boot da crDroid confirmado neste A032M S7, com vbmeta ORIGINAL. O AP experimental que contém vbmeta com flags 3 é um artefato de teste malsucedido e NÃO deve ser repetido como receita de instalação. Não presumir compatibilidade com outros firmwares.

### Download escolhido

- Mantenedor original: naz664.
- Release: https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08
- Arquivo: crDroid-10.13-a64_bvN-Unofficial.img.xz
- Download: https://github.com/naz664/crDroid_gsi/releases/download/v2025.03.08/crDroid-10.13-a64_bvN-Unofficial.img.xz
- Tamanho comprimido informado pela API da release: 779310104 bytes.
- Variante a64 (ARM32/Binder64), Vanilla, sem superuser PHH. Não confundir com arm64.
- Imagem descompactada: 2089295872 bytes; SHA-256 ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6.
- Primeiro boot confirmado com vbmeta original, kernel/DTBO originais; validação prolongada pendente.

### Primeira etapa no Windows

Baixar o arquivo original, guardar os backups separadamente e extrair o .xz com 7-Zip (https://www.7-zip.org/). A saída deve ser uma imagem .img. Não gravar antes de verificar tamanho, conteúdo e pacote preparado para o firmware de destino.

## Registros atuais

- [Estado funcional e resultados](docs/estado-funcional-2026-10-13.md)
- [Montagem e hashes de super](docs/montagem-super-crdroid-validada.md)
- [Teste de gravação Odin](docs/teste-odin-2026-10-13.md)
- [Incidente de bootloop](docs/bootloop-primeiro-teste.md)
- [Base oficial para o kernel](docs/kernel-base-oficial-s7.md)

Para este aparelho, o proprietário confirmou entrada em Download Mode mantendo Power + Volume para baixo até aparecer o modo. Não tratar as sequências anteriores de troca de botões como procedimento validado neste teste.
