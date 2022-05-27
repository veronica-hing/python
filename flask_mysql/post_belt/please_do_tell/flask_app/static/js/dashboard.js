function onSearchFriend(){
    //changes url to /friends/search/user_name to initiate search in python for db
    let searchDiv = document.querySelector('.search_cocktail')
    user_name = searchDiv.value;
    return location.href = `/friends/search/${user_name}`
}

async function onSearchDrink(){
    //change input string so spaces are underscores
    let searchDiv = document.querySelector('.search_cocktail')
    let cocktail_name = searchDiv.value;
    let format_cocktail = cocktail_name.replace(' ','_');
    let data = await fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${format_cocktail}`);
    if(!data){
        return alert(`Unfortunately, we could not find ${cocktail_name}`)
    }
    let drink = await data.json();
    let drink_data = drink.drinks[0];
    return location.href = `/cocktails/${drink_data.idDrink}`
}