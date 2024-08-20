#include <stdio.h>

int main() {
    int num1, num2, prodotto;

    printf("Inserisci il primo numero: ");
    scanf("%d", &num1);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &num2);


    prodotto = num1 * num2;

    
    printf("Il prodotto tra %d e %d è: %d\n", num1, num2, prodotto);

    return 0;
}
