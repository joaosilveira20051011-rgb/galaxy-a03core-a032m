#!/usr/bin/env bash
# Stock baseline only. Boot success must be tested separately.
set -euo pipefail
SOURCE=$(realpath "${1:?Usage: build-kernel-stock.sh SOURCE OUTPUT}")
OUTPUT=$(realpath -m "${2:?Usage: build-kernel-stock.sh SOURCE OUTPUT}")
PROJECT=$(cd "$(dirname "$0")/.." && pwd)
: "${CLANG_ROOT:?Use verified official clang-r383902 directory}"
: "${CROSS_ROOT:?Use verified AOSP aarch64-linux-android-4.9 binutils directory}"
export PATH="$CLANG_ROOT/bin:$PATH"
export BSP_BUILD_FAMILY=sharkl3 BSP_BUILD_ANDROID_OS=y
export DTC_OVERLAY_TEST_EXT="$SOURCE/tools/mkdtimg/ufdt_apply_overlay"
export DTC_OVERLAY_VTS_EXT="$SOURCE/tools/mkdtimg/ufdt_verify_overlay_host"
mkdir -p "$OUTPUT"
REFERENCE="$PROJECT/kernel/reference/A032MUBS7CZA5.config"
cp "$REFERENCE" "$OUTPUT/.config"
ARGS=(-C "$SOURCE" O="$OUTPUT" ARCH=arm64 CC=clang LD=ld.lld
 CLANG_TRIPLE=aarch64-linux-gnu- CROSS_COMPILE="$CROSS_ROOT/bin/aarch64-linux-android-"
 BSP_BUILD_DT_OVERLAY=y)
if [[ -n "${HOSTTOOLS_ROOT:-}" ]]; then
 export PATH="$HOSTTOOLS_ROOT/usr/bin:$PATH"
 export BISON_PKGDATADIR="$HOSTTOOLS_ROOT/usr/share/bison"
 export LD_LIBRARY_PATH="$HOSTTOOLS_ROOT/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
 ARGS+=(HOSTCFLAGS="-I$HOSTTOOLS_ROOT/usr/include"
 HOSTLDFLAGS="-L$HOSTTOOLS_ROOT/usr/lib/x86_64-linux-gnu")
fi
make "${ARGS[@]}" olddefconfig 2>&1 | tee "$OUTPUT/configure.log"
diff -u "$REFERENCE" "$OUTPUT/.config" > "$OUTPUT/config.diff" || test "$?" = 1
test ! -s "$OUTPUT/config.diff"
make "${ARGS[@]}" LOCALVERSION=-27418755 BUILD_NUMBER=A032MUBS7CZA5 \
 -j"${JOBS:-6}" Image modules dtbs 2>&1 | tee "$OUTPUT/build.log"
cmp "$REFERENCE" "$OUTPUT/.config"
