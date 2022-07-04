package Ch1;

import java.util.Scanner;

// Q2. 3개의 값을 입력받아 그 수 중에서 최솟값을 구하시오.(출력)
public class Q2_Min3 {

    static int min3(int a, int b, int c) {

        int min = a; //최솟값

        if(b<min)
            min = b;
        if(c<min)
            min = c;

        return min; // 최솟값(min)을 반환
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a,b,c; // 3개의 변수 선언

        System.out.println("3개의 수를  입력하세요!");

        // 사용자한테 3개의 수(a,b,c)를 입력받음
        System.out.print("a : ");
        a = sc.nextInt();
        System.out.print("b : ");
        b = sc.nextInt();
        System.out.print("c : ");
        c = sc.nextInt();

        // min3 메서드에 입력받은 매개 변수 a,b,c를 넣고 나온 값(min)을 반환해서 변수 min에 넣음
        int min = min3(a,b,c);

        // 계산된 min값을 출력
        System.out.print("최솟값 : " + min);

    }

}
