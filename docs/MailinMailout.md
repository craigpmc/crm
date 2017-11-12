# Mailin/out


## Introduction

[Mailin/Mailout specs](../specs/MailinMailout.md)


## Development setup
The current development setup is 
- postfix on your local machine
- run CRM mailer command in a docker (let's say 172.17.0.3)

### Postfix configurations
```
ahmed@ahmedheaven:/opt/ubuntumachine/crm  git:(master*) $ cat /etc/postfix/main.cf
# See /usr/share/postfix/main.cf.dist for a commented, more complete version


# Debian specific:  Specifying a file name will cause the first
# line of that file to be used as the name.  The Debian default
# is /etc/mailname.
#myorigin = /etc/mailname

smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
biff = no

# appending .domain is the MUA's job.
append_dot_mydomain = no

# Uncomment the next line to generate "delayed mail" warnings
#delay_warning_time = 4h

readme_directory = no

# TLS parameters
smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

# See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
# information on enabling SSL in the smtp client.

smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
myhostname = ahmedheaven
mydomain = ahmedheaven
#mydestination = $myhostname, ahmedheaven.com, mail.local localhost, $mydomain
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
mydestination = $myhostname, ahmedheaven, localhost.localdomain, localhost
relayhost = 172.17.0.3:6700 
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
inet_protocols = all
```
> The relayhost is docker ip followed by the port u want to forward mail to which in this case is 172.17.0.3:6700


### Mailer configuration
- `EMAIL_SUPPORT` to send emails coming to support.
- Environment variable `SENDGRID_API_KEY` to be able to send emails.