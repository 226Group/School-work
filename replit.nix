{pkgs}: {
  deps = [
    pkgs.docker-compose_1
    pkgs.nvidia-podman
    # pkgs.systemd
    # pkgs.docker
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
    pkgs.ghc
    pkgs.tree
  ];
}