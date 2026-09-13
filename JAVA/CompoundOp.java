public class CompoundOp {
    public static void main(String[] args) {
        int num = 10;
        num += 4;  // num =10+4 →14
        System.out.println(num);

        num -= 3;  // num=14-3 →11
        System.out.println(num);

        num *= 2;  // num=11*2 →22
        System.out.println(num);

        num /= 4;  // 22/4 整数除法 →5
        System.out.println(num);

        num %= 3;  //5%3 →2
        System.out.println(num);
    }
}
