#Create a simulator object
set ns [new Simulator]

#Open the NAM trace file
set nr [open out.tr w]
$ns trace-all $nr
set nf [open out.nam w]
$ns namtrace-all $nf

#Define different colors for data flows (for NAM)
$ns color 1 Blue
$ns color 2 Red
$ns color 3 Green

#Define a 'finish' procedure
proc finish {} {
        global ns nr nf
        $ns flush-trace
        #Close the NAM trace file and execute
        close $nf
	close $nr
        exec nam out.nam &
        exit 0
	}

#Create four nodes
for {set i 0} {$i < 4} {incr i 1} {
set n$i [$ns node]
}

#Create links between the nodes
$ns duplex-link $n0 $n3 1Mb 10ms DropTail
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 20ms DropTail
$ns duplex-link $n3 $n1 1Mb 20ms DropTail

#Give node positions (for NAM)
$ns duplex-link-op $n0 $n2 orient right
$ns duplex-link-op $n2 $n3 orient left-down
$ns duplex-link-op $n0 $n3 orient right-down
$ns duplex-link-op $n3 $n1 orient left-down

#Setup a TCP connection
set tcp [new Agent/TCP]
$ns attach-agent $n3 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n2 $sink
$ns connect $tcp $sink
$tcp set fid_ 3

#Setup a FTP over TCP connection
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP


#Setup of UDP connection
set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packet_size_ 1000
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0
set null0 [new Agent/Null]
$ns attach-agent $n2 $null0
$ns connect $udp0 $null0

set udp1 [new Agent/UDP]
$ns attach-agent $n1 $udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packet_size_ 500
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1
set null1 [new Agent/Null]
$ns attach-agent $n3 $null1
$ns connect $udp1 $null1

$udp0 set fid_ 1
$udp1 set fid_ 2

#Schedule events for the CBR and FTP agents
$ns at 0.1 "$cbr1 start"
$ns at 0.5 "$cbr0 start"
$ns at 1.0 "$ftp start"
$ns at 3.5 "$cbr0 stop"
$ns at 4.0 "$cbr1 stop"
$ns at 4.5 "$ftp stop"
$ns at 5.0 "finish"

#Run the simulation
$ns run

