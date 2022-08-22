let a = 2
let b = 4
let c = -6

function quadratic(a,b,c){
    // Value underneath the square root
    let x = (b*b) - (4*a*c)
    console.log(Math.sqrt(x))

    if(x<0){
        console.log("Imaginary")
    }
    else{
        let root1 = (-b + Math.sqrt(x)) / (2*a)
        let root2 = (-b - Math.sqrt(x)) / (2*a)

        console.log("First root is: " + root1)
        console.log("Second root is: " + root2)
    }
}

// function call
quadratic(a,b,c)