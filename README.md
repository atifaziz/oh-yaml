# Offline YAML Parser

A version of [Online YAML Parser] that can be run as a local program.

Usage:

    python app.py [ json | python | canonical-yaml ] < YAML

The program reads a YAML document from standard input and prints the specified
format (`json`, `python` or `canonical-yaml` where `json` is the default if
none is specified) to standard output.

If the YAML is invalid then the exit code is non-zero. Otherwise it is zero to
conventionally indicate success.

See the `examples` folder for examples of YAML documents.

On Windows, use [Pie] (included) for a non-intrusive Python installation.

To build a Docker image to use, run:

    docker build -t oh-yaml .

Example of running the image:

    $ cat examples/2.01 | docker run --name oh-yaml --rm -i oh-yaml

If on Windows, use the following command-line instead:

    > type examples\2.01 | docker run --name oh-yaml --rm -i oh-yaml


[Online YAML Parser]: http://yaml-online-parser.appspot.com/
[Pie]: https://github.com/atifaziz/pie.ps
