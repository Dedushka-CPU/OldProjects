#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char box[10][10];
int cool = 0;

void clearConsole() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void randomApple() {
    int x, y;
    do {
        x = rand() % 10;
        y = rand() % 10;
    } while (box[x][y] != '_');
    box[x][y] = 'A';
}

void checkPosition(int x, int y) {
    if (box[x][y] == 'A') {
        cool++;
        randomApple();
    }
}

void PressButton(int *x, int *y) {
    int c;
    scanf("%d", &c);
    if (c == 6) {
        *y = (*y + 1) % 10;
    } else if (c == 8) {
        *x = (*x - 1 + 10) % 10;
    } else if (c == 2) {
        *x = (*x + 1) % 10;
    } else if (c == 4) {
        *y = (*y - 1 + 10) % 10;
    }
    checkPosition(*x, *y);
}

void printfBox() {
    printf("Cool: %d\n", cool);
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%c ", box[i][j]);
        }
        printf("\n");
    }
}

int main() {
    srand(time(NULL)); 

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            box[i][j] = '_';
        }
    }

    randomApple();
    int pos_x = 5;
    int pos_y = 5;
    box[pos_x][pos_y] = 'Z';
    printfBox();

    while (1) {
        printf("Your turn.\n");
        box[pos_x][pos_y] = '_';
        PressButton(&pos_x, &pos_y);
        box[pos_x][pos_y] = 'Z';
        clearConsole();
        printf("Box after move.\n");
        printfBox();
        if(cool==10){
            clearConsole();
            printf("Yor're win!!\n");
            break;
        }
    }

    return 0;
}
