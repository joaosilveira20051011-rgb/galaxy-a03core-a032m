# OC1: primeiro boot físico e tabelas de runtime
Data: 2026-10-13. Evidência: resultados de ADB fornecidos pelo proprietário após instalar o candidato autorizado e dmesg OC1. Registro sanitizado, sem publicar serials ou logs brutos.

Confirmado:
- sys.boot_completed=1.
- /proc/version corresponde ao build OC1 de 13/10/2026 12:12:21 PDT, release 4.14.199-27418755-abA032MUBS7CZA5.
- policy0, CPUs0–3: tabela 768000/884000/1000000/1100000/1400000 kHz, scaling_max_freq=1400000.
- policy4, CPUs4–7: tabela 768000/1050000/1225000/1400000/1500000/1800000 kHz, scaling_max_freq=1800000.
- GPU: available_frequencies=256000000/384000000/600000000 Hz, max_freq=600000000; cur_freq=256000000 na leitura.
- O trecho do kernel lista os módulos PowerVR, câmera, toque, Wi-Fi e demais módulos carregados. Isso não comprova todas as funcionalidades.

Não confirmado:
- Frequências físicas sustentadas sob carga, tensão elétrica, estabilidade prolongada ou ganho de desempenho.
- Mensagem GPLL e readback dos registradores: não presentes no dmesg enviado, cujo primeiro timestamp já é aproximadamente42,39s. A ausência não demonstra falha nem sucesso da programação.

Achado relevante:
- Aproximadamente89,98s, timeout na comunicação com sensorhub (shub_send_data/nwrite=-62) seguido de WARNING em shub_send_command; outros timeouts ocorrem perto de105s.
- É um aviso de kernel com trace, não um kernel panic registrado nesse trecho. Não atribuir ao overclock nem declarar preexistente sem comparação equivalente com referência.
- Grande volume de AVCs SELinux limita a retenção do log de inicialização. Não desativar SELinux ou tratar todas as mensagens de timeout como erros PLL: os avisos periódicos do watchdog incluem parâmetros de configuração.

Próximas validações: capturar log de kernel desde o reinício, testar sensores e uso básico, verificar transições reais e mensagens de falha, depois realizar ensaios separados de CPU e GPU.
Status: compilado e validado estaticamente; boot físico confirmado por ADB; tabelas runtime confirmadas; GPU600MHz sob carga e estabilidade ainda pendentes.
