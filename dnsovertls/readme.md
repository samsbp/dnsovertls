Start docker in linux by issuing the below command
--> service docker start
TO start the container run
--> docker run -it -v <<file_path_to_the_project_folder>>:/dns ubuntu
Start two containers in seperate terminals and move to the dns folder in both the containers
--> cd dns
the project folder will be available in /dns path in the container
In both the container run,
--> apt-get update && apt-get install python openssl nano net-tools
Consider the two container as container A and container B
In A:
run
--> apt-get install bind9 bind9utils bind9-doc
--> nano /etc/bind/named.conf.options
copy and paste the below cotents in the terminal after the command nano is entered:
options {
	directory "/var/cache/bind";

	// If there is a firewall between you and nameservers you want
	// to talk to, you may need to fix the firewall to allow multiple
	// ports to talk.  See http://www.kb.cert.org/vuls/id/800113

	// If your ISP provided one or more IP addresses for stable
	// nameservers, you probably want to use them as forwarders.  
	// Uncomment the following block, and insert the addresses replacing
	// the all-0's placeholder.

	 forwarders {
	        8.8.8.8;
                8.8.4.4;
	 };
         forward only;

	//========================================================================
	// If BIND logs error messages about the root key being expired,
	// you will need to update your keys.  See https://www.isc.org/bind-keys
	//========================================================================
	dnssec-validation auto;

	auth-nxdomain no;    # conform to RFC1035
	listen-on-v6 { any; };
};

After entering the above command save it using ctrl+x and enter y for yes and issue enter key to save it under the same file name.

Then issue the command as follows,
--> service bind9 start
--> nano /etc/resolv.conf
erase all the contents in the file and paste the below content:
nameserver 127.0.0.1

After entering the above content save it using ctrl+x and enter y for yes and issue enter key to save it under the same file name.

In container B,
run the command as
--> nano dnsclient.py
go to line 20 and change the line as :
secure_socket.connect(('Container_B_ip_address',1000))

Get the ip address of the container by issuing the ifconfig command.

In container A,
run the following command
--> python dnsServer.py

In container B,
--> python dnsclient.py

In the host terminal,
--> nano /etc/resolv.conf
erase all the contents in the file and paste the below content:
nameserver <<ip_address_of_container_A>>

to check whether the setup is working,
issue the following command in host terminal
--> dig google.com

if dig is not found install it using
--> apt-get install dnsutils
