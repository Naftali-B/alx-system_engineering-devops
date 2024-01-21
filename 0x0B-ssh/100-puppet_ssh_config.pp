# Puppet manifest for managing SSH client configuration

exec { 'ssh_config':
  path    => '/bin',
  command => 'echo -e "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}

