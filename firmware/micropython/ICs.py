from machine import Pin,ADC

class L298:

    def __init__(self,motor_pins=[],en_pins=[],sense_pins=[]):
        self.motor_pins=[]
        self.en_pins=[]
        self.sense_pins=[]
        self.steps=[]
        self.current_pos=0
        for pin in motor_pins:
            self.pins.append(Pin(pin,Pin.OUT,value=0)) 
        for pin in en_pins:
            self.en_pins.append(Pin(pin,Pin.OUT,value=0))
        for pin in sense_pins:
            self.en_pins.append(ADC(pin))
        #step table
        self.init_step_table()
    
    def init_step_table(self): 
        self.step.append(lambda:(self.motor_pins[0](1),self.motor_pins[2](1)))
        self.step.append(lambda:(self.motor_pins[2](0),self.motor_pins[3](0)))
        self.step.append(lambda:(self.motor_pins[0](1),self.motor_pins[3](1)))
        self.step.append(lambda:(self.motor_pins[0](0),self.motor_pins[1](0)))
        self.step.append(lambda:(self.motor_pins[1](1),self.motor_pins[3](1)))
        self.step.append(lambda:(self.motor_pins[2](0),self.motor_pins[3](0)))
        self.step.append(lambda:(self.motor_pins[1](1),self.motor_pins[2](1)))
        self.step.append(lambda:(self.motor_pins[0](0),self.motor_pins[1](0)))

    def step(self,dir):
        self.steps[self.current_pos]()
        if dir:self.current_pos=self.current_pos+1 if self.current_pos<7 else 0
        else:self.current_pos=self.current_pos-1 if self.current_pos>0 else 7
