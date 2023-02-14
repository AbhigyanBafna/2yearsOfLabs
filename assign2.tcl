#Creating simulator object
set ns [new Simulator]

#Define different colors to differentiate.
$ns color 1 Blue
$ns color 2 Red

#Opening the NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Defining a finish Procedure
proc finish {} {
        global ns nf
        $ns flush-trace
	#Closing and executing NAM file
        close $nf
        exec nam out.nam &
        exit 0
        }

#Creating four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

#Creating duplex links
$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n3 2Mb 20ms DropTail

#Set Queue Size of first link
$ns queue-limit $n0 $n1 5

#Giving node positions (for NAM)
$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n1 $n3 orient right-down

#Monitor the queue for first link
$ns duplex-link-op $n0 $n1 queuePos 0.5

#Setting up TCP connections
set tcp1 [new Agent/TCP]
$ns attach-agent $n0 $tcp1
set tcp2 [new Agent/TCP]
$ns attach-agent $n0 $tcp2
set sink1 [new Agent/TCPSink]
$ns attach-agent $n2 $sink1
set sink2 [new Agent/TCPSink]
$ns attach-agent $n3 $sink2
$ns connect $tcp1 $sink1
$ns connect $tcp2 $sink2
$tcp1 set fid_ 1
$tcp2 set fid_ 2

#Setting up FTP over TCP connections
set ftp [new Application/FTP]
$ftp attach-agent $tcp1
set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp2

#Scheduling the FTP Traffic
$ns at 0.1 "$ftp start"
$ns at 0.1 "$ftp1 start"
$ns at 4.0 "$ftp stop"
$ns at 4.0 "$ftp1 stop"
$ns at 5.0 "finish"

#Run the simulation
$ns run









