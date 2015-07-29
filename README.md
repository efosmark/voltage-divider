Voltage Divider Calculation
===========================

Often times it's desired to find resistor values that will provide
a given output voltage for a given input voltage. This Python package
allows that calculation to be done easily.

It also allows you to find R1 and R2 values for a given 
[EIA value set](http://www.logwell.com/tech/components/resistor_values.html).
The current options being E3, E6, E12, E24 (default), E48, and E96.


Usage
-----

The package can either be used as a Python resource, or can be used directly on
the command-line for quick calculations.

As a Python resource:

	>>> import voltagedivider
	>>> from voltagedivider import divider
	>>> from voltagedivider import divider, eia
	>>> divider.calc_voltage_divider_resistance_values(3, 5)
	(1.0, 1.5)
	>>> divider.calc_voltage_divider_resistance_values(3, 5, value_set=eia.E48)
	(1.33, 1.96)

From the command line:

	$ python3 voltagedivider/divider.py 3 5
	Closest match (using E24 value set):
	  R1 decade:   1.0
	  R2 decade:   1.5
	  V out:       3.0 volts

	$ python3 voltagedivider/divider.py 3 5 --value_set=E48
	Closest match (using E48 value set):
	  R1 decade:   1.33
	  R2 decade:   1.96
	  V out:       2.98 volts


Author
------

Evan Fosmark <evan.fosmark@gmail.com>