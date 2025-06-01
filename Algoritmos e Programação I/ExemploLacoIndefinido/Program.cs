namespace ExemploLacoIndefinido;

class Program
{
    static void Main(string[] args)
    {
        int soma = 0;
        Console.Write("Informe um número: ");
        int n = int.Parse(Console.ReadLine());
        while (n >= 0)
        {
            soma = soma + n;
            Console.Write("Informe um número: ");
            n = int.Parse(Console.ReadLine());
        }
        Console.WriteLine("Soma:" + soma);
    }
}
