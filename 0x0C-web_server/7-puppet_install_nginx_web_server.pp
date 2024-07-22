# Install and manage Nginx service
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

# Allow Nginx through the firewall
firewall { '001 allow nginx':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}

# Set up web files and permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => $facts['user'],
  group   => $facts['user'],
  mode    => '0755',
  recurse => true,
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/error_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Backup default index file
file { '/var/www/html/index.nginx-debian.html.bckp':
  ensure  => file,
  source  => '/var/www/html/index.nginx-debian.html',
  backup  => false,
}

# Configure Nginx redirection and 404 page
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 0.0.0.0:80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com;
    }

    error_page 404 /error_404.html;
}
",
}

# Reload Nginx to apply changes
exec { 'reload_nginx':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
