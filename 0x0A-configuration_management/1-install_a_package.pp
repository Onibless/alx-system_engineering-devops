# install puppet-lint with the use of Puppet

package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
