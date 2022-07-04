package Ch1;

import java.util.Scanner;

// 1부터 n까지의 합을 구하시오.
// - 조건 : for문만 사용 가능
public class SumFor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n;
        System.out.println("1부터 n까지의 합을 구할 것이다.");

        System.out.print("n의 값 : ");
        n = sc.nextInt();

        // 1부터 n까지의 합을 구하는 식
        int sum = 0; // 총 합을 변수 sum에 담는다.

        //i가 1부터 n이 될때까지 i를 증가시킨다.(반복)
        //for문 구조
        // for(초기화 부분; 제어식; 엡데이트 부분)명령문
        for(int i=1; i<=n; i++)
            sum += i;

            System.out.println("1부터" + n + "까지의 합은 " + sum + "입니다.");


    }
}
