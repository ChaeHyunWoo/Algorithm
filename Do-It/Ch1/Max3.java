package Ch1;

import java.util.Scanner;
// 01-1 알고리즘이란
// 3개의 정수값을 입력하고 최대값을 구하기
/*
 - 문제 풀이 -
 1. max값에 a를 넣는다.
 2. b가 max보다 크면 max에 b를 넣는다.
 3. c가 max보다 크면 max에 c를 넣는다.
 */
public class Max3 {
    public static void main(String[] args) {

        // Scanner를 사용하여 사용자한테 입력값을 받는다.
        // (System.in) : 키보드와 연결된 표준 입력 스트림(Standard Input Stream)
        Scanner sc = new Scanner(System.in);
        System.out.println("3개의 정수의 최대값을 구합니다.");

        // 사용자한테 변수 a,b,c를 입력받는다.
        System.out.println("a : ");
        int a = sc.nextInt(); // 키보드로 입력된 정수값을 얻기 위해 nextInt() 사용
        System.out.println("b : ");
        int b = sc.nextInt();
        System.out.println("c : ");
        int c = sc.nextInt();

        int max = a;

        if(b>max)
            max = b;

        if(c>max)
            max = c;

        System.out.println("최대값은 " + max + "입니다!!!");

    }
}