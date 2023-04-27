set ns [new Simulator]

set anim [open out.nam w]
$ns namtrace-all $anim

proc finish {} {
	global ns anim
	$ns flush-trace
	close $anim
	exec nam out.nam &
	exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns duplex-link $n0 $n1 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 2Mb 10ms DropTail
$ns duplex-link $n3 $n0 2Mb 10ms DropTail

set tcp [new Agent/TCP]
set udp [new Agent/UDP]
set sink [new Agent/TCPSink]
set null [new Agent/Null]
$ns attach-agent $n0 $tcp
$ns attach-agent $n1 $sink
$ns attach-agent $n2 $udp
$ns attach-agent $n3 $null

set ftp [new Application/FTP]
set cbr [new Application/Traffic/CBR]
$ftp attach-agent $tcp
$cbr attach-agent $udp

$ns connect $tcp $sink
$ns connect $udp $null

$ns at 0.1 "$ftp start"
$ns at 0.2 "$cbr start"
$ns at 0.8 "$ftp stop"
$ns at 0.9 "$cbr stop"
$ns at 1.0 "finish"

$ns run

