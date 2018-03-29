#!/bin/sh
pylint --load-plugins pylint_django api/ backend/ dosen/ mahasiswa/ models/ pa/ sekre/ --reports=y
