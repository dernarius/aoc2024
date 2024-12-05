{
  outputs = { self, nixpkgs }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      pythonEnv = pkgs.python312.withPackages(ps: with ps; [
        networkx
      ]);
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = [
          pythonEnv
        ];
      };
    };
}
