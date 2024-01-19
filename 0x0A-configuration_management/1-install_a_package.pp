# 1-install_a_package.pp installs flask

package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
