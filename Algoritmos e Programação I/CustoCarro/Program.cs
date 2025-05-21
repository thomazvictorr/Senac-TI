namespace CustoCarro;

class Program
{
    static void Main(string[] args)
    {
        // entrada de dados
        Console.Write("Informe o custo de fábrica: ");
        double custoFabrica = double.Parse(Console.ReadLine());
        //procesamento dos dados
        double custoDistribuidor = custoFabrica * 0.28;
        double imposto = custoFabrica * 0.45;
        double custoConsumidor = custoFabrica + custoDistribuidor + imposto;
        // saida de dados
        Console.WriteLine("Custo ao consumidor: {0:N2}", custoConsumidor);
    }
}
