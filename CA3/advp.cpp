int main() {
    int a = 0;
    int b = 2;

    if (a > -1) {
        a = 3;
    } else {
        a = 4;
    }

    a = b + 5;

    for (int i = 0; i < 4; i++) {
        b = b + i;
        if (b < 5) {
            a = a * 2;
        } else {
            a = a / 2;
        }
    }

    // Additional control flow path based on the value of a
    if (a % 2 == 0) {
        b = b - 5;
    } else {
        b = b + 5;
    }

    // Additional control flow path based on the value of b
    switch (b) {
        case 0:
            a = a + 10;
            break;
        case 1:
            a = a - 10;
            break;
        default:
            a = a * 2;
            break;
    }

    // Additional control flow path based on the value of a
    if (a < 0) {
        b = b * -1;
    } else if (a == 0) {
        b = 0;
    } else {
        b = b + 1;
    }

    return 0;
}