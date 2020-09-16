set -e

NAME="blender-2.90.0-linux64"
NAMETAR="${NAME}.tar.xz"
CACHE="${HOME}/.blender-cache"
TAR="${CACHE}/${NAMETAR}"
URL="https://mirror.clarkson.edu/blender/release/Blender2.90/${NAMETAR}"

echo "Installing Blender ${NAME}"
mkdir -p $CACHE
if [ ! -f $TAR ]; then
    wget -O $TAR $URL
fi
tar -xf $TAR -C $HOME

echo "export PATH=${PATH}:\"${HOME}/${NAME}\"" > .envs