# Backup the default Nginx configuration file
file { '/etc/default/nginx.backup':
  ensure  => 'file',
  source  => '/etc/default/nginx',
  require => Exec['fix--for-nginx'],
}

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/^ULIMIT.*/ULIMIT=4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'test $(grep -c "^ULIMIT=4096$" /etc/default/nginx) -eq 0',
}

# Restart Nginx using service management
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => Exec['fix--for-nginx'],
}
