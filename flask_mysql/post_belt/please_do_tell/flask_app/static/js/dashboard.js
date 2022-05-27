function onSearchFriend(){
    //changes url to /friends/search/user_name
}

function getDrink(){
    //change input string so spaces are underscores
    let searchDiv = document.querySelector('.search_cocktail')
    let cocktail_name = searchDiv.value;
    cocktail_name = cocktail_name.replace(' ','_');
    
}