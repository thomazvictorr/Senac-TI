namespace Tabuada;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Informe um número: ");
        int n = int.Parse(Console.ReadLine());
        int r;
        for (int cont = 1; cont <= 10; cont++)
        {
            r = n * cont;
            Console.WriteLine("{0} x {1} = {2}", n, cont, r);
        }
    }
}