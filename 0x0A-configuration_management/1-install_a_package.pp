# install puppet-lint with the use of Puppet

package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem',
}
