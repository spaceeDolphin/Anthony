#include <wiringPi.h>
#include <iostream>
#include <string>
#include <string.h>

//using namespace std;

//Morse code parameters
const int unit = 400; //800ms morse unit length

#pragma region Morse Code
const char _[] = " ";
const char A[] = "._-";
const char B[] = "-_._._.";
const char C[] = "-_._-_.";
const char D[] = "-_._.";
const char E[] = ".";
const char F[] = "._._-_.";
const char G[] = "-_-_.";
const char H[] = "._._._.";
const char I[] = "._.";
const char J[] = "._-_-_-";
const char K[] = "-_._-";
const char L[] = "._-_._.";
const char M[] = "-_-";
const char N[] = "-_.";
const char O[] = "-_-_-";
const char P[] = "._-_-_.";
const char Q[] = "-_-_._-";
const char R[] = "._-_.";
const char S[] = "._._.";
const char T[] = "-";
const char U[] = "._._-";
const char V[] = "._._._-";
const char W[] = "._-_-";
const char X[] = "-_._._-";
const char Y[] = "-_._-_-";
const char Z[] = "-_-_._.";
#pragma endregion

void WordToMorse(char* wordArray, char* morseArray) {
    for (int i = 0; wordArray[i] != '\0'; i++) {
        wordArray[i] = tolower(wordArray[i]);
        if (wordArray[i] == '_') { strcat(morseArray, _); }
        else if (wordArray[i] == 'a') { strcat(morseArray, A); }
        else if (wordArray[i] == 'b') { strcat(morseArray, B); }
        else if (wordArray[i] == 'c') { strcat(morseArray, C); }
        else if (wordArray[i] == 'd') { strcat(morseArray, D); }
        else if (wordArray[i] == 'e') { strcat(morseArray, E); }
        else if (wordArray[i] == 'f') { strcat(morseArray, F); }
        else if (wordArray[i] == 'g') { strcat(morseArray, G); }
        else if (wordArray[i] == 'h') { strcat(morseArray, H); }
        else if (wordArray[i] == 'i') { strcat(morseArray, I); }
        else if (wordArray[i] == 'j') { strcat(morseArray, J); }
        else if (wordArray[i] == 'k') { strcat(morseArray, K); }
        else if (wordArray[i] == 'l') { strcat(morseArray, L); }
        else if (wordArray[i] == 'm') { strcat(morseArray, M); }
        else if (wordArray[i] == 'n') { strcat(morseArray, N); }
        else if (wordArray[i] == 'o') { strcat(morseArray, O); }
        else if (wordArray[i] == 'p') { strcat(morseArray, P); }
        else if (wordArray[i] == 'q') { strcat(morseArray, Q); }
        else if (wordArray[i] == 'r') { strcat(morseArray, R); }
        else if (wordArray[i] == 's') { strcat(morseArray, S); }
        else if (wordArray[i] == 't') { strcat(morseArray, T); }
        else if (wordArray[i] == 'u') { strcat(morseArray, U); }
        else if (wordArray[i] == 'v') { strcat(morseArray, V); }
        else if (wordArray[i] == 'w') { strcat(morseArray, W); }
        else if (wordArray[i] == 'x') { strcat(morseArray, X); }
        else if (wordArray[i] == 'y') { strcat(morseArray, Y); }
        else if (wordArray[i] == 'z') { strcat(morseArray, Z); }
        strcat(morseArray, " ");
    }
}

class Morse {
    public:
    int ledPin;

    Morse(int ledPin) {
        this->ledPin = ledPin;
    }

    void DiodeLong() {
    digitalWrite(ledPin, HIGH);
    std::cout << "-" << std::endl;
    delay(3*unit);
    digitalWrite(ledPin, LOW);
}
    void DiodeShort() {
    digitalWrite(ledPin, HIGH);
    std::cout << "." << std::endl;
    delay(unit);
    digitalWrite(ledPin, LOW);
}
    void PauseLong() {
    std::cout << " " << std::endl;
    delay(3*unit);
}
    void PauseShort() {
    //std::cout << "_" << std::endl;
    delay(unit);
}
};

int main() {
    // Setup
    wiringPiSetupGpio();
    int ledPin = 17;
    pinMode(ledPin, OUTPUT);

    // Read word and convert to Morse Code
    std::string wordIn;
    std::cin >> wordIn;
    char wordArray[wordIn.length() + 1];
    strcpy(wordArray, wordIn.c_str());
    std::cout << "'" << wordArray << "' in morse: ";
    char morseArray[50];
    WordToMorse(wordArray, morseArray);
    std::cout << morseArray << std::endl;

    // Display Morse Code with diode
    Morse mDiode(ledPin);
    for (int i = 0; morseArray[i] != '\0'; i++) {
        if (morseArray[i] == '.') { mDiode.DiodeShort(); }
        else if (morseArray[i] == '-') { mDiode.DiodeLong(); }
        else if (morseArray[i] == '_') { mDiode.PauseShort(); }
        else if (morseArray[i] == ' ') { mDiode.PauseLong(); }
    }

    return 0;
}


