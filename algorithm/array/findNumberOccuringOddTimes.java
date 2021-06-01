import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class findNumberOccuringOddTimes {

    public static int Solution1(List<Integer> in) {
        System.out.println("input list is " + in.toArray());
        HashSet<Integer> hs = new HashSet<>();
        for (Integer num : in) {
            if (hs.contains(num)) {
                hs.remove(num);
            } else {
                hs.add(num);
            }
        }
        if (hs.size() != 1) {
            throw new RuntimeException("Incorrect input integer list");
        }
        return hs.iterator().next();
    }

    public static void main(String[] args) {
        List<Integer> t1 = new ArrayList<>();
        t1.add(1);
        t1.add(3);
        t1.add(3);
        int a = findNumberOccuringOddTimes.Solution1(t1);
        System.out.println(a);
    }
}