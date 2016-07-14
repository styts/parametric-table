# Parametric Workbench/Table

![Editor with preview](/screenshot.jpg?raw=true)

Workbench table built with [OpenScad](http://www.openscad.org/) wrapper
[SolidPython](https://github.com/SolidCode/SolidPython).

Install SolidPython

    pip install SolidPython

To compile

    python workbench.py > output.scad

Best to open your editor in one window, and watch the results live in OpenScad
[_View -> Hide Editor_ mode].

If you're using vim, you can configure compilation on save via an autocommand:

    autocmd BufWritePost workbench.py silent !python <afile> > <afile>_output.scad

The BOM (bill-of-materials) is intended to help you shop for the right
amounts and cuts of wood. This feature is still rather experimental. _Measure
seven times, cut once_, as the proverb goes.
