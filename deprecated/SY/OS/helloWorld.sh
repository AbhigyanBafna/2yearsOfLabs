echo "Enter Name : "
read name
echo "Enter surname : "
read surname 
mkdir $surname
cd $surname
touch "$name.c"
echo "#include <stdio.h>" >> "$name.c"
echo "int main() {" >> "$name.c"
echo "   printf(\"Hello, World!\n\");" >> "$name.c"
echo "   return 0;" >> "$name.c"
echo "}" >> "$name.c"
gcc "$name.c" -o $name
./$name



