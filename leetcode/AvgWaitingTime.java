
class AvgWaitingTime{
  public static void main(String[] args) {
    double curr = 0;
    double wait = 0;
    int[][] customers={{1,2},{2,5},{4,3}};
    for (int[] c : customers) {
      // System.out.println(c);
      // System.out.println(c[1]);
      // System.out.println(customers);
      curr = Math.max(curr, 1.0 * c[0]) + c[1];
      wait =wait+ curr - c[0];
      }
        System.out.println(1.0 * wait / customers.length);
    }
}