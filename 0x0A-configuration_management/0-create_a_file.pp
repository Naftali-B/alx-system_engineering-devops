# creating a file in /tmp using puppet

file {'school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
}
