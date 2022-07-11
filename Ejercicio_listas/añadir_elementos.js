
// function solution(arrayA, arrayB){

//     var new_array = []

//     for(let i = 0; i < arrayA.length; i++){
//         new_array.push(arrayA[i])
//         new_array.push(arrayB[i])
//         new_array.ins
//     }

//     return new_array
// }

// console.log(solution([1,2,3],[4,5,6]))


// function solution2(arrayA_2, arrayB_2){

//     var cadena = ""
//     var new_array = []
//     cadena = arrayA_2 + arrayB_2
//     //console.log(cadena)
//     for(let j = 0; j < cadena.length; j++ ){
//         if (cadena[j] == ","){
//             continue
//         }
//         else{
//             new_array.push(cadena[j])
//         }
//     }
//     console.log(new_array);
// }

// solution2([1, 2, 3], [4, 5, 6]);
// solution2(["A","B","C"], ["D","E","F"]);


// function solution(arrayA, arrayB){
//     var cadena = ""

//     cadena = [arrayA + arrayB]
//     let arr = cadena.split()
//     console.log(arr)

//     return cadena

// }

// console.log(solution([1,2,3],[4,5,6]));
// console.log(solution(["A","B","C"],["D","E","F"]));


// function solution (arrayA, arrayB){

//     var new_array = []

//     for (let i = 0; i < arrayA.length; i++){
//         new_array.push(arrayA[i])
//     };

//     for (let i = 0; i < arrayA.length; i++){
//         new_array.push(arrayB[i])
//     };

//     return new_array
// }


// console.log(solution([1,2,3], [4,5,6]));
// console.log(solution(["A","B","C"], ["D","E","F"]));


// var cadena1 = "Hola-Mundo-soy-diego-soy-programador"
// var lista1 = [1,2,3], lista2 = [4,5,6]

// const cadena_lista = String(lista1) + "," + String(lista2)
// console.log(cadena_lista)


// let ele = cadena1.split("-")
// //console.log(ele);



// function solution (arrayA, arrayB){

//     const ca_conver = String(arrayA) +","+  String(arrayB)
//     const new_array =  ca_conver.split(",")

//     return new_array
   
// }

// console.log("Solucion:", solution([1,2,3],[4,5,6]))

// console.log("Solucion:", solution(["A","B","C"], ["D","E","F"]));


//##Array de arrays en un solo array

function array_arrays(array){
    const new_array = []

    for (e in array) {
      for (i in array[e]) {
        new_array.push(array[e][i]);
      }
    }
    
    return new_array
}


const lista= [[1,2],[3,4],[5,6]], lista1 = [1,2,3,4,5,6], lista2 = []

console.log(array_arrays(lista))

for (e in lista){
    //console.log(lista[e])
    for(i in lista[e]){
        //console.log(lista[e][i])
            lista2.push(lista[e][i])
    }    
}
//console.log(lista2)


//Solucion primer ejercicio
function solution1(arrayA, arrayB){
 	return [...arrayA, ...arrayB];
};

console.log(solution1([1,2,3],[4,5,6]))

console.log(solution1(["A", "B", "C"], ["D", "E", "F"]));


//Solución segundo ejercicio 
function solution2(array){
 	return array.flat();
}; 

console.log(solution2(lista));