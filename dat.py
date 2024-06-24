from ghidra.program.model.listing import Listing
from ghidra.program.model.symbol import SymbolUtilities
from ghidra.util.task import ConsoleTaskMonitor

listing = currentProgram().getListing()
function = getFunction("main")
function_body = function.getBody()
instruction_iterator = listing.getInstructions(function_body, True)

for instruction in instruction_iterator:
    references = instruction.getReferencesFrom()
    for reference in references:
        if reference.isMemoryReference():
            ref_address = reference.getToAddress()
            symbol = getSymbolAt(ref_address)
            if symbol is not None and symbol.isGlobal():
                print(f"Global data accessed at {instruction.getAddress()}: {symbol.getName()}") if "DAT" in symbol.getName() else next
