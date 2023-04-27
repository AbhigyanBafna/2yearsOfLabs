file_path="/home/lab1003/Desktop/Abhigyan/stuProf.txt"

lines=`wc --lines < $file_path`
words=`wc --words < $file_path`
chars=`wc --chars < $file_path`
bytes=`wc --bytes < $file_path`

echo "Number of lines: $lines"
echo "Number of words: $words"
echo "Number of characters: $chars"
echo "Number of bytes: $bytes"

