function calcular_area(raio) {
    let pi = 3.14159;
    return pi * Math.pow(raio, 2);
}
let idade = 18;
if (idade >= 18) {
    console.log("Pode votar");
} else {
    console.log("Não pode votar");
}
for (let i = 0; i < 5; i++) {
    console.log(`Contagem: ${i}`);
}
let numeros = [1, 2, 3, 4, 5];
let soma = 0;
for (let num of numeros) {
    soma += num;
}
console.log(`Soma total: ${soma}`);
class Carro {
    constructor(marca, modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }
    acelerar() {
        return `${this.marca} ${this.modelo} está acelerando!`;
    }
}
let meu_carro = new Carro("Toyota", "Corolla");
console.log(meu_carro.acelerar());