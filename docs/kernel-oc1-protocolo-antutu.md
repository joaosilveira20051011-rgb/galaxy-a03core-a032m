# OC1: preparação do benchmark

2026-10-13. O proprietário informou rotação automática normal. É evidência funcional relatada; não elimina os timeouts de sensorhub documentados.

Referência escolhida: AnTuTu Benchmark10.5.2 + pacote3D Lite V10. O APK principal oficial foi baixado e sua estrutura ZIP/manifest examinada: versão10.5.2 e bibliotecas armeabi-v7a/arm64-v8a/x86/x86_64. O diretório central ZIP do pacote3D Lite foi lido por HTTP Range206 e contém as mesmas arquiteturas. Isso confirma empacotamento para32bits, não execução completa no A03.

Links oficiais verificados por HTTP200:
https://file.antutu.com/soft2/antutu-benchmark-v10-en.apk
https://file.antutu.com/soft2/antutu_benchmark_v10_3d_lite.apk
Os antigos links /soft/ consultados retornaram404. A página principal atual oferece V12, portanto usar os links V10 acima para manter o protocolo fixo.

Primeiro: uma execução completa com OC1, aparelho resfriado, fora do carregador, brilho fixo, sem mudar governor/limites térmicos; preservar tela com total e subscoresCPU/GPU/MEM/UX, versão e temperaturas disponíveis. Interromper se houver congelamento, reinício ou artefatos gráficos. Depois comparar referência e OC com exatamente os mesmos APKs/ROM/apps/condições e repetições equivalentes.
Sem benchmark original equivalente, não calcular ganho percentual de OC. Não comparar diretamente números de versões maiores diferentes ou conjuntos3D diferentes. Um benchmark bem-sucedido não prova estabilidade diária.
Status: protocolo definido; benchmark ainda não executado ou recebido pelo assistente.
