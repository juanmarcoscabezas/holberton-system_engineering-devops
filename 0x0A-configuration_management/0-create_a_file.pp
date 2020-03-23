# Creates a file called holberotn in /tmp directory

file { "holberton":
	path    => "/tmp/holberton",
	ensure  => "file",
	content => "I love Puppet",
	group   => "www-data",
	mode    => "0744",
	owner   => "www-data",
}
