# Montagem experimental — crDroid 10.13 / SM-A032M S7

## Estado
Imagem montada e validada fora do aparelho em 2026-10-13. **Não instalada, não homologada e sem ganho de desempenho medido.**
Kernel de referência: boot atual A032MUBS7CZA5 com Magisk; nenhum kernel substituto incluído.
A preparação de AVB/verity e o procedimento de gravação permanecem pendentes. Este documento não autoriza tratar a imagem como pacote pronto para Odin.

## Arquivos utilizados
| Partição | Tamanho em bytes | SHA-256 |
|---|---:|---|
| system / crDroid 10.13 a64 bvN Vanilla | 2089295872 | ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6 |
| vendor atual | 407756800 | 6594a216453065b3b02efba11a20b2f12c6b6397e52e4014c1f3dbc0355e1451 |
| product atual | 2621440 | 88808d75976626d278006e97bbe09e0a5e75601c874df1d4e75900712b5a5075 |
| system_ext atual | 2621440 | f69cae008ab17cb767e535df6e331f6c0659c710c4d92782ebf917a3ddc7cfad |

GSI original: https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08
Arquivo: crDroid-10.13-a64_bvN-Unofficial.img.xz.
Propriedades inspecionadas: Android 14, SDK 34, ABI armeabi-v7a/armeabi, patch de segurança 2025-02-01.
a64 não significa sistema com aplicativos arm64.

## Resultado da montagem
- Arquivo raw: super_crdroid_10.13_a032m_s7_raw.img.
- Tamanho: 3303014400 bytes.
- SHA-256 observado: 1336913ec0f1989d7d62d136560b9aca7bb17a648e7c9576d5fa754cecdf0f09.
- liblp: versão 10.0; metadata máxima 65536; 2 slots; flags none.
- Grupo main: máximo 3298820096 bytes.
- Quatro partições readonly, sem sufixos de slots.
- Alinhamento escolhido para a montagem: 1048576 bytes.
- lpdump leu a tabela; lpunpack extraiu as quatro partições.
- SHA-256 das quatro partições extraídas igual ao de cada entrada.
- e2fsck -fn, sem reparos, passou nas quatro entradas.
- product/system_ext contêm 11 inodes usados cada, consistentes com imagens mínimas; o número isolado não prova compatibilidade.

Mensagens de lpmake “Invalid sparse file format at header magic” ocorreram ao detectar entradas raw: a execução terminou com código 0 e as extrações foram conferidas. Não usar essa explicação para ignorar erros ou diferenças de hashes em outras execuções.
O binário lpmake apresentou falha ao receber --help; sem argumentos exibiu o uso e a montagem efetiva concluiu. Binários comunitários fixados por commit e hash, sem auditoria completa de código.

## Reproduzir
Ambiente: Linux x86_64 ou WSL Linux x86_64; curl e ferramentas GNU; reservar cerca de 12 GB livres.
Colocar na mesma pasta os quatro arquivos com os nomes da tabela/script. Não usar vendor de outro aparelho.
O script verifica hashes antes da montagem, não escreve em partições do telefone e recusa sobrescrever a saída.

No CMD, na pasta dos arquivos:
```bat
powershell -NoProfile -Command "Expand-Archive -LiteralPath 'vendor_atual.zip' -DestinationPath 'vendor_extraido' -Force"
copy /b "vendor_extraido\vendor_atual.img" "vendor_atual.img"
certutil -hashfile "vendor_atual.img" SHA256
wsl --status
curl.exe -fL "https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/main/scripts/montar-super-crdroid.sh" -o "montar-super-crdroid.sh"
wsl bash ./montar-super-crdroid.sh
certutil -hashfile "super_crdroid_10.13_a032m_s7_raw.img" SHA256
```

Só executar a montagem se WSL estiver instalado com distribuição Linux configurada. A GSI .img deve estar previamente extraída; o script não extrai .xz.
Os backups pessoais de boot/super e dados do aparelho não devem ser publicados como pacote universal.
O script contém os hashes específicos deste projeto e deve falhar para entradas diferentes.

## Fontes das ferramentas
https://github.com/itsNileshHere/android-lptools/tree/b7b5c09916ab88074692006db7dab34256da6e24
https://android.googlesource.com/platform/system/extras/+/refs/heads/master/partition_tools/

## Próxima validação
Entender como o boot atual trata dm-verity/AVB e conferir a rota de recuperação/gravação antes de preparar o pacote flashável.
Depois: boot, tela/toque, chamadas, dados móveis, Wi-Fi, Bluetooth, áudio/câmeras, suspensão e desempenho.
A integridade estrutural não confirma nenhum desses comportamentos.
