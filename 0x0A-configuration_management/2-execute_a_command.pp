#   Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill_me_now':
  path    => '/usr/bin',
  command => 'pkill -f "killmenow"'
}