#Creating simulator object
set ns [new Simulator]

#Creating and Opening the nam file
set nf [open out.nam w]
$ns namtrace-all $nf

#Defining a finish Procedure
proc finish {} {
        global ns nf
        $ns flush-trace
        close $nf
        exec nam out.nam &
        exit 0
        }
        
#Creating 2 nodes
set n0 [$ns node]
set n1 [$ns node]

#Creating a duplex link
$ns duplex-link $n0 $n1 2Mb 10ms DropTail

#Setting max queue size.
$ns queue-limit $n0 $n1 5

#Monitor the queue for the link
$ns duplex-link-op $n0 $n1 queuePos 0.5

#Setting up a TCP agent
set tcp1 [new Agent/TCP]
$ns attach-agent $n0 $tcp1
set sink1 [new Agent/TCPSink]
$ns attach-agent $n1 $sink1

#Connecting TCP agent with Sink agent
$ns connect $tcp1 $sink1

$tcp1 set fid_ 1

#Creating FTP agent and attaching it to tcp1
set ftp [new Application/FTP]
$ftp attach-agent $tcp1

#Scheduling the FTP Traffic
$ns at 0.1 "$ftp start"
$ns at 4.0 "$ftp stop"
$ns at 5.0 "finish"

#Runs the simulation
$ns run
