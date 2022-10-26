
# Generate container data
# a1-a50 b1-b50
from led_control.dataclasses import Container

cont_data = {}
led_id = 0
for letter in ['a', 'b']:
    for _id in range(0, 50):
        cont_data[f"{letter}{_id+1}"] = Container(led_id=led_id)
        led_id += 1
print(cont_data)
