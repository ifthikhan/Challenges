/*
 * Q:
 *    Given a 1000X1000 grayscale image where each pixel is 8 bits, you need to
 *    reverse the order of the bits in each pixel. Example: 10001101 becomes
 *    10110001, 00111101 becomes 10111100 and so on. Provide the most efficient
 *    solution in the manner of performance because another input is that you need to
 *    handle many images per second.
 */

#include <stdio.h>
#include <stdlib.h>

#define ROWS 10
#define COLS 10

unsigned char reverse(unsigned char);
unsigned char reverse_linear(unsigned char);
void fill_matrix(unsigned char[][COLS], int, int);
void print_matrix(unsigned char[][COLS], int, int);
void mirror_matrix(unsigned char[][COLS], int, int);
unsigned char gen_rand(int);

int main() {

    unsigned char matrix[ROWS][COLS];

    fill_matrix(matrix, ROWS, COLS);

    printf("Initial Matrix \n");
    print_matrix(matrix, ROWS, COLS);

    printf("Mirrored Matrix \n");
    mirror_matrix(matrix, ROWS, COLS);
    print_matrix(matrix, ROWS, COLS);

    return EXIT_SUCCESS;
}

/*
 * Generates a matrix with the specified number of rows and columns.
 * The values generated are numerical and are not more than 256
 */
void fill_matrix(unsigned char matrix[][COLS], int rows, int cols) {

    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            matrix[i][j] = (unsigned char) gen_rand(256);
        }
    }
}

void mirror_matrix(unsigned char matrix[][COLS], int rows, int cols) {

    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            matrix[i][j] = reverse(matrix[i][j]);
        }
    }
}

void print_matrix(unsigned char matrix[][COLS], int rows, int cols) {

    int i, j;
    for (i = 0; i < rows; i++) {

        printf(" | ");
        for (j = 0; j < cols; j++) {
            printf("%3u | ", matrix[i][j]);
        }
        printf("\n");
    }
}

/**
 * Returns random number in range of 0 to max_val
 */
unsigned char gen_rand(int max_val) {

    return (unsigned char) rand();
}

/*
 * A method to reverse bits in a single byte.
 */
unsigned char reverse(unsigned char input) {

    unsigned char output = (input >> 4) | (input << 4);
    output = ((output & 0xCC) >> 2) | ((output & 0x33) << 2);
    output = ((output & 0xAA) >> 1) | ((output & 0x55) << 1);

    return output;
}

/*
 * Mirrors the bit patterns of the input and return the mirrored
 * data.
 */
unsigned char reverse_linear(unsigned char input) {

    short i = 0;
    unsigned char output = 0;

    for (i = 0; i < 8; i++) {
        output = (output << 1) | (input & 0x1);
        input = input >> 1;
    }

    return output;
}

