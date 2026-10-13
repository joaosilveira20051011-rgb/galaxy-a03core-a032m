# OC1 experimental — Galaxy A03 Core SM-A032M S7
Data: 2026-10-13. Kernel compilado e auditado; boot OC ainda NÃO testado.

## Implementação solicitada
| Domínio | Tabela normal solicitada | Alimentação solicitada |
|---|---:|---:|
| CPU0–3, bin2 | 1,4 GHz | 1,15 V |
| CPU4–7, bin1 | 1,8 GHz | 1,10 V |
| SCU, bin1 | 1,25 GHz, sem OC | 1,10 V, alinhada ao cluster rápido |
| PowerVR | 600 MHz | Configuração original |

As duas tensões CPU representam +50 mV sobre os pontos superiores normais identificados no aparelho. São hipóteses experimentais para o primeiro teste, não tensões mínimas caracterizadas nem garantias de estabilidade. A quantização do FAN53555 pode elevar a solicitação lenta de 1,15 V para aproximadamente 1,154518 V conforme a codificação do driver; não é medição elétrica.

O ponto superior foi substituído, mantendo o número de índices de cada domínio e o pareamento CPU rápida/SCU. Por isso 1,2 GHz no cluster lento e 1,6 GHz no rápido deixam de ser pontos da tabela normal destes bins. As tabelas quentes originais e o limiar de seleção de 65 °C permanecem intactos. A passagem entre tabelas ainda depende de teste físico; a frequência efetivamente selecionada pode ficar abaixo do antigo topo por causa da tabela cpufreq normal.

## GPU: correção além do número na tabela
O módulo original pvrsrvkm.ko foi extraído de /mnt/vendor/socko. RgxSprdInit lê sprd,dvfs-lists e associa o índice 9 ao último clock da lista, GPLL. RgxSetFreqVolt seleciona os pais de GPU core/soc por clk_set_parent, sem chamar clk_set_rate.
O patch muda o ponto de 550 para 600 MHz e usa assigned-clocks/assigned-clock-rates para solicitar GPLL=600000000 antes do probe da plataforma. A implementação do próprio kernel 4.14 lê essas propriedades em drivers/clk/clk-conf.c e aplica os defaults em drivers/base/platform.c.
A mensagem A03CORE_OC1 GPLL informa frequência pedida, frequência derivada dos registradores e retorno da programação. Não é uma medição independente nem prova de lock/estabilidade.
O módulo não demonstrou controle de tensão GPU nesse caminho; nenhum aumento fictício foi acrescentado a valores zero do DTS.

## Base e rastreabilidade
Base oficial Samsung SM-A032F_13_Opensource.zip mais atualização A032MUBS7CZA5, conforme publicação Samsung para SM-A032M:
https://opensource.samsung.com/uploadSearch?searchValue=SM-A032M
Hashes, commits locais, compilador e alvos estão em manifest.json.
Clang AOSP r383902 11.0.1; config extraída do aparelho e mantida byte a byte; ARCH=arm64, mesma UTS_RELEASE necessária aos módulos.
OC1-source.patch contém as três alterações do source. Os scripts incluídos auditam os módulos/DTB e empacotam o formato específico. build-stock.sh exige a árvore preparada, toolchains e ferramentas na estrutura do projeto; não é um instalador autônomo nem um build para qualquer computador.

## Verificações realmente executadas
- Segunda tentativa de build: exit 0, Image/modules/dtbs.
- Primeira tentativa falhou em gen_kheaders: TAR detectou diretório alterado durante leitura. Log preservado; repetição terminou sem desabilitar a verificação.
- Avisos herdados: Kconfig SEC_DEBUG/choices e APIs OpenSSL 3 obsoletas no utilitário host extract-cert. Logs preservados.
- Config final e IKCONFIG extraída do Image idênticas à referência; vmlinux ELF AArch64 e Image ARM64.
- 28 módulos originais, 2064 entradas CRC importadas: zero ausências e zero divergências, vermagic correspondente. Isso não substitui novo teste de carregamento.
- DTB compilado: exatamente sete propriedades alteradas; demais propriedades, incluindo OPPs quentes, idênticas. Teste negativo rejeitou DTB stock como candidato OC.
- Empacotador testado contra a referência: roundtrip idêntico em todos os bytes.
- Boot OC: header v2/page 2048, 67108864 bytes; ramdisk preservado; DTB com envelope original, SHA1 do header recalculado.
- TAR OC contém exclusivamente boot.img, conferido byte a byte contra a imagem produzida.
- Blob vbmeta embutido preservado. Seu descritor já não correspondia ao payload com Magisk; não existe nova assinatura Samsung válida. Partição vbmeta não foi alterada.
- Fontes modificadas revisadas e commitadas em branch local dedicada. Nenhum código de thermal, AVB, cpufreq, segurança ou módulo PowerVR foi desativado ou substituído.

## Limitações que permanecem
Nenhum boot OC, teste de funcionalidades, estabilidade, frequência sustentada, temperatura, tensão física ou benchmark foi realizado no aparelho.
Não foi implementada recuperação automática igual à do Redmi. O driver CPU usa transições assíncronas; retorno de sucesso pode indicar solicitação enfileirada. O PowerVR original não propaga todos os erros de clock. Preservar esses caminhos não demonstra estabilidade.
O pacote é específico ao contexto SM-A032M/S7 e aos bins identificados. Outras variantes e dispositivos não foram validados.
Não distribuir esta imagem com ramdisk Magisk como pacote universal para aparelhos sem root.

## Conteúdo e conferência
AP_BOOT_OC1_1800_1400_600_EXPERIMENTAL.tar: candidato experimental.
AP_RESTAURAR_BASELINE_FUNCIONAL.tar: boot recompilado de referência que o proprietário confirmou iniciar; contém o ramdisk do projeto.
boot_OC1_1800_1400_600_EXPERIMENTAL.img e Image: artefatos reais.
sp9863a_OC1.dtb: componente para auditoria/reprodução, NÃO instrução de flash separado.
Não há novo DTBO neste pacote. Os módulos originais extraídos não foram redistribuídos.
Execute verificar.ps1 antes de qualquer instalação; exigir todos os hashes OK.

## Instalação — somente após autorização explícita para teste
1. Confirmar disponibilidade da restauração e acesso ao Download Mode. Neste aparelho, o proprietário demonstrou manter Power+VolumeMenos pressionados continuamente até entrar nesse modo.
2. No Odin já utilizado neste projeto, somente AP_BOOT_OC1_1800_1400_600_EXPERIMENTAL.tar em AP. BL/CP/CSC vazios; Re-Partition e Nand Erase desmarcados. Não carregar PIT, vbmeta, super ou firmware completo.
3. Após PASS, observar a inicialização. Se houver bootloop, retornar ao modo Download pelo procedimento já comprovado e instalar AP_RESTAURAR_BASELINE_FUNCIONAL.tar somente em AP. Esse retorno restaura o boot de referência, não garante recuperação de todo incidente.
4. Depois de iniciar: confirmar sys.boot_completed, versão/data de compilação, root, módulos, frequências disponíveis e mensagem GPLL. Não começar por carga máxima prolongada.
5. Testar CPU/GPU separadamente, transições carga/repouso, suspensão/retorno, conectividade, áudio, câmeras, toque e carregamento; coletar erros DVFS/PLL e registros de falha.
Não há flash executado pelo assistente nem autorização de instalação presumida.

Este relatório substitui a proposta pendente de 1,7 GHz, expressamente rejeitada pelo proprietário.
