set -eu

cd "$(git rev-parse --show-toplevel)"


echo "from https://johnvansickle.com/ffmpeg/"
echo "only for ubuntu amd 64"

cd bin
wget "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
mkdir -p ffmpeg_folder
tar -xvf "ffmpeg-release-amd64-static.tar.xz" -C ffmpeg_folder --strip-components 1

cd ffmpeg_folder
ls -al


echo "all done"
