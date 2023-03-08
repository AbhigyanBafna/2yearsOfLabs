.model small
.data
a db 96H
.code
mov ax,@data
mov ds,ax
mov al,a
and al,0f0h
mov cl,04h
rcr al,cl
mov bh,al
call disp
mov al,a
and al,0fh
mov bh,al
call disp
mov ah,4cH
int 21H
disp proc near
mov ch,02h
mov cl,04h
l2: rol bh,cl
mov dl,bh
and dl, 0fH
cmp dl,09
jbe l4
add dl,07
l4: add dl,30H
mov ah,02
int 21H
dec ch
jnz l2
mov ah,02h
mov dl,''
int 21h
endp
ret
end

