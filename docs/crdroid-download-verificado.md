# crDroid 10.13 — conferência do download

Registro de 2026-10-13. Resultados fornecidos pelo proprietário através do CMD no Windows.

- Arquivo: crDroid-10.13-a64_bvN-Unofficial.img.xz
- Release original: https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08
- 7-Zip 24.08 x64: teste CRC64 e extração concluídos com "Everything is Ok".
- Tamanho comprimido: 779310104 bytes.
- Tamanho extraído: 2089295872 bytes.
- SHA-256 da imagem extraída: ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6

## Capacidade

Soma dos arquivos system proposto, vendor atual, product atual e system_ext atual: 2502295552 bytes.
Limite do grupo main informado por lpdump: 3298820096 bytes.
Diferença aritmética: 796524544 bytes, antes de considerar alinhamento e formato da GSI.

Isso indica viabilidade de tamanho se a imagem estiver em formato raw. Ainda é necessário inspecionar formato, sistema de arquivos, componentes e metadados. Não comprova compatibilidade nem inicialização.

## Próximas verificações

- Formato e arquitetura da imagem candidata.
- AVB/vbmeta atuais, para não presumir que o novo system será aceito.
- Empacotamento e conferência das partições resultantes.
- Instalação e testes ainda não realizados.
