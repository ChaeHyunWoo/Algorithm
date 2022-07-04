package Ch1;

import java.util.Scanner;

// Q3. 4개의 값 중에 최솟값을 구하시오(출력).
public class Q3_Min4 {

    static int min4(int a, int b, int c, int d) {

        int min = a;

        if(b<min)
            min = b;
        if(c<min)
            min = c;
        if(d<min)
            min = d;

        return min; //최솟값(min) 반환

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a,b,c,d;

        System.out.print("4개의 수를 입력하세요!");
        System.out.print("a : ");
        a = sc.nextInt();

        System.out.print("b : ");
        b = sc.nextInt();

        System.out.print("c : ");
        c = sc.nextInt();

        System.out.print("d : ");
        d = sc.nextInt();

        int min = min4(a,b,c,d);

        System.out.print("최솟값 : " + min);
    }
}
