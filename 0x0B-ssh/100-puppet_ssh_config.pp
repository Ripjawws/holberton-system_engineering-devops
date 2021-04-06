# puppet
file_line { 'identity':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/etc/ssh/ssh_config',
}
file_line {'password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}