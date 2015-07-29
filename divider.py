import eia

def calc_vout(vin, r1, r2):
	return (r2 / (float(r1) + float(r2))) * vin

def calc_voltage_divider_resistance_values(vout, vin, value_set=eia.E24):
	closest_vout = None
	closest_r1 = None
	closest_r2 = None
	for i, r1_value in enumerate(value_set):
		for j, r2_value in enumerate(value_set):
			new_vout = calc_vout(vin, r1_value, r2_value)
			if closest_vout is None or abs(new_vout - vout) < abs(closest_vout - vout):
				closest_vout = new_vout
				closest_r1 = r1_value
				closest_r2 = r2_value
	return closest_r1, closest_r2

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Calculates the decade values for R1 and R2 that will provide the closest output voltage to the specified voltage.')
	parser.add_argument('vout', type=float, help='Desired voltage out')
	parser.add_argument('vin', type=float, help='Voltage in')
	parser.add_argument('--value_set', type=str, default='E24', help='Either `E12` or `E24`')
	args = parser.parse_args()

	value_set_name = args.value_set or 'E24'
	if not hasattr(eia, value_set_name):
		raise SystemExit('Invalid value set.')
	value_set = getattr(eia, value_set_name)

	closest_r1, closest_r2 = calc_voltage_divider_resistance_values(args.vout, args.vin, value_set=value_set)
	
	print("Closest match (using {} value set):".format(value_set_name))
	print("  R1 decade:  ", closest_r1)
	print("  R2 decade:  ", closest_r2)
	print("  Vout:       ", round(calc_vout(args.vin, closest_r1, closest_r2), 2), "volts")
