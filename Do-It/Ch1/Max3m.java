package Ch1;
// 3개의 정수값 가운데 최댓값을 구하여 출력합니다.

public class Max3m {
    //a,b,c의 최댓값을 구하여 반환

    // max3 메서드는 int형 매개 변수 a,b,c의 값을 받아 최댓값을 구하고
    // 그것을 int형 값(max)로 반환한다.
    static int max3(int a, int b, int c) {
        int max = a;
        if(b>max)
            max = b;
        if(c>max)
            max = c;

        return max; // 구한 최댓값(max)를 호출한 곳으로 반환한다.
        // @추가 설명
        /*
        메서드는 return문에서 처리한 결과값을 원래 호출한 곳으로 반환한다.
        max3 메서드의 반환값은 int형이고, 메서드 끝부분에서 변수 max값을 반환한다.
        예를 들어 max(3,2,1)을 호출하면 아래 28번줄을 보면 알 수 있듯이 메서드호출식 max(3,2,1)을 평가한 값은 int형 3이 된다.
        다만 반환값(return값)의 자료형이 void인 메서드는 값을 반환하지 않는다.
         */
    } // end max3메서드

    //main 함수
    // 모든 출력 결과가 3이 나온다.
    public static void main(String[] args) {
        System.out.println("max3(3,2,1) = " + max3(3,2,1));
        System.out.println("max3(3,2,2) = " + max3(3,2,2));
        System.out.println("max3(3,1,2) = " + max3(3,1,2));
        System.out.println("max3(3,2,3) = " + max3(3,2,3));
        System.out.println("max3(2,1,3) = " + max3(2,1,3));
        System.out.println("max3(1,2,3) = " + max3(1,2,3));
        System.out.println("max3(3,2,1) = " + max3(2,1,3));
    }
}
