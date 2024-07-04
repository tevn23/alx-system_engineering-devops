# Puppet manifest to configure SSH client
file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
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

file { '/home/ubuntu/.ssh/school':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  source => 'puppet:///modules/ssh/school', # Make sure the private key is available in the module files
}
