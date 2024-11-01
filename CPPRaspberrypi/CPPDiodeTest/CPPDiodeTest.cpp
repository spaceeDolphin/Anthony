#include <wiringPi.h>
#include <iostream>

int main() {
	//setup
	wiringPiSetupGpio();

	int ledPin = 17;

	pinMode(ledPin, OUTPUT);

	while(true) {
		//LED ON
		digitalWrite(ledPin, HIGH);
		std::cout << "LED ON" << std::endl;
		delay(1000);

		//LED OFF
		digitalWrite(ledPin, LOW);
		std::cout << "LED OFF" << std::endl;
		delay(1000);
	}
	return 0;
}

