# Instalar crDroid 10.13 GSI — A03 Core com bootloader desbloqueado

## Escopo e estado real

Procedimento destinado ao **SM-A032M, firmware A032MUBS7CZA5/S7**, usando crDroid 10.13 **a64_bvN Vanilla**. O bootloader deve estar previamente desbloqueado; este guia não ensina nem executa desbloqueio.

A instalação da GSI foi confirmada no aparelho do projeto, que já tinha boot com Magisk e uma GSI anterior. **A instalação partindo de um sistema Samsung original apenas desbloqueado não foi validada.** Bootloader desbloqueado, root e aceitação AVB/verity são condições diferentes. Não se afirma que desbloquear sozinho torna qualquer boot compatível.

Este guia usa o caminho reproduzível com **root já funcional para obter o próprio backup**. Sem root, é necessário obter e auditar as imagens correspondentes do firmware/uma rota de recovery apropriada antes de seguir; não instalar um boot aleatório apenas para contornar essa etapa.

A montagem abaixo é estritamente conferida contra as entradas usadas no projeto. Se hashes/layout diferirem, o script deve parar: outro ambiente precisa de análise própria. Não remover a conferência para fazê-lo funcionar.

## Downloads disponíveis

A GSI está também [anexada à Release do projeto](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases/download/stock-baseline-v0.1/crDroid-10.13-a64_bvN-Unofficial.img.xz). SHA-256 comprimido publicado pelo GitHub: `30dcb62d15c6da6a9a2e46e6b6f66383a1a15b5dcaeb877ed030bc8d051e8413`. Não é uma super nem AP do Odin; siga a montagem abaixo. [Central atual de materiais](CENTRAL-DOWNLOADS-E-INSTALACOES.md).

## 1. Ferramentas e espaço

- Windows com platform-tools, 7-Zip, driver Samsung e Odin reconhecendo o aparelho.
- WSL com Linux x86_64 configurado, curl, sha256sum, Python 3 e ferramentas GNU. Instalar WSL não é instalar a ROM.
- Reservar pelo menos **30 GB livres no computador** para backups, extração, imagens de conferência e TARs.
- Backup dos dados pessoais fora do telefone e rota de Download Mode/recuperação já confirmada.
- Firmware oficial correspondente disponível para recuperação do próprio aparelho.

