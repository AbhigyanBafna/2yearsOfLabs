#Sets Filepath and gets info about stuProf.txt
filepath=$(pwd)
filepath+="/stuProf.txt"

lines=`wc -l < $filepath`
words=`wc -w < $filepath`
chars=`wc -m < $filepath`
bytes=`wc -c < $filepath`

echo "Number of lines: $lines"
echo "Number of words: $words"
echo "Number of characters: $chars"
echo "Number of bytes: $bytes"

