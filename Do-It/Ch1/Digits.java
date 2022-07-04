package Ch1;

import java.util.Scanner;

// 2자리의 양수(10~99)만 입력이 가능한 프로그램을 작성하시오.
// - do-while문 사용
/*
do while문의 do문은
일단 루프 본문을 한 번 실행한 다음에 계속 반복할 것인지를 판단하는 사후 판단 반복문이다.

Tip
사전 판단 반복문인 while문,for문은 처음에 제어식을 평가한 결과가 0이면 루프 본문을 1번도 실행하지 않는다.
do-while문은 루프 본문이 반드시 1번은 실행된다.(do문이 최소 1회 실행된다는 뜻)
 */
public class Digits {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;

        System.out.println("2자리 정수(양수)를 입력하세요 : ");

        // while문 조건이 걸릴 때까지 do문 무한 반복
        do {
            System.out.print("값 입력 : ");
            n = sc.nextInt();
        } while(n<10 || n>99);
        System.out.println(n + "은 2자리 정수(양수)입니다!");
    }
}
