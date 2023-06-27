start = 2;
var categorySearch = "";
var querySearch ="";
// For movies that have two different names, the search may not work

document.addEventListener("DOMContentLoaded", function() {
    if (window.innerWidth < 1440) {
        if (document.querySelectorAll(".textContainerThings")) {
            document.querySelectorAll(".textContainerThings").forEach(item=>{
                item.style.justifyContent = 'space-around';
            })
        }
    }
    if (document.querySelector("title").innerHTML == " All Movies ") {
        fetch("https://api.themoviedb.org/3/discover/movie?api_key=ab83a2c7a7f36490276cecada647c422")
        .then(response=>response.json())
        .then(movies=>{
            movies['results'].forEach(movie => {
                if (movie['original_title'] === "Harry Potter and the Philosopher's Stone") {
                    movie['original_title'] = "Harry Potter and the Sorcerer's Stone"
                }
                const element = document.createElement("div");
                element.innerHTML = `<h2>${movie['original_title']}</h2>
                                    <img class="moviePoster" src="https://image.tmdb.org/t/p/original/${movie['poster_path']}">
                `;
                element.id = movie['id'];
                element.className = "movie";
                element.style.border = "solid";
                document.querySelector("#container").append(element);
                element.addEventListener("click", () => {
                    window.location.href = "/movie/" + movie['id'];
                });
            });
        })
        .catch(err=>console.log(err))
        window.onscroll = () => {
            if (window.innerHeight + window.scrollY + 0.5 >= document.body.offsetHeight) {
                load();
            }
        }
        
    }
    
    if (document.querySelector("#search")) {
        document.querySelector("#search").addEventListener("submit", function(event) {
            search(event);
        })
    }
    

    if (document.querySelector("title").innerHTML === "Search") {
        console.log(categorySearch, querySearch)
    }
})

function load() {
    console.log("load")
    console.log(start)
    console.log(`IH: ${window.innerHeight} Scroll: ${window.scrollY} offsetheight: ${document.body.offsetHeight}`)
    if (start != 501) {
        fetch(`https://api.themoviedb.org/3/discover/movie?api_key=ab83a2c7a7f36490276cecada647c422&page=${start}`)
        .then(response=>response.json())
        .then(movies=>{
            movies['results'].forEach(movie => {
                const element = document.createElement("div");
                element.innerHTML = `<h2>${movie['original_title']}</h2>
                                    <img class="moviePoster" src="https://image.tmdb.org/t/p/original/${movie['poster_path']}">
                `;
                element.id = movie['original_title'];
                element.className = "movie";
                element.style.border = "solid";
                document.querySelector("#container").append(element);
                element.addEventListener("click", () => {
                    window.location.href = "/movie/" + movie['id'];
                });
            });
        })
        .catch(err=>console.log(err))
        start++;
    }

}

function search(event) {
    const query = document.querySelector("#query");
    if (query.value === "") {
        document.querySelector("#searchErr").style.display = 'block';
    }
    else {
        window.location.href = "/search/Movie%20Title/" + query.value;
    }
    event.preventDefault();

}

function makePart(id, container) {
    fetch(`https://api.themoviedb.org/3/movie/${id}?api_key=ab83a2c7a7f36490276cecada647c422`)
    .then(response=>response.json())
    .then(movie => {
        const element = document.createElement("div");
        element.innerHTML = `<h2>${movie['original_title']}</h2>
                            <img class="moviePoster" src="https://image.tmdb.org/t/p/original/${movie['poster_path']}">
        `;
        element.id = movie['original_title'];
        element.className = "movie";
        element.style.border = "solid";
        document.querySelector(container).append(element);
        element.addEventListener("click", () => {
            window.location.href = "/movie/" + movie['id'];
        });
    })
}