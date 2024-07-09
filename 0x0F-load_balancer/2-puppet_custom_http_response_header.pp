# Define a class to manage nginx and custom header
class nginx_custom_header {

  # Update package lists and ensure nginx is installed
  exec { 'update_apt':
    command => '/usr/bin/apt-get update',
    path    => ['/usr/bin', '/bin'],
    unless  => '/usr/bin/dpkg -s nginx | /bin/grep "Status: install ok installed"',
  }

  package { 'nginx':
    ensure  => present,
    require => Exec['update_apt'],
  }

  # Define nginx configuration file to add custom header
  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => file,
    content => "add_header X-Served-By \"${hostname}\";",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  # Ensure nginx service is running and start if necessary
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

}
