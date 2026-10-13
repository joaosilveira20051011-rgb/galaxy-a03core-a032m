# OC2: primeiro boot e auditoria de políticas

O proprietário iniciou o OC2 no SM-A032M em 13/10/2026. Captura mostrou sys.boot_completed=1, version=OC2, sensor_error=0 e limites internos CPU 55/53 °C e GPU 60/58 °C.

Primeira captura: placa 47,597 °C, cpu_limited=0 e gpu_limited=0; policy0 máximo 1400 MHz e policy4 máximo 1500 MHz. A origem transitória do teto 1500 MHz não foi determinada.

Coleta posterior A03_OC2_Limites.txt: placa 40,998 °C, CPU interna 44,462 °C, GPU interna 41,391 °C. Status do controlador: placa 41,082 °C, ambos limites adicionais liberados. policy0 máximo 1400 MHz; policy4 máximo 1800 MHz e 1800 MHz presente na tabela. Ambos cooling devices CPU em estado zero. Logo, o teto anterior de 1500 MHz não permaneceu.

Auditoria dos arquivos init coletados não identificou escrita de scaling_max_freq ou teto explícito de 1500 MHz pela GSI. Vendor init.md.rc contém atribuição do governador power_allocator a zonas térmicas e gatilhos persist.sys.thermal.ipa; thermald permanece configurado. Esses controles não sobrescrevem os thresholds constantes do novo controlador nativo, cujo status sysfs é somente leitura.

Log: sprd-cpufreqhw registrou desativação do boost ao observar policy max 1100 MHz menor que 1400 MHz. O código verificado define boost como modo temporário de inicialização que evita DVFS; a mensagem não prova remoção do overclock. Não foi demonstrado se essa observação veio da proteção inicial do OC2, de temperatura ou de outro controle.

Conclusão limitada às evidências: OC2 iniciou; sensor válido; limites internos preservados; CPU máxima restaurada para 1400/1800 MHz; nenhum sobrescritor foi localizado nos scripts init examinados. Isso não exclui limites dinâmicos de Power HAL/serviços nem comprova frequências efetivas sustentadas sob carga.

Pendentes: acionamento/liberação física em 55/60 °C, teto efetivo GPU 384 MHz quando ativo, ciclos de repouso/jogo, testes de funcionalidades e estabilidade prolongada. Nenhuma política do vendor foi removida, nenhum novo flash nem tuning aplicado nessa auditoria.
