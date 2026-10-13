# A03 Core SM-A032M — OC2 térmico experimental

Compilado e validado estaticamente em 13/10/2026. NÃO iniciado nem testado fisicamente nesta versão. Destinado ao ambiente do proprietário: SM-A032M, firmware A032MUBS7CZA5, crDroid 10.13 Android 14 a64 e ramdisk já modificado pelo Magisk. O boot fornecido preserva esse ramdisk; não é um pacote universal para aparelhos sem root.

## Comportamento implementado

OC1 preservado: CPU lenta 1400 MHz, rápida 1800 MHz, GPU 600 MHz. O sensor board-thmzone é o termistor da placa; não se afirma que reproduz fisicamente quiet_therm do Redmi.

| Controle adicional | Ativação | Limite | Liberação |
|---|---|---|---|
| CPU, ambos os grupos | Placa >=55 °C | Lento 1100 MHz / rápido 1500 MHz | Placa <53 °C |
| GPU | Placa >=60 °C | 384 MHz | Placa <58 °C |

Leitura a cada segundo por workqueue congelável. Em erro de sensor, os limites adicionais ficam ativos. A temperatura mostrada no status pode ser a última válida; verificar também sensor_error. CPUFREQ_ADJUST aplica o menor limite junto aos controles existentes; a GPU é limitada no update_devfreq antes do target do driver, na próxima atualização do devfreq. O limite adicional não escreve em max_freq: esse arquivo da GPU pode continuar indicando 600 MHz mesmo quando o teto interno é 384 MHz. Observar a frequência efetiva sob carga.

Mantidos: tabelas quentes do DVFS a 65 °C, proteções térmicas originais, bateria/carregamento, thermald, vendor, DTBO, AVB e ramdisk. Nenhuma regra do thermald foi removida e nenhum tuning de memória/I/O foi aplicado. Controles originais podem limitar antes ou mais que o adicional.

O controlador nativo é compilado com CONFIG_THERMAL e só inicia com o identificador de máquina sprd,sc9863a; não instalar em outros modelos por compartilhar o SoC.

## Verificações concluídas

- Compilação real: quarta tentativa terminou com código zero. As três anteriores falharam no tar dos cabeçalhos; até a tentativa serial falhou. Foi isolada a pasta temporária de gen_kheaders.sh em /tmp, mantendo a checagem do tar e limpeza automática. A causa externa exata das mudanças de metadados não foi demonstrada.
- Configuração final e IKCONFIG iguais byte a byte à configuração original.
- DTB idêntico ao OC1, sem novos limites críticos nem mudança de OPPs nesta etapa.
- ELF AArch64 e símbolos do controlador presentes.
- 28 módulos originais, 2064 entradas de importação: nenhuma ausência nem divergência de CRC; vermagic correspondente. Isso não substitui teste de carregamento físico.
- Teste de software da histerese: ativação, permanência e liberação nos limites de CPU/GPU; checkpatch do controlador sem erros/avisos.
- Boot header v2, página 2048, partição de 64 MiB, ramdisk preservado e TAR contendo somente boot.img.
- O blob vbmeta embutido foi preservado. O descritor assinado já não corresponde ao payload com root; não se afirma nova assinatura AVB válida. Nenhuma partição vbmeta deve ser alterada para este teste.
- Warnings preexistentes de Kconfig Samsung/OpenSSL do host ficam preservados nos logs. Não foram desativadas verificações para obter sucesso.

## Arquivos

AP_BOOT_OC2_THERMAL_EXPERIMENTAL.tar: candidato para AP do Odin.
AP_RESTAURAR_OC1_FUNCIONAL.tar: cópia exata do AP OC1 que o proprietário já iniciou; reversão para o OC1.
boot_OC2_THERMAL_EXPERIMENTAL.img e Image: artefatos reais.
OC2-source-complete.patch: controlador e correção do empacotador, aplicado após OC1.
kernel.config, embedded.config, Module.symvers, relatórios e logs: validação/reprodução.
thermal-vendor-original-decoded.xml: política original recuperada, para auditoria; NÃO instalar como substituição do thermal.conf criptografado.

Commits locais: aea866f (controle térmico), df2ea21 (isolamento dos cabeçalhos). Base OC1: 6eaf404. Aplicar o patch sobre a fonte Samsung/base OC1 documentada no repositório; utilizar a mesma toolchain Clang r383902 e configuração. O script de build pressupõe a organização a03-kernel/toolchains, host-tools e a03-work já usada no projeto.

## Instalação e reversão após autorização do proprietário

Não houve flash nesta entrega. Antes de instalar, conservar os dados pessoais e ambos os APs. No ambiente já testado do proprietário, usar Odin com AP_BOOT_OC2_THERMAL_EXPERIMENTAL.tar somente em AP; BL/CP/CSC vazios, Re-Partition e Nand Erase desativados. Preservar as demais opções da instalação OC1 que funcionou. Não substituir DTBO, vendor ou vbmeta.

Se não iniciar, usar AP_RESTAURAR_OC1_FUNCIONAL.tar em AP com o mesmo procedimento. O proprietário conseguiu retornar ao Download Mode mantendo Power + Volume Menos continuamente até aparecer o modo; esse é o procedimento observado neste aparelho, não uma garantia universal.

Após boot, confirmar pelo CMD/platform-tools. Substituir SERIAL_DO_A03 pelo identificador exibido por adb devices; não publicar esse identificador em logs públicos:

```cmd
adb -s SERIAL_DO_A03 shell getprop sys.boot_completed
adb -s SERIAL_DO_A03 shell "su -c 'cat /sys/kernel/a03core_thermal/status; uname -a; cat /sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq; cat /sys/devices/system/cpu/cpufreq/policy4/scaling_max_freq; cat /sys/class/devfreq/60000000.gpu/cur_freq'"
adb -s SERIAL_DO_A03 shell "su -c 'dmesg'" > "%USERPROFILE%\Downloads\A03_OC2_Boot.txt" 2>&1
```

Depois testar rotação, conectividade, áudio, câmera e uma carga habitual com observação de temperatura/frequências. Não provocar aquecimento artificial para alcançar os limites. Sem testes físicos, não declarar boot, redução térmica, FPS, autonomia ou estabilidade confirmados.

## Tuning separado

Após boot validado, auditar ZRAM/compressão disponíveis, parâmetros de reclaim, LMKD da ROM e I/O. Preparar um módulo Magisk reversível para ajustes em execução, mantendo os mínimos de CPU/GPU e a proteção térmica. Alterar uma categoria por etapa e medir efeitos; nenhuma promessa de percentuais de ganho. Novos recursos que exijam configuração/código do kernel serão tratados em uma compilação posterior, com justificativa.
