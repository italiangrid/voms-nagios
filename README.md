### VOMS Nagios probes

The Virtual Organization Membership Service is a Grid attribute authority which
serves as central repository for VO user authorization information, providing
support for sorting users into group hierarchies, keeping track of their roles
and other attributes in order to issue trusted attribute certificates and
assertions used in the Grid environment for authorization purposes.

The VOMS Admin service is a web application providing tools for administering
the VOMS VO structure. It provides an intuitive web user interface for daily
administration tasks

This package provides a Nagios probe to check VOMS Admin service status for
a given VO.

For more information:

~~~
voms-admin-probe --help
~~~

Usage example
-------------

~~~
# voms-admin-probe --hostname voms.cern.ch --vo atlas \
                   --cert /etc/grid-security/hostcert.pem \
                   --key /etc/grid-security/hostkey.pem 
~~~

VOMS Admin for VO atlas up and running.

~~~
# echo $?
0
~~~

Contact
-------

If you have problems, questions, ideas or suggestions, please contact us at
the following URLs

   * GGUS (official support channel): http://www.ggus.eu
   * VOMS Product Team list: voms-product-team@lists.cnaf.infn.it
   * VOMS nagios probe source: https://github.com/italiangrid/voms-nagios
