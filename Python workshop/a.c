#include <stdio.h>
#include <windows.h>  // Sleep function ke liye
 #include <stdlib.h> // For system("cls");

int main() {
    int width = 10; // Width of the screen
    int pos = 0;    // Ball ki current position
    int dir = 1;    // Ball ki movement ka direction (1 ya -1)

    while (1) { // Infinite loop
        printf("\r");  // Cursor ko line ke shuruat par le aana

        // Screen par ball ka display
        for (int i = 0; i < width; i++) {
            if (i == pos)
                printf("O");  // Ball ka symbol
            else
            {
                system("cls");//// Loding ke time bar bar screen ko clear kar de isliye
                printf("\t\t\t.......Loding............");  // prosess ke time kuch to msg aana chiye naa
            }
        }

        fflush(stdout);  // Output ko turant display karna
        Sleep(1.100);      // Ball ki speed (1.100 milliseconds)

        // Agar ball boundary par hit karti hai toh direction change karo
        if (pos == 0 || pos == width - 1)
            dir = -dir;  // Direction ko reverse karna

        pos = pos + dir; // Ball ki position update karo
    }
}
