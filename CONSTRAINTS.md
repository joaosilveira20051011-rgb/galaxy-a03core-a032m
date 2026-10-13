# Critérios do kernel A032M S7

## Referência autorizada

- Compilar primeiro com clocks e tensões originais; zero alterações em OPP, PLL, tabelas de tensão ou limites térmicos nesta etapa.
- Nenhuma alteração em vbmeta, userdata, recovery ou firmware de rádio.
- Base oficial e toolchains identificadas por origem, versão e SHA-256. Arquivos incompletos ou CRC incorreto bloqueiam uso.
- Preservar configuração, imagens originais e logs; não reduzir verificações para declarar sucesso.

## Gates

| Verificação | Critério | Evidência |
|---|---|---|
| Fontes | ZIP íntegro e atualização correta | zipfile.testzip, SHA-256 e README Samsung |
| Compilação | exit code 0; zero erros de compilação/link | log integral e status do make |
| Configuração | diferenças com IKCONFIG explicadas | scripts/diffconfig e configuração final |
| Clocks/tensões | tabelas originais preservadas | diff dos DTS/drivers e inspeção de DT |
| Arquitetura | ARM64 com suporte COMPAT | readelf de vmlinux e CONFIG_ARM64/COMPAT |
| Módulos vendor | vermagic e CRCs auditados | readelf .modinfo/__versions e Module.symvers |
| Boot | componentes e header conferidos; imagem <= 67108864 bytes | parser de boot, hashes de componentes |
| Hardware | não declarar boot/estabilidade sem teste físico | relatório do proprietário e logs disponíveis |

Warnings deverão ser classificados; não mascarar problemas de código ou ABI para terminar o build. Não basta igualar a string de vermagic para provar ABI.

## Etapa futura

CPU rápida 1,8 GHz, CPU secundária 1,4 GHz e GPU 600 MHz são metas experimentais solicitadas. Tensões estimadas não são valores validados. Instalação requer autorização explícita. Nenhum ajuste experimental entra nesta referência.
