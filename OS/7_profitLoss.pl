#Calculates simple profit loss.
print "Enter cost price:";
$cp=<>;
print "Enter selling price:";
$sp=<>;
$profit=$sp-$cp;
if($profit>0)
{
        print "PROFIT=$profit";
}
else
{
        print "LOSS=$profit"
}