package com.programmers.java;

class 하샤드수_Level1 {
    public boolean solution(int x) {

        // sum은 자릿수의 합
        int sum = 0;
        int y = x;

        while (y>0) {
            sum += y%10;
            y /= 10;
        }
        return x%sum == 0;
    }
}
