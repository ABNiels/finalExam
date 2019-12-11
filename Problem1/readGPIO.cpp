
#include<iostream>
#include<fstream>
#include<string.h>
#include<sstream>
#include<unistd.h>
#include<stdlib.h>
#include"GPIO.h"

using namespace std;
using namespace exploringBB;

int main(int argc, char* argv[]){
   GPIO extLed(60);
   
   extLed.setDirection(INPUT);
   if (extLed.getValue() == HIGH) cout << "ON" << endl;
   else cout << "OFF" << endl;

   return 0;
}
