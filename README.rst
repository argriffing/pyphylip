
About pyphylip
==============

Read and write files in the phylip sequence format_.


Installation
============

Because pyphylip has been packaged for pypi,
it can be installed using::

    $ pip install pyphylip


Usage
=====

Decode a phylip sequence file given a source of lines in the file::

    >>> with open('infile.phy') as f:
    ...     headers, sequences = pyphylip.decode(f)

Encode some headers and corresponding sequences as a phylip sequence file::

    >>> with open('outfile.phy', 'w') as f:
    ...     f.write(pyphylip.encode(headers, sequences) + '\n')


.. _format: http://evolution.genetics.washington.edu/phylip/doc/sequence.html
