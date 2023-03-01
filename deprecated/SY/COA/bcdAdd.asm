.model small
.data
a dw 1234H
b dw 5678H
.code
mov ax, @data
mov ds, ax
mov ax, a
mov bx, b
add al, bl
daa
mov bl, al
adc ah, bh
mov al, ah
daa
mov bh, al
mov ch, 04h
mov cl, 04h
l2:rol bx, cl
mov dl, bl
and dl, 0fH
cmp dl, 09
jbe l4
add dl, 07
l4:add dl, 30H
mov ah, 02
int 21H
dec ch
jnz l2
mov ah, 4cH
int 21H
end