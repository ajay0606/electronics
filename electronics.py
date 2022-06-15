from math import fsum, sqrt


class SeriesParallel:

    def __init__(self, value = []):
        self.value = value

    def series_calculation(self):
        return f"Calculation for Series (resistance and capacitance) is {fsum(self.value)}"

    def parallel_calculation(self):
        c = 0
        l = []
        for _ in range(len(self.value)):
            x = 1/self.value[c]
            l.append(x)
            c += 1
        x = fsum(l)
        y = 1/x
        return f"Calculation for parallel (resistance and capacitance) is {y:.4f}"

t = SeriesParallel([200,380])
print(t.series_calculation())
print(t.parallel_calculation())




class VoltageDivider:
    '''To calculate Voltage Divider 2 funtions
    -> required_resistor parameters Vin=volts in, Vout=volts out
    , R1=resistor of any value
    ->voltage_divider parameters Vin=volts in, R1=resistor value 1,
    , R2=resistor value 2'''

    def __init__(self,Vin=None, Vout=None, R1=None, R2=None):
        self.Vin = Vin
        self.Vout = Vout
        self.R1 = R1
        self.R2 = R2

    def require_resistor(self):
        '''To calculate required resistor for desire volts
        parameter Vin=Volts in, Vout=Volts out, R1= resistor of any value '''
        r2 = (self.Vout) * (self.R1) / (self.Vin - self.Vout)
        return f"Resistor required for {self.Vout} is {r2}\u03A9"


    def voltage_divider(self):
        '''Voltage divider with 2 resistor for desire volts
        parameters Vin=Volts in, R1= first resistor, R2=second resistor'''
        Vout = self.Vin * (self.R2 / (self.R1 + self.R2))
        return f"To Divide Voltage R1 and R2 in series to get {Vout:.2f} V"

v = VoltageDivider(Vin=9,Vout=3.3,R1=68)
print(v.require_resistor())
#print(v.voltage_divider())


class CurrentDivider:
    '''To calculate current in circuit this is current divider class
    there are 2 main fuctions
    -> branch_current() parameters are volts, power, resistance.
    -> current_in_branch_conductance() parameters are volts, resistance '''

    def __init__(self, volts=None, power=None, resistance=[]):
        self.volts = volts
        self.power = power
        self.resistance = resistance

    def current_divider_on_volts_resistance(self):
        x = [fsum([self.volts / i]) for i in self.resistance]
        return f"Current in each node by parallel resistor value and volts value {x}"

    def total_current_on_power_volts(self):
        current = self.power / self.volts
        return current

    def total_resistance_in_parell(self):
        '''To Calculate Resistance of Parallel Resistor'''
        c = 0
        l = []
        for _ in range(len(self.resistance)):
            x = 1/self.resistance[c]
            l.append(x)
            c += 1
        x = fsum(l)
        y = 1/ x
        return y

    def branch_current(self):
        c = 0
        l = []
        for _ in range(len(self.resistance)):
            current = self.total_current_on_power_volts() * (self.total_resistance_in_parell() / self.resistance[c])
            l.append(current)
            c+=1
        return l

    def current_from_conductance_from_resistor(self):
        current = self.volts * (1 / self.total_resistance_in_parell())
        return current


    def current_in_branch_conductance(self):
        resist = 1/self.total_resistance_in_parell()
        l = []
        c = 0
        for _ in range(len(self.resistance)):
            current = self.current_from_conductance_from_resistor() * ((1/self.resistance[c])/resist)
            l.append(current)
            c+=1
        return l

c = CurrentDivider(100,1500,[10,25,100])
q = CurrentDivider(volts=30, resistance=[20,60])
w = CurrentDivider(volts=50, resistance=[2000,5000,10000])
print(c.branch_current())
print(c.current_in_branch_conductance())

print(q.current_in_branch_conductance())

print(w.current_in_branch_conductance())


class Resistor:
    def __init__(self, volts=None, current=None, resistance=None, power=None):
        self.volts = volts
        self.current = current
        self.resistance = resistance
        self.power = power

    def resistance_on_voltage_and_current(self):
        resistor = self.volts / self.current
        return f"Resistance of circuit with volts {self.volts}V and current {self.current}A is {resistor:.2f} \u03A9"

    def resistance_on_voltage_power(self):
        resistor = self.volts ** 2 / self.power
        return f"Resistance of circuit with volts {self.volts}V and power {self.power}W is {resistor:.2f} \u03A9"

    def resistance_on_power_current(self):
        resistance = self.power / self.current ** 2
        return f"Resistance of circuit with power {self.power}W and current {self.current}A is {resistance:.2f} \u03A9"


class Current(Resistor):

    def __init__(self, volts=None, current=None, resistance=None, power=None):
        super().__init__(volts=volts, current=current, resistance=resistance, power=power)

    def current_on_volts_resistance(self):
        current = self.volts / self.resistance
        return f"Current in circuit with volts {self.volts}V and resistance {self.resistance}\u03A9 is {current:.2f}A"

    def current_on_power_volts(self):
        current = self.power / self.volts
        return f"Current in circuit with power {self.power}W and volts {self.volts}V is {current}A"

    def current_on_power_resistance(self):
        current = sqrt(self.power / self.resistance)
        return f"Current in circuit with power {self.power}W and resistance {self.resistance}\u03A9 is {current:.2f}A"


class Volts(Resistor):

    def __init__(self, volts=None, current=None, resistance=None, power=None):
        super().__init__(volts=volts, current=current, resistance=resistance, power=power)

    def volts_on_current_resistance(self):
        volts = self.current * self.resistance
        return f"Volts in circuit with current {self.current}A and resistance {self.resistance}\u03A9 is {volts:.2f}V"

    def volts_on_power_current(self):
        volts = self.power / self.current
        return f"Volts in circuit with power {self.power}W and current {self.current}A is {volts:.2f}V"

    def volts_on_power_resistance(self):
        volts = sqrt(self.power * self.resistance)
        return f"Volts in circuit with power {self.power}W and resistance {self.resistance}\u03A9 is {volts:.2f}V"


class Watts(Resistor):

    def __init__(self, volts=None, current=None, resistance=None, power=None):
        super().__init__(volts=volts, current=current, resistance=resistance, power=power)

    def watts_on_volts_current(self):
        watts = self.volts * self.current
        return f"Power in watts in circuit with voltage {self.volts}V and current {self.current}A is {watts:.2f}W"

    def watts_on_volts_resistance(self):
        watts = (self.volts ** 2) / self.resistance
        return f"Power in watts in circuit with voltage {self.volts}V and resistance {self.resistance}\u03A9 is {watts:.2f}W"

    def watts_on_current_resistance(self):
        watts = (self.current ** 2) * self.resistance
        return f"Power in watts in circuit with current {self.current}A and resistance {self.resistance} is {watts:.2f}W"


w = Watts(volts=5, resistance=30, current=0.8)
# w.watts_on_volts_current()
# w.watts_on_volts_resistance()
# w.watts_on_current_resistance()
