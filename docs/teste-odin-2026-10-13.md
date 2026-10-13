# Teste de gravação — 2026-10-13

## Confirmado pela captura enviada pelo usuário
- Aparelho identificado anteriormente no Download Mode: SM-A032M, OEM LOCK OFF (U), FRP LOCK OFF, KG STATUS CHECKING; firmware coletado A032MUBS7CZA5.
- Odin fornecido como 3.14.4; log identifica engine ID:3.1401.
- Arquivo AP: AP_crDroid_10.13_A032M_S7_EXPERIMENTAL.tar.
- ID:COM preenchido; Added!!.
- Auto Reboot desmarcado; F. Reset Time marcado; Re-Partition/Nand Erase/Flash Lock desmarcados.
- Log lista super.img e vbmeta.img, seguido de RQT_CLOSE !! e RES OK !!.
- Resultado: PASS!, succeed 1 / failed 0; tempo exibido 02:47.

Isso comprova que o Odin reportou a gravação concluída. Não equivale a readback independente, inicialização confirmada, aceitação em runtime da configuração AVB, estabilidade ou ganho de desempenho.

## Próxima etapa
Reiniciar para testar a primeira inicialização. Não foi executado factory reset nesta etapa. Se houver erro/bootloop, coletar a tela e o comportamento antes de escolher a próxima intervenção.

Kernel modificado: não incluído. O AP não contém boot.img nem dtbo.img; esses componentes não foram substituídos por este pacote.

Status deste registro: gravação reportada como bem-sucedida; boot e funções pendentes.
