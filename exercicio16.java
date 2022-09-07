
import java.util.Scanner;

public class App {

    public static void main(String[] args) {
    /*16. Escreva um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a
    sua média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e
    Recuperação (media entre 5.1 a 6.9); */ 
      
      float nota1;
      float nota2;
      float nota3;
      float media;
      String nome;
      
      Scanner leitorScanner = new Scanner(System.in);
      System.out.println("digite seu nome");
      nome = leitorScanner.nextLine();
      System.out.println("digite nota 1");
      nota1 = leitorScanner.nextFloat();
      System.out.println("digite nota 2");
      nota2 =  leitorScanner.nextFloat();
      System.out.println("digite nota 3");
      nota3 = leitorScanner.nextFloat();
      
      media = ((nota1+nota2+nota3)/3) ;
              
      if(media >= 7){
        System.out.println(nome + ", " + "você foi aprovado(a)!");
      }else{
          if (media >= 6 || 5 >= media){
          System.out.println(nome + ", " + "você está encrencado(a): em Recuperação");
          }else{
          System.out.println(nome + ", " + "lascou, você foi reprovado(a)!");             
            }
        }
      }

}
   
