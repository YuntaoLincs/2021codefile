# Unix tool using in OS

1. gdb
    1. instruction
        layout src
        layout asm
        si
        wb
    time travel debug
        record full
        record stop
        rsi
2. Qemu
3. perf (record the program running information and use it to optimize the program)

unix instruction:
1. ps ( process status )
    1. pstree ( print it with a tree graph)
2. tree (+ filename) (show the structure of the file) 
3. strace (trace the syscalls)
    1. -T ( adding the time line)
4. kill ( with the pid, can kill the process forcefully)