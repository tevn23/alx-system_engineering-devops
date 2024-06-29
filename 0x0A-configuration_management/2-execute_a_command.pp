# Kills a process named killmenow
exec { 'kill_killmenow':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  path        => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
