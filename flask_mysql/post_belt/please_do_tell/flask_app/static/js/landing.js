//get all the cocktails from API to put them on carousel slides on landing page
//all the cocktails on carousel are 50 selected from API that are the 50 on the IBA official cocktail list (if the DB has it, apparently no trinidad sour)
    //this is workaround since I do not want to pay for API curated list

// const IBA_LIST = [17209, 11113, 11202, 17196, 17212, 11410, 17202, 17247, 11007, 11000, 11844, 17190, 17192, 13377, 17828, 11014, 178317, 17251, 17185, 11288, 17199, 14366, 17256, 17189, 17829, 178367, 12754, 17215, 17216, 11004, 15941, 17195, 17210, 11227, 11006, 17197, 17200, 13971, 17204, 17188, 11009, 11001, 17207, 17214, 12196, 17193, 12420, 17194, 11034, 17184, 17186, 17211, 17198, 11580, 11690, 17205, 17253, 13214, 12101, 12214, 17219, 17180, 11102, 17250, 11005, 17213, 17201, 17203, 11008, 17206, 11003, 17191, 12127, 13621, 17218, 17241]

const IBA_LIST = [17209, 11113, 11202, 17196, 17212, 11410, 17202];//shorter temp
async function getCocktails(cocktailIdArr){
    let cocktail_data = {};//object with drink objects stored as keys by drink id from cocktail list array
    for(let cocktail_id of cocktailIdArr){
        data = await fetch(`https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${cocktail_id}`);
        let drink = await data.json();
        cocktail_data[`${cocktail_id}`] = drink.drinks[0];
    }
    console.log(IBA_LIST.length)
    return cocktail_data
}

const ibaCocktailSlides = getCocktails(IBA_LIST).then(res=> cocktailSlides(res));

function cocktailSlides(cocktailObj){
    let slideShowDiv = document.querySelector('.slideshow-container');
    console.log(cocktailObj)
    for(let [drink_id,drink] of Object.entries(cocktailObj)){
        let div = document.createElement('div');
        div.className = "mySlides";
        div.innerHTML = `<img src="${drink.strDrinkThumb}/preview">
        <a href = "cocktails/${drink_id}">${drink.strDrink}</div>`;

        slideShowDiv.append(div);
    }
}
