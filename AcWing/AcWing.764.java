import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = "";
        
        for (int i = 0; i < a.length(); i ++){
            char tmp = (char) (a.charAt(i) + a.charAt((i + 1) % a.length()));
            b += tmp;
        }
        System.out.print(b);
    }
}
