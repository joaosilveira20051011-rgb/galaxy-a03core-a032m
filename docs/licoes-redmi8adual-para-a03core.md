# Lições do Redmi 8A Dual aplicáveis ao A03 Core
Data: 2026-10-13. Status: recuperação documental; nenhuma alteração ou compilação OC do A03 autorizada nesta etapa.

## Escopo e evidências recuperadas
Foram consultados o handoff CONTEXTO_COMPLETO_KERNEL_REDMI_8A_DUAL_OC.txt, Auditoria_primeira_build.md, Auditoria_OC2.md, Auditoria_OC2_Diagnostico.md, Pesquisa_e_Auditoria_OC3_2496.md, Pesquisa_e_Auditoria_OC3V_2496_APC25.md, Redmi_PLL_Investigacao_20261011.md, Auditoria_OC4.md, OC4_alteracoes.patch, Demonstrativo_OC5.md, manifest.json, registros de terminal de 12/10/2026 e diagnostico(1).txt. Também foram recuperadas mensagens anteriores do projeto. Arquivos privados não são reproduzidos aqui, nem identificadores pessoais.

Limitações: recuperação dos materiais acessíveis, não de uma transcrição integral garantida. Não houve reexecução dos benchmarks, recompilação do Redmi ou inspeção elétrica. O handoff de 09/10 precede os testes de OC5 de 12/10; seu estado antigo não invalida os testes posteriores.

## Histórico recuperado
Base Redmi: olivewood, Snapdragon 439, MiThorium 4.19.315, commit baecec5449e288adfb846c278c56fc288c99a2cd, Evolution X Android 14.
- OC inicial: alvos 2304 MHz no cluster rápido, 1708,8 MHz no lento, GPU 750 MHz.
- OC2: alvo experimental 2800 MHz; histórico de falhas de inicialização. Não há caracterização elétrica suficiente para declarar um teto físico.
- OC3/OC3V: alvo 2496 MHz. Investigação identifica falha de lock do PLL; OC3V acrescentava tensão APC solicitada, sem resolver o problema. O log bruto consultado mostra preparação da transição, não sucesso em 2496 MHz.
- OC4: investigação da votação digital do PLL, propagação de erros, restauração dos registradores e limitação após falha. Patch real foi consultado.
- OC5: alvo rápido 2400 MHz, lento 1804,8 MHz, GPU 750 MHz configurada. Commit registrado bfbc9de3ebe00c0933d6758eb99440ea42ba3402.

### Evidência física de OC5
O registro de terminal de 12/10 contém teste temporário com fastboot boot, sys.boot_completed=1 e transições repetidas para 2400000000 Hz com stage=3 e ret=0. Também registra a tabela do cluster lento incluindo 1804800 kHz. Confirma boot e sucesso reportado pelo driver nas transições; não substitui medição independente do clock nem demonstra estabilidade prolongada em toda carga.
GPU: consultas negadas por permissão. Portanto 750 MHz é configuração, não frequência física confirmada no registro.
Hash do boot OC5 registrado e conferido no terminal: f094b03c1f71a49df42e594a9f9ea96ea4c080a5e69616c4b4f4ad2afe1e4270.
O arquivo registra flash permanente bem-sucedido, mas termina sem prova de novo boot completo após esse flash.

Benchmarks históricos relatados: AnTuTu 10.4.5 GPU Lite, 147629 original, 164690 em versão OC, 178025 em OC4. Não há benchmark OC5 identificado. Esses valores não são uma comparação controlada reexecutada e não permitem prever ganho no A03.

