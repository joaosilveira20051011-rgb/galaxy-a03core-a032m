#!/usr/bin/env bash
set -euo pipefail
# Linux x86_64 ou WSL. Executar na pasta que contém os quatro arquivos.
# Este script monta e valida uma imagem; não grava no celular.
for cmd in curl sha256sum stat cmp; do command -v "$cmd" >/dev/null; done
mkdir -p tools roundtrip
base="https://raw.githubusercontent.com/itsNileshHere/android-lptools/b7b5c09916ab88074692006db7dab34256da6e24/bin"
for tool in lpmake lpdump lpunpack; do
  curl --fail --location --retry 3 "$base/$tool" --output "tools/$tool"
done
sha256sum --check <<'HASHES'
bca9880b1ab76a5718e885158658a968d49c34c33d2242aadec870207bd581d3  tools/lpmake
da0eeb6e3cafc471df3199f681fb9d7d0ad5421763101baa05bb149ead7a7a4b  tools/lpdump
3c01cd0c4a5bb5c596617e236951c004bbacb91da7d8b33d9bf4d78e4dd1b0b5  tools/lpunpack
ae15ae5541e51509e574eab7cf6c71cae60d5a69483816a7f8773579c729d1d6  crDroid-10.13-a64_bvN-Unofficial.img
6594a216453065b3b02efba11a20b2f12c6b6397e52e4014c1f3dbc0355e1451  vendor_atual.img
88808d75976626d278006e97bbe09e0a5e75601c874df1d4e75900712b5a5075  product_atual.img
f69cae008ab17cb767e535df6e331f6c0659c710c4d92782ebf917a3ddc7cfad  system_ext_atual.img
HASHES
chmod +x tools/lpmake tools/lpdump tools/lpunpack
out="super_crdroid_10.13_a032m_s7_raw.img"
test ! -e "$out" || { echo "Saída já existe; mova-a antes de repetir."; exit 1; }
tools/lpmake --metadata-size 65536 --metadata-slots 2 --super-name super \
  --device super:3303014400:1048576:0 --group main:3298820096 \
  --partition system:readonly:2089295872:main --image system=crDroid-10.13-a64_bvN-Unofficial.img \
  --partition vendor:readonly:407756800:main --image vendor=vendor_atual.img \
  --partition product:readonly:2621440:main --image product=product_atual.img \
  --partition system_ext:readonly:2621440:main --image system_ext=system_ext_atual.img \
  --force-full-image --output "$out"
test "$(stat -c %s "$out")" = 3303014400
tools/lpdump "$out" | tee super-layout.txt
tools/lpunpack "$out" roundtrip
cmp crDroid-10.13-a64_bvN-Unofficial.img roundtrip/system.img
cmp vendor_atual.img roundtrip/vendor.img
cmp product_atual.img roundtrip/product.img
cmp system_ext_atual.img roundtrip/system_ext.img
sha256sum "$out" | tee super-sha256.txt
echo "Montagem validada. AVB/verity e teste no aparelho continuam pendentes."
