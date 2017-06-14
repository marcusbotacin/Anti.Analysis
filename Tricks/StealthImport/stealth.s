	.file	"t.c"
	.intel_syntax noprefix
	.section	.rodata
.LC0:
	.string	"Hello World!"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	mov	edi, OFFSET FLAT:.LC0
	call	puts
	# trick init
	# chain
	mov	eax, [fs:0x0]
	# -1 or 0xFFFFFFFF
	cmp	dword ptr [eax], -1
	mov 	eax, [eax]
	# handler offset
	mov	eax, [eax+0x4]
	# page alignment
	and	eax, 0xFFFF0000
	#MZ
	cmp	word ptr [eax], 0x4d5a
	sub	eax, 0x10000
	# offset
	mov 	bx, [eax+0x3c]
	movzx	ebx, bx
	add	eax, ebx
	# PE
	mov	bx, 0x5045
	cmp	[eax], ebx
	# offset IMAGE_DATA_DIR
	add	eax, 0x78
	mov	eax, [eax]
	# image_base_address
	add	eax, 0x12345678
	mov	eax, [eax+0xc]
	add	eax, 0x12345678
	# ordinary code
	mov	eax, 0
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.2) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
