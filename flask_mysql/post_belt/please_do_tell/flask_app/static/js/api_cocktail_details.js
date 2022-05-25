async function getCocktail(drink_id){
    let data = await fetch(`https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${drink_id}`);
    let drink = await data.json();
    let drink_data = drink.drinks[0];
    return drink_data;
}

function cocktailCard(cocktail_data){
    let pix_div = document.querySelector('.cocktail-img');
    pix_div.src = `${cocktail_data.strDrinkThumb}/preview`;
    pix_div.alt = cocktail_data.strDrink;

    let fav_div = document.querySelector('.favorited');
    fav_div.href = `/favorites/add/${cocktail_data.idDrink}/${cocktail_data.strDrink}`

    let name_div = document.querySelector('.cocktail-name');
    name_div.innerText = cocktail_data.strDrink;

    let instructions_div = document.querySelector('.instructions');
    instructions_div.innerText = cocktail_data.strInstructions;

    let glass_div = document.querySelector('.glass-ware');
    glass_div.innerText = cocktail_data.strGlass

    let ing_div = document.querySelector('.ing-list');
    for(let i = 1; i < 16; i++){
        if(cocktail_data[`strIngredient${i}`]){
            let list_ing = document.createElement('li');
            list_ing.innerText = cocktail_data[`strMeasure${i}`];
            list_ing.innerText += '- ';
            list_ing.innerText += cocktail_data[`strIngredient${i}`]; 
            ing_div.append(list_ing);
        }else{
            break;
        }
    }
}

//get the cocktail id from url
let urlString = window.location.href;
let urlArr = urlString.split('/');
let cocktail_number = parseInt(urlArr[(urlArr.length-1)]);//get the last item since id is at end

const cocktailContent = getCocktail(cocktail_number).then(res=> cocktailCard(res));