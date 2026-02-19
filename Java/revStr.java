public class revStr {
    public static void main(String[] args) {
        String str = "Hello World";
        
        StringBuilder sb = new StringBuilder(str);
        String reversed = sb.reverse().toString();
        
        System.out.println("Original: " + str);
        System.out.println("Reversed: " + reversed);
    }
}