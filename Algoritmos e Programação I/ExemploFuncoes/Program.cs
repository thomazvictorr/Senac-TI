namespace ExemploFuncoes;

class Program
{
    static void Main(string[] args)
    {
        mensagem();
        Console.WriteLine("Digite o número: ");
        int numero = int.Parse(Console.ReadLine());
        int fat = calculaFatorial(numero);
        Console.WriteLine("Fatorial = " + fat);
    }

    static void mensagem()
    {
        Console.WriteLine("**** Calcula o Fatorial de um Número ****");
    }

    static int calculaFatorial(int n)
    {
        int fatorial = 1;
        for (int cont = 1; cont <= n; cont++)
        {
            fatorial = fatorial * cont;
        }
        return fatorial;
    }
}