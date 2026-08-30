# Task 04 – The Bull & The Bear

## Objective

The objective of this task was to build a Crypto Tracker web application using HTML, CSS, JavaScript, and a cryptocurrency API.

The application should allow users to view live cryptocurrency market data, search for cryptocurrencies, view price charts for different time ranges, add cryptocurrencies to a wishlist, and switch between Dark Mode and Light Mode.



## Technologies Used

- HTML
- CSS
- JavaScript
- CoinGecko API
- HTML Canvas for the price chart
- Git and GitHub



## 1. Creating the Project

I created a `Task-04` folder inside my `amfoss-tasks` directory.

The project contains the following files:

- `index.html`
- `style.css`
- `script.js`
- `logbook.md`

The HTML file provides the structure of the webpage, CSS is used for styling, and JavaScript is used to fetch API data and implement the interactive features.



## 2. Understanding and Using the API

I used the CoinGecko API to obtain cryptocurrency market data.

The API endpoint used was:

https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false

The API returns information such as:

- Cryptocurrency name
- Symbol
- Current price
- Market capitalization
- Market rank
- 24-hour price change
- Other market information

I opened the API link in the browser to verify that the API was returning JSON data successfully.



## 3. Fetching Cryptocurrency Data

In JavaScript, I used the `fetch()` function to request data from the CoinGecko API.

The response was converted into JSON using:

javascript
response.json()

The received cryptocurrency data was then processed using forEach() and displayed dynamically on the webpage.

This helped me understand how JavaScript can communicate with an external API and use the returned data in a webpage.

4. Market Overview

I created a Market Overview section where cryptocurrency cards are displayed.

Each card contains:

Cryptocurrency name
Symbol
Current price
24-hour percentage change
Add to Wishlist button

The cards are generated dynamically using JavaScript instead of manually creating every cryptocurrency card in HTML.

5. Cryptocurrency Search

I added a search input and Search button.

The user can enter a cryptocurrency name such as:

Bitcoin

The application searches through the cryptocurrency data obtained from the API and displays the matching result.

This helped me understand how JavaScript can be used to filter data based on user input.

6. Price Chart

I implemented a price chart using an HTML <canvas> element.

The application provides multiple time-range options:

24H
1W
1M
3M
1Y

When a time range is selected, the application obtains the corresponding market data and updates the chart.

This helped me understand how API data can be converted into a visual representation.

7. Wishlist Feature

I implemented a wishlist feature for cryptocurrencies.

Each cryptocurrency card contains an:

 * "Add to Wishlist" button:

When the button is clicked, the selected cryptocurrency is added to the My Wishlist section.

The wishlist displays information such as:

Cryptocurrency name
Symbol
Current price

I used JavaScript event listeners to detect button clicks and dynamically add the selected cryptocurrency to the wishlist.

8. Dark Mode / Light Mode:

I implemented a Dark Mode / Light Mode toggle.

The button allows the user to switch between the two themes.

JavaScript is used to change the theme, while CSS defines the appearance of the different modes.

This improved the usability and appearance of the application.

9. Testing:

I tested the different features of the application.

Tests performed
Checked whether cryptocurrency data loads correctly.
Searched for Bitcoin.
Checked that cryptocurrency cards are displayed.
Tested the Add to Wishlist button.
Checked whether the wishlist displays the selected cryptocurrency.
Tested the 24H chart.
Tested the 1W chart.
Tested the 1M chart.
Tested the 3M chart.
Tested the 1Y chart.
Tested Dark Mode.
Tested Light Mode.
Checked the browser console for errors.

The API was also opened directly in the browser to verify that it was returning data correctly.

10. Problems Faced:
Problem 1: Search was not initially displaying the expected result

I checked the JavaScript code and the browser console and corrected the search functionality.

Problem 2: Wishlist was initially empty

I modified the JavaScript so that the wishlist button creates a new wishlist item and appends it to the wishlist section.

Problem 3: Multiple wishlist entries were being created

While implementing the wishlist functionality, I encountered an issue where clicking the button could create repeated entries.

I corrected the JavaScript event handling and tested the feature again.

Problem 4: Chart time ranges

Some chart time ranges required different API parameters. I tested the different buttons and corrected the JavaScript so that the chart updates according to the selected range.

11. What I Learned

Through this task, I learned:

How to dynamically create HTML elements using JavaScript.
How to use forEach() to process API data.
How to use DOM methods such as createElement() and appendChild().
How to implement search functionality.
How to create a wishlist feature.
How to display data using a canvas-based chart.
How to implement Dark Mode and Light Mode.
How HTML, CSS, JavaScript, and APIs work together to create an interactive web application.

12. Final Result:

The final application is a responsive Crypto Tracker that provides cryptocurrency market information in one place.

The application includes:

Live cryptocurrency market data
Cryptocurrency search
Market overview
Current prices
24-hour price changes
Interactive price chart
Multiple time ranges
Wishlist functionality
Dark Mode / Light Mode
Clean and intuitive interface

The project was tested locally in the browser and the major features were verified to be working.

13. Conclusion

This task helped me understand how real-world web applications can use APIs to obtain live data and dynamically display it to users.

I gained practical experience with HTML, CSS, JavaScript, APIs, DOM manipulation, event handling, data visualization, and debugging.

The task also gave me a better understanding of how frontend applications interact with external services to provide real-time information.
