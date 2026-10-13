# OC2: controle térmico adicional e planejamento de tuning

Estado: implementação experimental; compilação iniciada em 13/10/2026. Não instalado, boot não testado e comportamento físico não validado.

Base: kernel OC1 SM-A032M/A032MUBS7CZA5, crDroid 10.13 Android 14 a64. OC preservado: CPU lenta 1400 MHz, rápida 1800 MHz, GPU 600 MHz.

## Especificação autorizada

Sensor da placa board-thmzone: CPU limitada a 1100/1500 MHz em 55 °C, liberação abaixo de 53 °C; GPU limitada a 384 MHz em 60 °C, liberação abaixo de 58 °C. Os tetos CPU são frequências existentes nas tabelas do aparelho. Não se afirma equivalência física entre board-thmzone e quiet_therm do Redmi.

Novo controlador nativo: leitura a cada segundo em workqueue congelável; falha de sensor mantém limites conservadores; notificador CPUFREQ_ADJUST aplica limite adicional sem substituir a referência térmica do DVFS original. A GPU recebe teto no caminho update_devfreq antes do target do driver; o teto vale na próxima atualização do devfreq. A interface max_freq do usuário não é sobrescrita e pode continuar indicando 600 MHz; é necessário observar a frequência efetiva sob carga.

Preservados: controle térmico original da CPU, tabelas quentes a 65 °C, limites críticos existentes, bateria, carregamento, serviço thermald, vendor, DTBO, AVB e ramdisk. Nenhum módulo de remoção de regras do thermald foi criado.

## Evidências da auditoria

thermal.conf do vendor é criptografado. Foi recuperado XML válido por análise do thermald e a recriptografia reproduziu todos os blocos originais. Regras incluem placa a 50 °C, carga 48/50 °C e SoC 90/95/100/110 °C. Há referências a sensores e caminhos ausentes na coleta; presença no arquivo não comprova aplicação em execução. GPU exposta como 60000000.gpu, simple_ondemand, frequências 256/384/600 MHz; CONFIG_DEVFREQ_THERMAL não habilitado na configuração atual.

Estado observável previsto: /sys/kernel/a03core_thermal/status. Diagnóstico de transições: A03CORE_OC2 no dmesg.

## Tuning posterior

Preparar separadamente um módulo Magisk reversível depois do boot OC2 validado. Avaliar ZRAM e algoritmos efetivamente disponíveis, swappiness/reclaim, LMKD da ROM e escalonadores I/O presentes. Não copiar parâmetros do Redmi; não aumentar mínimos CPU/GPU nem sobrepor limites térmicos. Não prometer percentuais de ganho. Usar métricas comparáveis de responsividade, frametimes, memória, consumo e temperatura. Nenhum tuning extra foi aplicado nesta etapa.