Links:
- [Platform-tools](https://developer.android.com/tools/releases/platform-tools)
- [7-Zip](https://www.7-zip.org/)
- [GSI original de naz664](https://github.com/naz664/crDroid_gsi/releases/tag/v2025.03.08)
- [Releases do projeto](https://github.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/releases)

Utilizar o Odin que já reconhece o aparelho. No projeto foi usado Odin 3.14.4; este guia não fornece um executável de origem não conferida.

## 2. Identificar o destino

Na pasta platform-tools, CMD:

```cmd
adb devices
set "A03_SERIAL=SERIAL_DO_A03"
adb -s %A03_SERIAL% shell getprop ro.product.vendor.model
adb -s %A03_SERIAL% shell getprop ro.bootloader
adb -s %A03_SERIAL% shell getprop ro.product.cpu.abilist
adb -s %A03_SERIAL% shell su -c id
```

Substituir SERIAL_DO_A03 pelo identificador LOCAL mostrado por adb devices. Não publicar esse identificador.

No ambiente de referência: vendor.model SM-A032M, bootloader A032MUBS7CZA5, ABI armeabi-v7a/armeabi e root uid=0. Conferir também OEM LOCK OFF na tela de Download Mode. A identificação SM-A032F exibida pela GSI não substitui vendor/bootloader.

**a64 é ARM32/Binder64; não baixar arm64.** Se não houver root, não continuar os comandos de backup abaixo.

## 3. Backup antes de trocar system/super

Os comandos abaixo apenas leem as partições e gravam arquivos no PC. Conferir cada retorno; arquivo vazio ou saída com erro não é backup.

```cmd
mkdir "%USERPROFILE%\Downloads\A03_GSI"
adb -s %A03_SERIAL% exec-out su -c "cat /dev/block/by-name/boot" > "%USERPROFILE%\Downloads\A03_GSI\boot_antes.img"
adb -s %A03_SERIAL% exec-out su -c "cat /dev/block/by-name/dtbo" > "%USERPROFILE%\Downloads\A03_GSI\dtbo_antes.img"
adb -s %A03_SERIAL% exec-out su -c "cat /dev/block/by-name/vbmeta" > "%USERPROFILE%\Downloads\A03_GSI\vbmeta_antes.img"
adb -s %A03_SERIAL% exec-out su -c "cat /dev/block/by-name/super" > "%USERPROFILE%\Downloads\A03_GSI\super_antes.img"
certutil -hashfile "%USERPROFILE%\Downloads\A03_GSI\boot_antes.img" SHA256
certutil -hashfile "%USERPROFILE%\Downloads\A03_GSI\dtbo_antes.img" SHA256
certutil -hashfile "%USERPROFILE%\Downloads\A03_GSI\vbmeta_antes.img" SHA256
certutil -hashfile "%USERPROFILE%\Downloads\A03_GSI\super_antes.img" SHA256
```

No layout de referência, boot tem 67108864 bytes, dtbo 8388608 bytes e super 3303014400 bytes. Antes de qualquer flash, exigir backup íntegro, reconhecido por lpdump e com tamanho correspondente ao layout do seu destino. O backup de super não inclui userdata.

Não publicar estes backups como arquivos universais nem enviar EFS/NV/IMEI/credenciais.

## 4. Baixar, testar e extrair a GSI

CMD:

```cmd
cd /d "%USERPROFILE%\Downloads\A03_GSI"
curl.exe -fL "https://github.com/naz664/crDroid_gsi/releases/download/v2025.03.08/crDroid-10.13-a64_bvN-Unofficial.img.xz" -o "crDroid-10.13-a64_bvN-Unofficial.img.xz"
"%ProgramFiles%\7-Zip\7z.exe" t "crDroid-10.13-a64_bvN-Unofficial.img.xz"
"%ProgramFiles%\7-Zip\7z.exe" x "crDroid-10.13-a64_bvN-Unofficial.img.xz" -o"."
certutil -hashfile "crDroid-10.13-a64_bvN-Unofficial.img" SHA256
```

Se o .xz já existir e for o arquivo correto, pular somente o download. Exigir teste/extração sem erros.

Imagem extraída: **2089295872 bytes**.
SHA-256 da **.img**, não do .xz:
```text
ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6
```

Créditos: naz664, release v2025.03.08. A GSI não contém o kernel OC2.

## 5. Obter as partições de suporte do próprio backup

Ainda no CMD, verificar WSL e abrir Linux na pasta:

```cmd
wsl --status
wsl
```

No terminal Linux, se necessário entrar em /mnt/c/Users/SEU_USUARIO/Downloads/A03_GSI. Executar os comandos seguintes **no Linux**, não diretamente no CMD:

```bash
mkdir -p tools originais
tool_base="https://raw.githubusercontent.com/itsNileshHere/android-lptools/b7b5c09916ab88074692006db7dab34256da6e24/bin"
curl -fL "$tool_base/lpdump" -o tools/lpdump
curl -fL "$tool_base/lpunpack" -o tools/lpunpack
printf '%s\n' 'da0eeb6e3cafc471df3199f681fb9d7d0ad5421763101baa05bb149ead7a7a4b  tools/lpdump' '3c01cd0c4a5bb5c596617e236951c004bbacb91da7d8b33d9bf4d78e4dd1b0b5  tools/lpunpack' | sha256sum -c -
chmod +x tools/lpdump tools/lpunpack
tools/lpdump super_antes.img
tools/lpunpack super_antes.img originais
cp originais/vendor.img vendor_atual.img
cp originais/product.img product_atual.img
cp originais/system_ext.img system_ext_atual.img
```

Ferramentas comunitárias fixadas por commit e hash, já utilizadas na montagem do projeto; não se afirma auditoria completa do código.

O layout conferido no projeto: super 3303014400 bytes; metadata máxima 65536; 2 slots de metadata; grupo main máximo 3298820096; system/vendor/product/system_ext readonly sem sufixos de slots. Dois slots de metadata não significam automaticamente aparelho A/B.

Os hashes esperados pelo script para vendor/product/system_ext são:
- vendor: 6594a216453065b3b02efba11a20b2f12c6b6397e52e4014c1f3dbc0355e1451
- product: 88808d75976626d278006e97bbe09e0a5e75601c874df1d4e75900712b5a5075
- system_ext: f69cae008ab17cb767e535df6e331f6c0659c710c4d92782ebf917a3ddc7cfad

Esses são componentes do ambiente do projeto, não hashes universais de todo aparelho S7. Product/system_ext da ROM Samsung original podem diferir. Se diferirem, parar; essa combinação não foi validada pela receita.

## 6. Montar e conferir super

No Linux/WSL, na mesma pasta:

```bash
curl -fL "https://raw.githubusercontent.com/joaosilveira20051011-rgb/galaxy-a03core-a032m/main/scripts/montar-super-crdroid.sh" -o montar-super-crdroid.sh
bash montar-super-crdroid.sh
```

O script confere ferramentas e entradas, monta a imagem e extrai novamente as quatro partições para comparar byte a byte. Ele não grava no aparelho. Não ignorar falha de hash, tamanho, lpmake ou comparação.

Saída: super_crdroid_10.13_a032m_s7_raw.img
Tamanho: 3303014400 bytes
SHA-256 registrado da montagem de referência:
```text
1336913ec0f1989d7d62d136560b9aca7bb17a648e7c9576d5fa754cecdf0f09
```

A mensagem antiga do script “teste no aparelho pendente” descreve a etapa de preparação original. A GSI posteriormente iniciou no aparelho, mas isso não homologa outra combinação de entradas.

## 7. Preparar AP contendo SOMENTE super.img

No Linux/WSL, o Python 3 empacota a imagem sob o nome correto sem fazer uma segunda cópia dela:

```bash
python3 - <<'PY'
import hashlib, tarfile
from pathlib import Path
src = Path("super_crdroid_10.13_a032m_s7_raw.img")
out = Path("AP_crDroid_10.13_A032M_S7_SUPER_ONLY.tar")
assert src.stat().st_size == 3303014400
with src.open("rb") as f:
    digest = hashlib.sha256()
    for block in iter(lambda: f.read(1048576), b""):
        digest.update(block)
assert digest.hexdigest() == "1336913ec0f1989d7d62d136560b9aca7bb17a648e7c9576d5fa754cecdf0f09"
assert not out.exists(), "Saida existente; conservar/mover antes de repetir."
with tarfile.open(out, "w", format=tarfile.USTAR_FORMAT) as t:
    info = tarfile.TarInfo("super.img")
    info.size = src.stat().st_size
    info.mode = 0o644
    with src.open("rb") as f:
        t.addfile(info, f)
with tarfile.open(out, "r:") as t:
    assert t.getnames() == ["super.img"]
    f = t.extractfile("super.img")
    digest = hashlib.sha256()
    for block in iter(lambda: f.read(1048576), b""):
        digest.update(block)
    assert digest.hexdigest() == "1336913ec0f1989d7d62d136560b9aca7bb17a648e7c9576d5fa754cecdf0f09"
print("TAR conferido: somente super.img, hash correspondente.")
PY
```

Esta preparação SUPER_ONLY deriva da super validada, evitando carregar vbmeta. **Esse novo nome/pacote não foi gravado num segundo teste físico independente.** A instalação original usou um AP que também alterava vbmeta e depois restaurou o vbmeta original; não repetir essa parte malsucedida.

Voltar ao CMD com exit e conferir:

```cmd
tar -tf "%USERPROFILE%\Downloads\A03_GSI\AP_crDroid_10.13_A032M_S7_SUPER_ONLY.tar"
certutil -hashfile "%USERPROFILE%\Downloads\A03_GSI\AP_crDroid_10.13_A032M_S7_SUPER_ONLY.tar" SHA256
```

A listagem deve conter **somente super.img**. Não renomear a GSI bruta para .tar.

Preparar a restauração no Linux/WSL, na mesma pasta:

```bash
python3 - <<'PY'
import hashlib, tarfile
from pathlib import Path
src = Path("super_antes.img")
out = Path("AP_RESTAURAR_SEU_SUPER.tar")
assert src.stat().st_size == 3303014400
assert not out.exists(), "Saida existente; conservar/mover antes de repetir."
def sha(stream):
    d = hashlib.sha256()
    for b in iter(lambda: stream.read(1048576), b""):
        d.update(b)
    return d.hexdigest()
with src.open("rb") as f:
    original = sha(f)
with tarfile.open(out, "w", format=tarfile.USTAR_FORMAT) as tar:
    info = tarfile.TarInfo("super.img")
    info.size = src.stat().st_size
    info.mode = 0o644
    with src.open("rb") as f:
        tar.addfile(info, f)
with tarfile.open(out, "r:") as tar:
    assert tar.getnames() == ["super.img"]
    assert sha(tar.extractfile("super.img")) == original
print("Restauracao conferida; SHA256 do super original:", original)
PY
```

Conservar super_antes.img e AP_RESTAURAR_SEU_SUPER.tar fora do telefone. Sem restauração pronta, não avançar.

## 8. Instalar pelo Odin — ambiente compatível

Esta etapa substitui super e o sistema. Só executar depois de resolver compatibilidade do boot/AVB, conferir entradas e preparar recuperação. A autorização de outro proprietário deve ser obtida antes da gravação.

Na pasta platform-tools, CMD:

```cmd
adb -s %A03_SERIAL% reboot download
```

No Odin:
- Aguardar reconhecimento em ID:COM.
- AP: AP_crDroid_10.13_A032M_S7_SUPER_ONLY.tar.
- BL, CP, CSC e USERDATA vazios.
- Re-Partition, Nand Erase e Flash Lock desmarcados; não carregar PIT.
- Não incluir vbmeta, boot ou DTBO nessa etapa.
- No teste original, Auto Reboot estava desmarcado e F. Reset Time marcado.
- Start; aguardar PASS antes de desconectar/reiniciar.
- Com a gravação concluída, usar reinicialização confirmada do aparelho; na referência Power + Volume Menos força reinício. Não fazê-lo durante a transferência.

O processo original preservou o boot Magisk existente. Não foi validada aqui a aceitação desta GSI pelo boot Samsung original apenas desbloqueado. Não modificar flags de vbmeta por tentativa.

Troca de sistema pode exigir limpeza de dados conforme a ROM anterior/encriptação; no projeto não foi registrado factory reset na etapa inicial. Portanto, **não há promessa de preservar todos os dados**, nem uma ordem genérica de formatar. Erro de encriptação/boot exige analisar o caso antes de executar wipe.

## 9. Confirmar e testar

```cmd
adb -s %A03_SERIAL% shell getprop sys.boot_completed
adb -s %A03_SERIAL% shell getprop ro.build.version.release
adb -s %A03_SERIAL% shell getprop ro.product.cpu.abilist
adb -s %A03_SERIAL% shell getprop ro.build.fingerprint
adb -s %A03_SERIAL% shell uname -a
```

Esperado: boot_completed 1, Android 14, ABI ARM32 e identificação crDroid correspondente. Primeiro boot pode ser mais demorado; PASS do Odin não prova boot.

Testar toque/tela, Wi-Fi, Bluetooth, chamadas/dados, áudio, câmera, rotação, suspensão, carregamento e reinicialização. Registrar o que realmente foi testado.

O kernel OC2 é instalação separada: [tutorial OC2](TUTORIAL-OC2-THERMAL.md). Não usá-lo para encobrir falha de instalação da GSI.

## 10. Recuperação

Se a GSI não iniciar, retornar ao Download Mode pela rota previamente confirmada e restaurar o TAR do **próprio super anterior**. Preservar as opções de gravação restritas a AP. Se o boot também foi alterado, a restauração correspondente é outro procedimento.

Não usar automaticamente o velho AP_crDroid_10.13_A032M_S7_EXPERIMENTAL.tar.gz: ele contém super.img e vbmeta.img, e a alteração de vbmeta causou bootloop no teste original.

Restaurar super não recupera userdata formatada nem substitui firmware de recuperação. Não realizar outras gravações por tentativa.

## Referências e limites

[Montagem auditada](montagem-super-crdroid-validada.md), [teste Odin histórico](teste-odin-2026-10-13.md), [estado funcional](estado-funcional-2026-10-13.md), [incidente AVB](bootloop-primeiro-teste.md).

Esta é documentação da reprodução no ambiente correspondente, com verificações objetivas. Não declarar compatibilidade universal nem apresentar um aparelho Samsung original apenas desbloqueado como ponto de partida já testado.
