# Estado funcional em 2026-10-13

## Evidências do aparelho
- build.prop lido com root: ro.crdroid.build.version=crDroidAndroid-14.0-20250307-v10.13.
- ro.crdroid.display.version=crDroidAndroid-14.0-v10.13.
- ro.build.flavor=treble_a64_bvN-userdebug.
- Fingerprint do arquivo: google/treble_a64_bvN/tdgsi_a64_ab:14/AP2A.240905.003/eng.nobody.20250307.120152:userdebug/release-keys.
- Android 14 e sys.boot_completed=1.
- su: uid=0, contexto magisk; Magisk 30.7:MAGISK:R.
- /data/adb/modules vazio.
- Kernel preservado: 4.14.199-27418755-abA032MUBS7CZA5, ARMv8l; configuração interna ARM64 com COMPAT.
- RAM utilizável MemTotal 1890968 KiB; MemAvailable observado 832984 KiB, apenas fotografia de um momento, sem comparação de desempenho.
- zRAM: capacidade 2621436 KiB, utilizado 183552 KiB na leitura; prioridade -2.

## Relato funcional
Após a lista de testes de Wi-Fi, dados móveis, chamadas, câmeras, áudio, Bluetooth, suspensão e reinício, o proprietário respondeu “Tudo normal”. Registrar como relato do proprietário; não é bancada independente nem comprovação de estabilidade prolongada.

## Incidente e recuperação
AP com super crDroid e vbmeta alterado para flags 3: Odin PASS em 02:47, seguido de bootloop Samsung. Recovery por sequências sugeridas não foi acessado; adb devices vazio e consulta USB não identificou o telefone naquela leitura.
O proprietário conseguiu Download Mode mantendo Power + Volume para baixo até aparecer o modo. Esse foi o procedimento efetivamente relatado como funcional; as instruções anteriores de soltar/trocar botões não tiveram êxito no teste.
TAR contendo somente vbmeta original: Odin PASS em 00:03. Após reiniciar, o proprietário relatou sistema iniciado e as consultas confirmaram boot_completed=1. Não houve factory reset relatado.
A reversão isolada associa fortemente o bootloop à alteração de vbmeta no conjunto testado. Não comprova por si só o mecanismo interno exato da falha.

## Cuidado com propriedades sobrescritas
getprop retornou fingerprint Samsung, ro.crdroid.version=14.0, verifiedbootstate=green e veritymode=enforcing. A leitura direta do build.prop confirmou v10.13. Esses getprops não bastam para garantir bootloader bloqueado ou cadeia AVB inteiramente válida; o Download Mode anterior mostrava OEM LOCK OFF (U). Não atribuir a origem dessas sobrescritas sem investigar.

## Próxima decisão
Usuário decidiu priorizar kernel próprio compilado; sem ajustes de desempenho em runtime nesta fase. Manter vbmeta original. Primeira compilação deverá ser uma referência compatível, antes de alterações de CPU/GPU, scheduler ou gerenciamento de memória. Nenhum overclock ou ganho de desempenho foi demonstrado.
