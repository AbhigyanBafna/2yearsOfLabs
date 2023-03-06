i=1
while [ $i -le 12 ]
do
let res="$i * $1"
echo "$1 x $i = $res"
((i++))
done
