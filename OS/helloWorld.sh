mkdir $2
cd $2
touch "$1.c"
echo '#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}' > "$1.c"
gcc "$1.c" -o $1
./$1
