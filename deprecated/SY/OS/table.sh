echo "Enter the number -"
read n
i=1
while [ $i -le 12 ]
do
let res="$i * $n"
echo "$n x $i = $res"
((i++))
done
