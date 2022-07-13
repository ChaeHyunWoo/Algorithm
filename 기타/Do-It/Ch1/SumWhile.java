package Ch1;

import java.util.Scanner;

// - 01-2 반복
// 1부터 n까지의 정수의 합 구하기(while문 사용)
// - Tip - 하나의 변수를 사용하는 반복문은 while문보다 for문을 사용하는 것이 더 좋다.
public class SumWhile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("1부터 n까지의 합을 구할 것이다.");
        System.out.print("n의 값을 입력 : ");
        int n = sc.nextInt();

        // 1부터 n까지의 합 구하는 식
        int sum = 0; //변수 sum은 1부터 n까지의 합을 넣을 것이다.
        int i =1;

        // while:반복문
        while(i<=n) { // i가 1부터 n까지 반복
            sum += i; // sum에 i를 더한다.  -> += 게 쓴 경우 왼쪽으로 값을 더한다.
            i++; // i값을 1씩 증가시킨다.
            // while문은 반복문이기에 i가 n이 될때까지 계속 반복한다. 반복을 하면서 sum에 값이 계속 누적된다.
        }
        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }
}
