# OC1: GPLL confirmado por leitura de registradores

2026-10-13. Nova captura do proprietário preserva o boot de 0 a aproximadamente28,26s.

Aos17,964696s: `A03CORE_OC1 GPLL requested=600000000 register_rate=600000000 ret=0`.
Isto confirma pedido600MHz, leitura calculada a partir dos registradores600MHz e retorno0 da programação. Não é medição física independente nem teste de estabilidade.
Em seguida o PowerVR registra BVNC22.86.104.218, encontra OPPs256/384/600MHz e inicializa. O comando insmod de pvrsrvkm termina com sucesso.

Achados preservados: avisos durante probe de drivers de toque/sysfs/GPIO e formato de log de chipone; ausência de mmdvfs.ko e leds-sc27xx-bltc.ko solicitados pelo init. Sem comparação equivalente da referência, não classificar como regressão OC nem ignorar seu impacto funcional.

Aos0,818711s o driver software fan53555 identifica Option13/Rev1 e rejeita ChipID13 com probe -22. O hardware DVFS Unisoc utiliza caminho distinto; não concluir que CPU não recebe alimentação. Porém os valores de tensão efetivamente entregues e a compatibilidade elétrica do regulador externo continuam sem confirmação. A quantização da tabela de hardware é uma inferência de código, não uma medição.

Status: dois boots relatados pelo proprietário; primeiro confirmado por sys.boot_completed=1 e versão OC1; segundo registro mostra inicialização desde0s até28s. CPU1,4/1,8GHz em tabelas e GPLL600MHz por registradores; funcionamento sob carga, sensores, alimentação e estabilidade pendentes.
