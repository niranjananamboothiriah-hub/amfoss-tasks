const apiURL =
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false";

const cryptoList = document.getElementById("cryptoList");
const wishlist = document.getElementById("wishlist");
const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const priceChart = document.getElementById("priceChart");

let allCoins = [];
let selectedCoin = null;


// ===============================
// LOAD CRYPTOCURRENCIES
// ===============================

fetch(apiURL)
    .then(response => response.json())
    .then(data => {

        allCoins = data;

        displayCoins(allCoins);

        // Show Bitcoin by default on the chart
        selectedCoin = allCoins[0];

        loadChart(selectedCoin, 1);

    })
    .catch(error => {
        console.error("Error loading cryptocurrency data:", error);
    });


// ===============================
// DISPLAY CRYPTOCURRENCY CARDS
// ===============================

function displayCoins(coins) {

    cryptoList.innerHTML = "";

    coins.forEach(coin => {

        const card = document.createElement("div");

        card.classList.add("crypto-card");

        card.innerHTML = `
            <h3>${coin.name}</h3>
            <p>${coin.symbol.toUpperCase()}</p>
            <p>$${coin.current_price}</p>
            <p>24H: ${coin.price_change_percentage_24h !== null
                ? coin.price_change_percentage_24h.toFixed(2)
                : "N/A"}%</p>

            <button class="wishlist-btn">
                ⭐ Add to Wishlist
            </button>
        `;


        // ===============================
        // CLICK CARD → SHOW CHART
        // ===============================

        card.addEventListener("click", event => {

            // Don't open chart when wishlist button is clicked
            if (event.target.classList.contains("wishlist-btn")) {
                return;
            }

            selectedCoin = coin;

            loadChart(selectedCoin, 1);

        });


        // ===============================
        // WISHLIST BUTTON
        // ===============================

        const wishlistButton =
            card.querySelector(".wishlist-btn");


        wishlistButton.addEventListener("click", event => {

            event.stopPropagation();

            // Check whether coin is already in wishlist
            const alreadyAdded =
                wishlist.querySelector(
                    `[data-id="${coin.id}"]`
                );


            if (alreadyAdded) {

                return;

            }


            // Create wishlist item
            const item = document.createElement("div");

            item.setAttribute("data-id", coin.id);

            item.innerHTML = `
                <h3>${coin.name}</h3>
                <p>${coin.symbol.toUpperCase()}</p>
                <p>$${coin.current_price}</p>
            `;


            wishlist.appendChild(item);

        });


        cryptoList.appendChild(card);

    });

}


// ===============================
// SEARCH FUNCTION
// ===============================

function searchCrypto() {

    const searchTerm =
        searchInput.value.trim().toLowerCase();


    if (searchTerm === "") {

        displayCoins(allCoins);

        return;

    }


    const results =
        allCoins.filter(coin =>
            coin.name.toLowerCase().includes(searchTerm) ||
            coin.symbol.toLowerCase().includes(searchTerm)
        );


    displayCoins(results);


    // If search has results,
    // show the first result on the chart

    if (results.length > 0) {

        selectedCoin = results[0];

        loadChart(selectedCoin, 1);

    }

}


// ===============================
// SEARCH BUTTON
// ===============================

searchButton.addEventListener("click", searchCrypto);


// ===============================
// SEARCH USING ENTER KEY
// ===============================

searchInput.addEventListener("keydown", event => {

    if (event.key === "Enter") {

        searchCrypto();

    }

});


// ===============================
// PRICE CHART
// ===============================

function loadChart(coin, days) {

    const chartURL =
        `https://api.coingecko.com/api/v3/coins/${coin.id}/market_chart?vs_currency=usd&days=${days}`;


    fetch(chartURL)

        .then(response => response.json())

        .then(data => {

            drawChart(data.prices);

        })

        .catch(error => {

            console.error("Error loading chart:", error);

        });

}


// ===============================
// DRAW CHART
// ===============================

function drawChart(prices) {

    const ctx = priceChart.getContext("2d");

    const width = priceChart.width;
    const height = priceChart.height;


    // Clear old chart
    ctx.clearRect(0, 0, width, height);


    if (!prices || prices.length === 0) {

        return;

    }


    const values =
        prices.map(price => price[1]);


    const minPrice =
        Math.min(...values);

    const maxPrice =
        Math.max(...values);


    const padding = 40;


    ctx.beginPath();


    prices.forEach((price, index) => {

        const x =
            padding +
            (index / (prices.length - 1)) *
            (width - padding * 2);


        const y =
            height -
            padding -
            ((price[1] - minPrice) /
                (maxPrice - minPrice || 1)) *
            (height - padding * 2);


        if (index === 0) {

            ctx.moveTo(x, y);

        } else {

            ctx.lineTo(x, y);

        }

    });


    ctx.strokeStyle = "#2f6df6";

    ctx.lineWidth = 3;

    ctx.stroke();

}


// ===============================
// TIME RANGE BUTTONS
// ===============================

const timeButtons =
    document.querySelectorAll(".time-buttons button");


timeButtons.forEach(button => {

    button.addEventListener("click", () => {

        if (!selectedCoin) {

            return;

        }


        const text =
            button.textContent.trim();


        let days;


        if (text === "24H") {

            days = 1;

        } else if (text === "1W") {

            days = 7;

        } else if (text === "1M") {

            days = 30;

        } else if (text === "3M") {

            days = 90;

        } else if (text === "1Y") {

            days = 365;

        }


        loadChart(selectedCoin, days);

    });

});

const themeButton = document.getElementById("themeButton");

themeButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        themeButton.textContent = "☀️ Light Mode";
    } else {
        themeButton.textContent = "🌙 Dark Mode";
    }
});
