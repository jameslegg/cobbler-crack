cobbler-crack.py
================

A tiny little replacment for the ENC in cobbler that parses the default json seralized files and produces the same output as cobblers built in ENC.

Useful for when a rapidly expanding puppet installation starts hammering the 
crap out of cobblerd and you just can't make it go fast enough.
This fapws based python webserver might be good enough until you can get around
to upgrading cobblers backend or building somthing better.

# Requires
* http://www.fapws.org/
* http://software.schmorp.de/pkg/libev.html
* python-yaml

# Issues
* very little testing
* settings files not yet parsed
* this is a fairly stupid idea
