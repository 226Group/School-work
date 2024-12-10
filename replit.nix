{pkgs}: {
  deps = [
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


# { pkgs ? import <nixpkgs> {} }:
# let
#   myContainer = pkgs.dockerTools.buildImage {
#     name = "my-simple-container";
#     tag = "latest";

#     # Specify the contents of the container
#     contents = [
#       # pkgs.docker
#     ];

#     # Optionally, you can specify a command to run when the container starts
#     config = {
#       Cmd = [ "bash" ]; # or any other command you want to run
#     };
#   };
# in
# {
#   inherit myContainer;
# }


# { pkgs ? import <nixpkgs> {} }:

# pkgs.mkShell {
#   buildInputs = [ 
#     pkgs.postgresql
#     pkgs.pg_ctl
#   ];
# }