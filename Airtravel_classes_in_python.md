# Learning Python

Classes in Python: airtavel (flight, aircraft...)

## Usage

### Two classes

>>> from airtravel import *
>>> a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
>>> a.registration()
'G-EUPT'
>>> a.model()
'Airbus A319'
>>> a.seating_plan()
(range(1, 23), 'ABCDEF')

## Collaborating classes

>>> from airtravel import *
>>> f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
>>> f.aircraft_model()
'Airbus A319'
