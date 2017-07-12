node default {
  host { 'puppet.londonappleadmins.org.uk':
    ensure => 'present',
    name => 'puppet.londonappleadmins.org.uk',
    ip => '192.168.33.10',
  }
}
