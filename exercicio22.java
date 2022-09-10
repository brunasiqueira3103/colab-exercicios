package exercicio22;
import java.util.Scanner;


public class App {
 
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        
        String nomeProduto;
        float precoCusto = 0.0f;
        float precoVenda = 0.0f;
        float totalCusto = 0.0f;
        float totalVenda =0.0f;
        int i = 0;
        
        for(; i < 3; i++){
            
            System.out.println("Informe o nome do produto: ");
            nomeProduto = leitor.next();
            
            System.out.println("Informe o preço de custo do produto: ");
            precoCusto = leitor.nextFloat();
            
            System.out.println("Informe o preço de venda do produto: ");
            precoVenda = leitor.nextFloat();
     
            totalCusto = totalCusto + precoCusto;
            totalVenda = totalVenda + precoVenda;
            
            if (precoCusto == precoVenda) {
                 System.out.println("Houve Empate, sem lucro, sem perda!");
                }else{
                      if (precoCusto > precoVenda){
                          System.out.println("Houve Prejuízo!");
                        }else{
                           System.out.println("Houve Lucro!");
                        }
            System.out.println(nomeProduto + " preço de custo: " + precoCusto
                    + ", preço de venda " + precoVenda);
            }
        }
        
        System.out.println("/n" +" A média de custo é de: " + (totalCusto/i)); 
        System.out.println("A média de venda é de: " + (totalVenda/i));  

    }
}
