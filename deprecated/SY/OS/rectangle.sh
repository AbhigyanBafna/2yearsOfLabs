echo "Enter Length of Rectangle : "
read l
echo "Enter Breadth of Rectangle : "
read b 
let area="$l * $b"
let peri="2 * ($l + $b)"
echo "Perimeter is : $peri"
echo "Area is : $area"

