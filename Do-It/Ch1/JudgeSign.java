package Ch1;

import java.util.Scanner;

// 입력한 정수값이 양수인지 음수인지 0인지 판단하도록 작성하시오.
public class JudgeSign {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n; // 입력된 값을 담을 변수 n 선언

        System.out.print("정수를 입력하세요 : ");
        n = sc.nextInt(); //입력된 값을 n에 넣음

        // 정수값이 양수,음수,0인지 판단 하는 식
        if(n>0) // n이 양수일 때(0보다 클 때)
            System.out.println(n + "는 양수입니다.");
        else if(n<0) // n이 음수일 때(0보다 작을 때)
            System.out.println(n + "는 음수입니다.");
        else // 위의 두 상황이 아니면 0이라 따로 조건 필요 x (else만 써도 된다.) -> 위의 두 상황이 아니면 무조건 0이기 때문에
            System.out.println(n + "는 0입니다.");
    }
}
