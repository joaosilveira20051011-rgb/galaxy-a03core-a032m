# Primeiro teste: bootloop

Após o PASS no Odin, o usuário relatou reinícios repetidos na logo Samsung, sem chegar à animação crDroid. Duas tentativas de recovery por botões não abriram o menu. A captura de adb devices mostrou lista vazia naquela tentativa; isso não prova ausência permanente de USB/ADB durante todo o ciclo.

O pacote não substituiu boot, dtbo ou recovery. Foram alterados super e vbmeta principal. Portanto a causa permanece aberta: comportamento da verificação/bootloader, montagem em first stage ou compatibilidade da GSI, entre outras. Nenhum factory reset foi realizado e não se deve atribuir a falha aos dados antigos sem evidência.

Preparado TAR para reverter somente vbmeta principal ao backup original, sem substituir super nem userdata. É um teste de isolamento e não uma correção comprovada.

Arquivo: AP_RESTAURAR_VBMETA_ORIGINAL_A032M_S7.tar
Tamanho: 1054720 bytes.
SHA256 TAR: 534578ad18acb575575988dfe10dfbb8aeb3f7d145e467ca8f3a8a2ce87f8af5.
Contém somente vbmeta.img, 1048576 bytes, idêntico byte a byte ao backup original:
560e09e545a6e330e3ce13205001b19e48c3bcbd60babad9cef85a4db4c270eb.

Pendente: acesso ao Download Mode, gravação desse TAR e observação do próximo boot. Se não resolver, considerar retorno completo por super_atual.img e vbmeta original, ambos salvos antes do teste. Não usar imagens de boot/recovery de outro binário como tentativa aleatória.
