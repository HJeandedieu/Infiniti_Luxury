// 1. Function to get today's day
function getTodayDay() {
  return new Promise((resolve) => {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const today = new Date().getDay();
    resolve(days[today]);
  });
}

// 2. Function to get the meal of the day
function getMealOfTheDay(day) {
  return new Promise((resolve, reject) => {
    const meals = {
      Monday: "Spaghetti Bolognese",
      Tuesday: "Grilled Chicken Salad",
      Wednesday: "Vegetable Stir Fry",
      Thursday: "Beef Tacos",
      Friday: "Fish and Chips",
      Saturday: "Pizza",
      Sunday: "Roast Chicken"
    };

    const meal = meals[day];
    if (meal) resolve(meal);
    else reject("No meal planned for today");
  });
}

// 3. Using the promises
getTodayDay()
  .then(day => {
    console.log("Today is:", day);
    return getMealOfTheDay(day);
  })
  .then(meal => {
    console.log("Meal of the day:", meal);
  })
  .catch(error => {
    console.log("Error:", error);
  });
