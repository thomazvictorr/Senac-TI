namespace CalculaDobro;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Informe um número: ");
        int numero = int.Parse(Console.ReadLine());
        int dobro = numero * 2;
        Console.WriteLine("Dobro = " + dobro);
    }
}
