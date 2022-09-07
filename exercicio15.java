import java.util.Scanner;

public class Exercicios {

    public static void main(String[] args) {
      /*15. Faça um algoritmo que receba um número e diga se este número está 
        no intervalo entre 100 e 200; */ 
       
      int numero;
      Scanner leitorScanner = new Scanner(System.in);
      
      numero = leitorScanner.nextInt();
      
      if(numero >= 100 && numero <= 200){
        System.out.println("O numero digitado esta dentro do intervalo");
      }else{
        System.out.println("O numero digitado não esta dentro do intervalo");
      }
    
}}
