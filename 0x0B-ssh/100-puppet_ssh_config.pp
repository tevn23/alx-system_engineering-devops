# Puppet manifest to configure SSH client
file { '~/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '~/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => 'Host myserver
    HostName 18.206.206.134
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ',
}

file { '~/.ssh/school':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  source => 'puppet://~/ssh/school',
}
