file { 'ssh_config':
  path    => '/home/masa2024/.ssh/config',
  ensure  => file,
  mode    => '0600',
  owner   => 'masa2024',
  group   => 'masa2024',
  content => template('ssh/ssh_config.erb'),
}

file { '/home/masa2024/.ssh':
  ensure => directory,
  owner  => 'masa2024',
  group  => 'masa2024',
  mode   => '0700',
}
