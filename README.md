# vocore_hwreg
this is a python package created for interfacing with voCore2 hardware registers

# usage
Usage is very simple, package provide 4 methods		
`read(<register addr int>)` - returns register value as python long		

```python
>>>import hwreg
>>> hwreg.read(int("10000060",16))		
1427440910L
>>>
```	
	
`read_bit(register_addr_int,bitPosition)` - returns register bit value at specified position(0-31)

```python
>>>import hwreg
>>>hwreg.read_bit(int("10000060",16),2)		
1L
>>>hwreg.read_bit(int("10000060",16),5)
0L
```	

`write(register_addr_int,value)` - write value to register		
below should turn off vocore2 onboard led
```python
>>>import hwreg
>>>hwreg.write(int("10000644",16),int("1000",16))		
1
```
`write_bit(register_addr_int,bitPosition,bitValue)` - write bit value to register	
below should turn off(0) and on(1) onboard led
```python
>>>import hwreg
>>>hwreg.write_bit(int("10000624",16),12,0)		
1L
>>>hwreg.write_bit(int("10000624",16),12,1)
0L
```
