package Ch1;

import java.util.Scanner;

// Q1. 사용자한테 입력받은 4개의 수 중에서 최대값을 구하시오.
public class Q1_Max4 {

    static int max4(int a, int b, int c, int d) {

        int max = a; // 최댓값

        if(b>max)
            max = b;
        if(c>max)
            max = c;
        if(d>max)
            max = d;

        return max; //최댓값(max)를 반환
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a,b,c,d;

        System.out.println("4개의 수를 입력하세요!!");
        System.out.print("a : ");
        a = sc.nextInt();

        System.out.print("b : ");
        b = sc.nextInt();

        System.out.print("c : ");
        c = sc.nextInt();

        System.out.print("d : ");
        d = sc.nextInt();

        int max = max4(a,b,c,d); //a,b,c,d의 최댓값

        System.out.print("최댓값 : " + max);
    }
}