## Descobertas técnicas aproveitáveis
1. Base e dependências exatas importam. No Redmi, uma árvore de áudio incorreta compilava, mas faltavam 569 símbolos exportados; foi rejeitada. Após correção, a auditoria registrou 11464 exports/CRCs compatíveis. No A03, continuar verificando módulos vendor/odm e a ABI da base S7, além do build.
2. Tensão do núcleo, alimentação analógica do PLL e voto digital do PLL são domínios distintos. Aumentar APC não comprova que a causa da falha de clock foi resolvida. RPM TUR=384 no Qualcomm é um nível lógico, não 384 mV.
3. '+25 mV' exige definir a referência. Na OC3V, ceiling 880->905 mV, floor 815->905 mV e tensão vista no diagnóstico anterior 855->905 mV são mudanças diferentes. Fixar floor=ceiling também muda o comportamento de malha fechada daquele corner.
4. Não ignorar erros de transição. OC4 propagava falha de lock e restaurava configuração anterior; alguns caminhos anteriores podiam esconder falhas. Falha na restauração continuava crítica, não era convertida em sucesso.
5. Instrumentar pedido, valor arredondado e retorno. Stage=4/ret=0 significava liberar limite no diagnóstico, não atingir a frequência. Stage=3/ret=0 é evidência do retorno do driver.
6. Tests de host verificam lógica e regressões, não transistores, reguladores, cache ou estabilidade física.
7. Preservar ramdisk, estrutura de boot e recuperação específica. Fastboot boot do Redmi não é um procedimento demonstrado para o Samsung.
8. Separar CPU, GPU, memória e ajustes térmicos permite localizar causas. Boot bem-sucedido é apenas a primeira validação.

## Diferenças que impedem copiar números ou patches
| Item | Redmi 8A Dual | A03 Core do projeto |
|---|---|---|
| Plataforma | Qualcomm SDM439 | Unisoc SC9863A |
| Kernel | 4.19.315 | 4.14.199 |
| Cluster rápido | CPU0–3/policy0 | CPU4–7/policy4 |
| Cluster lento | CPU4–7/policy4 | CPU0–3/policy0 |
| GPU | Adreno/Qualcomm | PowerVR |
| Controle | CPR, clocks Qualcomm | hardware DVFS Unisoc, reguladores e tabelas específicas |
| Boot/recuperação | fastboot demonstrado | formato Samsung/Odin |

Não portar drivers Qualcomm, tabelas CPR, votos RPM ou parâmetros PLL para Unisoc. Reaproveitar a estratégia de revisão, testes, instrumentação e recuperação, após estudar os caminhos reais do A03.

## Consequências para a proposta A03
O aparelho identificado possui bin lento 2, rápido 1 e SCU 1. As tabelas consultadas pedem 1,10 V no topo lento de 1,2 GHz e 1,05 V no topo rápido de 1,6 GHz, em faixa térmica normal. São valores solicitados pelo software, não medições elétricas.
- 1,05 V para o cluster lento em 1,4 GHz seria inferior à tensão solicitada em 1,2 GHz; não é aumento leve.
- 1,13–1,15 V para o rápido representaria +80–100 mV sobre 1,05 V; não +25–50 mV.
- O cluster rápido e SCU exigem tratamento consistente de índices e alimentação compartilhada.
- A possibilidade de codificar frequência no PLL não demonstra estabilidade nessa frequência.
- 1,7 GHz é escolha de incremento para um ensaio isolado; não teto físico estabelecido.

## Proposta pendente de nova autorização
Primeiro ensaio: cluster rápido em 1,7 GHz, tensão solicitada normal 1,075 V (+25 mV sobre sua tabela normal); SCU permanece em 1,25 GHz, com tensão solicitada normal alinhada em 1,075 V. Substituir o ponto superior mantendo a quantidade de índices, em vez de acrescentar índice sem mapear SCU.
Manter cluster lento em 1,2 GHz e GPU em 550 MHz. Preservar tabelas quentes originais, políticas térmicas e demais configurações. Revisar o mecanismo real de mudança de faixa térmica e falhas antes de entregar imagem.
Não há rollback OC implementado ou comprovado no A03 apenas porque existiu no Redmi.
Alvos posteriores 1,8/1,4 GHz e GPU 600 MHz continuam experimentais e sujeitos a etapas próprias.
Autorização para preparar/compilar não autoriza flash: instalação requer autorização explícita separada.

## Estado
Concluída recuperação e comparação dos materiais disponíveis. Nenhuma mudança em clocks/tensões, nova imagem OC ou teste físico A03 foi executado nesta etapa.
