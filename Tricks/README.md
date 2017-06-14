# Tricks

## Implemented tricks

* *GarbageBytes*: Add extra bytes to make analysis harder.
* *IsDebuggerPresent*: Check debuggers presence.
* *ProgramControlFlowChange*: Obfuscate taken branches.
* *SizeOfImage*: A known packing technique.
* *CPUInstructionsResultsComparison*: Check LDT,IDT values.
* *HardwareBreakpoints*: Check for hardware breakpoints.
* *LDR*: Direct address resolving.
* *PushPopMath*: Obfuscated constants.
* *SoftwareBreakpoint*: Check for trap flag/breakpoint.
* *FakeConditionalJumps*: Control flow obfuscation.
* *HeapFlags*: Check PEB flags.
* *NOPSequence*: Pattern Matching evasion.
* *PushRet*: Control flow change.
* *SSRegister*: Debugger evasion.
* *FakeRet*: Make a *CALL* using a *RET*.
* *HookDetection*: Detect a *JMP* instruction.
* *NtGlobalFlag*: Check PEB flags.
* *StealthImport*: Use functions without explicit importing it. This example needs to be completed in order to proper work.

## Compilation

For compiling using GCC, use the *compile.sh* script. If you want to compile for Windows, you can use [MinGW](www.mingw.org).
