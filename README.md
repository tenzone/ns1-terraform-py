# ns1-terraform-py

## Purpose:
the purpose of this script is to pull record information from the ns1 python api client, and then ouput it as terraform HCL.
This makes the import process of large number of records easier, especially writing out the HCL once imported.

### Gotchas
the output format of some multi line answers is wrong. it is an easy fix, but i have not gotten around to fixing it yet
