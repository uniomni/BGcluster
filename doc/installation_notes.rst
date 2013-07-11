
INSTALLATION NOTES
==================

Install OpenLDAP Server
-----------------------
 * Installing OpenLDAP Server:
 
   * Modify /etc/hosts/::
     
      127.0.1.1       tambora.example.com     tambora
     
   * Install OpenLDAP::
   
      sudo apt-get install slapd ldap-utils
   
   * Modifying/Populating your Database:
   
     Create file ~/sandpit/ldap_config_files/add_content.ldif::
     
      dn: ou=Users,dc=example,dc=com
      objectClass: organizationalUnit
      ou: People

      dn: ou=Groups,dc=example,dc=com
      objectClass: organizationalUnit
      ou: Groups

      dn: cn=modelling,ou=Groups,dc=example,dc=com
      objectClass: posixGroup
      cn: modelling
      gidNumber: 5000

      dn: uid=john,ou=Users,dc=example,dc=com
      objectClass: inetOrgPerson
      objectClass: posixAccount
      objectClass: shadowAccount
      uid: john
      sn: Doe
      givenName: John
      cn: John Doe
      displayName: John Doe
      uidNumber: 10000
      gidNumber: 5000
      userPassword: johnldap
      gecos: John Doe
      loginShell: /bin/bash
      homeDirectory: /home/john
   
     Add the content::
     
      ldapadd -x -D cn=admin,dc=example,dc=com -W -f add_content.ldif

   * Logging:
   
     Create file ~/sandpit/ldap_config_files/logging.ldif::
   
      dn: cn=config
      changetype: modify
      add: olcLogLevel
      olcLogLevel: stats
        
     Implement the change::
     
      sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f logging.ldif

   * LDAP Authentication:

     install libraries on the client that will know how and when to contact it. On Ubuntu, this has been traditionally accomplishd by installing the libnss-ldap package. This package will bring in other tools that will assist you in the configuration step. Install this package now::

      sudo apt-get install libnss-ldap

     You will be prompted for details of your LDAP server. If you make a mistake you can try again using::

      sudo dpkg-reconfigure ldap-auth-config

     The results of the dialog can be seen in /etc/ldap.conf. If your server requires options not covered in the menu edit this file accordingly.

     Now configure the LDAP profile for NSS::

      sudo auth-client-config -t nss -p lac_ldap

     Configure the system to use LDAP for authentication::

      sudo pam-auth-update

   * User and Group Management:

     The ldap-utils package comes with enough utilities to manage the directory but the long string of options needed can make them a burden to use. The ldapscripts package contains wrapper scripts to these utilities that some people find easier to use.

     Install the package::

      sudo apt-get install ldapscripts

     Then edit the file /etc/ldapscripts/ldapscripts.conf to arrive at something similar to the following::

      SERVER=localhost
      BINDDN='cn=admin,dc=example,dc=com'
      BINDPWDFILE="/etc/ldapscripts/ldapscripts.passwd"
      SUFFIX='dc=example,dc=com'
      GSUFFIX='ou=Groups'
      USUFFIX='ou=Users'
      MSUFFIX='ou=Computers'
      GIDSTART=10000
      UIDSTART=10000
      MIDSTART=10000