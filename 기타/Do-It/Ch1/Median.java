package Ch1;

import java.util.Scanner;

// 3개의 정수값을 입력하고 중앙값(중간값)을 구한 다음 출력하시오.

// 3개의 값의 중앙값을 구하는 과정은 퀵 정렬(Quick Sort)에서도 사용 가능
public class Median {

    // med3메서드 대신 med4처럼 작성해도 결과는 같다.
    // 하지만 처음의 if문이 성립한 경우 2번 째 if문에서도 같은 판단을 수행하므로 효율이 나빠진다.
    static int med4(int a, int b, int c) {
        if((b>=a && c<=a) || (b<=a && c>=a))
            return a;
        else if((a>b && c<b) || (a<b && c>b))
            return b;
        return c;
    }

    //3개의 정수 중 중간값(중앙값)을 구하는 메서드
    static int med3(int a,int b,int c) {
        if (a >= b)
            if (b >= c)
                return b;
            else if (a <= c)
                return a;
            else
                return c;
        else if (a > c)
            return a;
        else if (b > c)
            return c;
        else
            return b;

    }

    //main
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a,b,c;

        System.out.println("3개의 정수의 중앙값을 구할거야");

        System.out.print("a : ");
        a = sc.nextInt();
        System.out.print("b : ");
        b = sc.nextInt();
        System.out.print("c : ");
        c = sc.nextInt();

        System.out.println("중앙값(중간값)은 " + med3(a,b,c) + "입니다!");

    }
}
