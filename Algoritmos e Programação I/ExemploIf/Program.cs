namespace ExemploIf;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Velocidade: ");
        int velocidade = int.Parse(Console.ReadLine());
        if (velocidade > 60)
        {
            Console.WriteLine("Você excedeu o limite de velocidade");
            Console.WriteLine("Multado");
        }
        Console.WriteLine("Fim do Programa!");
    }

}
