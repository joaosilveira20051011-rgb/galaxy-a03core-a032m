# Central de downloads e instalações — A03 Core

Auditoria de 13/10/2026. Ambiente do projeto: **SM-A032M / A032MUBS7CZA5 (S7), crDroid 10.13 a64 Vanilla Android 14, kernel OC2 e Magisk 30.7**.
Este índice é a referência atual; relatórios antigos registram etapas históricas.

## Instalações: arquivos e tutorial
| Material | Download | Tutorial / recuperação | Estado |
|---|---|---|---|
| GSI crDroid 10.13 a64 Vanilla | [Cópia na Release](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/crDroid-10.13-a64_bvN-Unofficial.img.xz) · [Origem naz664](https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08) | [GSI: backup, super, Odin e recuperação](TUTORIAL-GSI-BOOTLOADER-DESBLOQUEADO.md) | GSI instalada no projeto; não é AP/super pronto |
| Kernel de referência sem OC | [ZIP](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/a03core-stock-baseline-20261013.zip) | [Tutorial referência](TUTORIAL_A03CORE_STOCK_v0.1.txt) | Boot confirmado |
| Kernel OC1 histórico | AP_RESTAURAR_OC1_FUNCIONAL.tar dentro do ZIP OC2 | [Tutorial OC1](TUTORIAL-OC1-HISTORICO.md) | AP disponível; ZIP histórico separado ainda não publicado |
| Kernel OC2 térmico | [ZIP](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/a03core-OC2-thermal-55-60-experimental.1.zip) | [Tutorial OC2](TUTORIAL-OC2-THERMAL.md) | Boot confirmado; atuação nos limites térmicos e estabilidade prolongada pendentes |
| Perfil de memória Magisk | [Arquivos versionados](../modules/a03_memoria) | [Instalação ADB e reversão](TUTORIAL-MEMORIA-A03-2GIB.md) | 2 GiB / lzo-rle / 70 / 1 / 5 confirmados após reboot; não é ZIP instalável |
| LiteGapps Core ARM14 | [ZIP oficial](https://downloads.sourceforge.net/project/litegapps/litegapps/arm/34/core/2026-10-01/LiteGapps-core-arm-14.0-20261001-official.zip) | [Instalação Magisk e remoção](TUTORIAL-GAPPS-LITEGAPPS-ARM14.md) | ZIP integral/CRC conferidos; módulo e processos presentes no aparelho; login/sincronização completa não auditados |
| Magisk 30.7, aplicativo | [APK oficial](https://github.com/topjohnwu/Magisk/releases/download/v30.7/Magisk-v30.7.apk) | Instalar o APK; root do ambiente já preparado pelos boots do projeto | APK sozinho não faz root; root inicial do Samsung original não homologado |

## Hashes e formatos
| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| a03core-OC2-thermal-55-60-experimental.1.zip | 34577485 | `6889c22a7dd028cf455e445fec1ebfcc0b7b4eb66b823a09ce75f01977e35dda` |
| a03core-stock-baseline-20261013.zip | 39508699 | `f86c440e9321d362c22352bc4417b568a447ca5833d96f9d33b8a993567fb57f` |
| crDroid-10.13-a64_bvN-Unofficial.img.xz | 779310104 | `30dcb62d15c6da6a9a2e46e6b6f66383a1a15b5dcaeb877ed030bc8d051e8413` |
| TUTORIAL_A03CORE_STOCK_v0.1.txt | 13120 | `4b8b646eab3be3eaee7f312af61db299a03be4b4d9acff8d7ac43e5aba341526` |
| LiteGapps-core-arm-14.0-20261001-official.zip | 96005180 | `ea09bdbbaccb3182920d45f0af05a19a3c70ee6b30843b9f74407d18fdd7da5f` |
| Magisk-v30.7.apk | — | `e0d32d2123532860f97123d927b1bb86c4e08e6fd8a48bfc6b5bee0afae9ebd5` |

Hashes da Release são os digests publicados pelo GitHub; GApps foi baixado integralmente e testado nesta auditoria. Os downloads de referência, OC2, GSI e APK foram abertos por requisição parcial, com magic ZIP/XZ/APK correspondente. Isso não equivale a testar hardware nem a baixar novamente toda a GSI.
SHA-256 da GSI **extraída**: `ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6` — tamanho 2089295872 bytes.
Nunca carregar o .img.xz diretamente no AP do Odin.

## Ferramentas auxiliares
- [Platform-tools oficial](https://developer.android.com/tools/releases/platform-tools).
- [7-Zip oficial](https://www.7-zip.org/).
- [Driver Samsung oficial](https://developer.samsung.com/android-usb-driver).
- [Python oficial para Windows](https://www.python.org/downloads/windows/), usado no preparo de TAR.
- Odin: a execução do projeto usou a versão 3.14.4. Não existe nesta auditoria uma cópia do executável usado acompanhada de hash/origem comprovada; conserve sua cópia funcional. Não confundir sites de download com página oficial Samsung. Um download auditado do mesmo binário permanece pendente.

## Ordem de uso
1. Conferir modelo real no vendor, firmware S7, root/bootloader e compatibilidade.
2. Fazer backup próprio e preparar recuperação.
3. GSI/super conforme tutorial correspondente; não seguir pacote AVB antigo.
4. Kernel de referência, OC1 histórico ou OC2, conforme objetivo; não instalar todos indiscriminadamente.
5. GApps opcional em Vanilla e com Magisk funcionando.
6. Perfil de memória opcional, seguido de reinício e conferência.

Boots publicados preservam o ramdisk Magisk do aparelho de referência. Não são imagens sem root homologadas.

## Fontes, patches, logs e compilação
- [Base Samsung e atualização S7](kernel-base-oficial-s7.md): download pelo Samsung Open Source Release Center; conferir arquivos/hashes exatos descritos.
- [Relatório da compilação de referência](kernel-stock-compilado-2026-10-13.md), [configuração original](../kernel/reference/A032MUBS7CZA5.config), [script de build](../scripts/build-kernel-stock.sh).
- [Patch OC1](../kernel/patches/OC1-1800-1400-600.patch), [patch OC2 adicional](../kernel/patches/OC2-board-thermal-55-60.patch).
- [Relatório OC1](kernel-oc1-1800-1400-600-compilacao.md), [relatório OC2](kernel-oc2-thermal-compilado-e-validacao.md), [auditoria runtime](kernel-oc2-boot-confirmado-auditoria-rom.md).
- O ZIP de referência e ZIP OC2 incluem binários, configuração, logs e relatórios de verificação. OC2 contém também seu patch adicional completo e script de build.
- [Script de montagem super](../scripts/montar-super-crdroid.sh) e [manifesto](../artifacts/crdroid-10.13-a032m-s7-manifest.json).
- O ZIP automático Source code da Release aponta para o **tag histórico**, não inclui todos os avanços posteriores em main. Use Code > Download ZIP de main para os documentos/scripts atuais ou git clone.
- Árvore Samsung completa e toolchains são dependências externas; não afirmar que este repositório isolado compila sem preparar as dependências descritas. A configuração exata e procedimentos reais estão documentados; a reprodução em um segundo ambiente não foi executada.

## O que não é distribuído como receita de instalação
- Backups pessoais EFS/NV, serial/IMEI/contas e credenciais.
- AP antigo com vbmeta alterado: causou bootloop e não deve ser apresentado como instalação padrão.
- Super pronta universal: varia conforme vendor/firmware. O script faz montagem com imagens compatíveis e hashes estritos; as imagens próprias devem ser obtidas pelo procedimento de backup.
- Método integral validado a partir de qualquer firmware Samsung original: ainda não existe neste projeto.
- GSI anterior Lineage/MagiskSI adaptada por terceiro: fonte/patches e binário correspondente não foram disponibilizados nesta auditoria.

## Telegram e estado da distribuição
Comunidade: https://t.me/A03CoreBrasilGSIKernel/1
Os tópicos Comece aqui, Tutoriais e GSI e Downloads recebem o link deste índice; arquivos grandes são apontados pelos links verificados da Release/origem.
A tentativa de anexar o ZIP OC1 separado ao Telegram falhou. A rota disponível para OC1 usa o AP dentro do ZIP OC2.
A sessão GitHub no navegador não está autenticada e o conector utilizado não oferece edição/upload de Release. Por isso, esta auditoria atualiza o repositório e o Telegram, mas não altera o corpo da Release nem promete novos assets. A frase antiga “não inclui a GSI” no corpo é superada pela seção GSI e pelo asset .img.xz efetivamente anexado. O índice registra os arquivos reais e suas limitações.
