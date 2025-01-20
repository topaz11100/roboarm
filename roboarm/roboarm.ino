#include "Servo_Vector.h"
#include "IO_helper.h"

const int motor_count = 5;

Servo_vector arm{motor_count};
const int arm_pin[motor_count] = {4,5,6,7,8};
const int speed = 1500;
int angle[motor_count] = {90,90,90,90,90};

Protocol p{',', motor_count};

void setup()
{
  Serial.begin(9600);
  arm.attach(arm_pin);
  arm.move_arr(angle, speed);
}

void loop()
{
  String input = receive_String('a');
  if (input.equals("")) return;
  p.strip(input);
  p.fillintarr(angle);
  arm.move_arr(angle, speed);
}

/*

0 : 좌, 앞, 밑, 밑, 집기
1 : 우, 뒤, 위, 위, 놓기

const int limit[5][2] = { {180, 0}, {0, 180}, {135, 0}, {180, 0}, {, } };

*/


