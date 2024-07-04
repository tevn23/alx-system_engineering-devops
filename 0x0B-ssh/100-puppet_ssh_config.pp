# Puppet manifest to configure SSH client
file { '/root/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/root/.ssh/config':
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

file { '/root/.ssh/school':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  source => 'puppet:///root/ssh/school',
}
