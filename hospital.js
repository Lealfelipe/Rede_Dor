// Questão 4: Lógica de Programação
// Desenvolva um trecho de código (Em qualquer linguagem, mas preferencialmente JavaScript)
// para verificar se pacientes devem ser encaminhados para urgência ou emergência.
// Requisitos:
// 1. Defina uma coleção de objetos representando pacientes, com os seguintes atributos:
// “nome”, “idade” e “condição”
// 2. Escreva um método que identifique na coleção, segundo o critério a seguir, se o
// paciente deve ser encaminhado para urgência ou emergência:
// a. Pacientes com dores agudas no peito, fraturas expostas, acidentes de trânsito,
// ferimentos à bala ou com idade superior a 70 anos devem ser encaminhados
// para emergência.
// b. Pacientes com fraturas não expostas, cólicas renais, luxações e torções devem
// ser encaminhados para urgência.



class Paciente {
    constructor(nome, idade, condicao) {
        this.nome = nome;
        this.idade = idade;
        this.condicao = condicao;
    }

    avaliacao(){
        if (this.idade >= 70)
            return "Paciente encaminhado para EMERGENCIA"
        
        if (this.condicao == "dores agudas no peito" || this.condicao == "fraturas expostas" || this.condicao == "acidentes de trânsito" || this.condicao =="ferimentos à bala")
            return "Paciente encaminhado para EMERGENCIA"
        else if (this.condicao == "fraturas não expostas" || this.condicao == "cólicas renais" || this.condicao == "luxações" || this.condicao == "torções")
            
            return "Paciente encaminhado para Urgencia"


    }
}



const pacientes = [
    new Paciente("Felipe", 70, "fraturas não expostas"),
    new Paciente("José", 35, "dores agudas no peito"),
    new Paciente("Cris", 15, "torções")
]


pacientes.forEach(paciente => {
    console.log(`Paciente: ${paciente.nome}\n
    Idade: ${paciente.idade}\n
    Condição: ${paciente.condicao}\n
    Encaminhamento: ${paciente.avaliacao()}`
    )
    
});