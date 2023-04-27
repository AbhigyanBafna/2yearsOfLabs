#Takes name and surname as cmdline input. Makes a directory of the surname, then inside it writes
# a hello world program with filename: name.c and executes it.
mkdir $2
cd $2
touch "$1.c"
echo '#include <stdio.h>

int main() {
    // Write C code here
    printf("Hello world");

    return 0;
}' > "$1.c"
gcc "$1.c" -o $1
./$1
