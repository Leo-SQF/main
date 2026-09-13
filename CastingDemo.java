public class CastingDemo {
    public static void main(String[] args) {
        double num1 = 7.89;
        int cut = (int) num1;
        System.out.println(cut);

        int m = 7;
        int n = 2;
        System.out.println(m / n);
        System.out.println( (double)m / n );
        System.out.println( (double)(m/n) );
    }
}