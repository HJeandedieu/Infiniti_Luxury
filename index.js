        //VEHICLES DROPDOWN
        const vehicle_button = document.getElementById('vehicle_button');
        const vehicle_button_close = document.getElementById("vehicle_close");
        const vehicle_dropdown = document.getElementById('vehicles_dropdown');

        // SHOP DROPDOWN
        const shop_button = document.getElementById('shop_button');
        const shop_button_close = document.getElementById("shop_close");
        const shop_dropdown = document.getElementById("shop_dropdown");

        // OWNERS DROPDONW
        const owners_button = document.getElementById("owners_button");
        const owners_button_close = document.getElementById("owners_close")
        const owners_dropdown = document.getElementById("owners_dropdown");

        // SERVICE DROPDOWN
        const service_button = document.getElementById("service_button");
        const service_button_close = document.getElementById("service_close")
        const service_dropdown = document.getElementById("service_dropdown")
        
        // NECESSITIES
        const main = document.getElementById('main');
        const footer = document.getElementById('footer');

        vehicle_button.addEventListener('click', (e)=>{
            e.preventDefault();
            shop_dropdown.classList.add("hidden");
            owners_dropdown.classList.add("hidden");
            service_dropdown.classList.add("hidden");
            if(vehicle_dropdown.classList.contains('hidden')){
                vehicle_dropdown.classList.remove("hidden");
                main.classList.add("hidden");
                footer.classList.add("hidden");
            }else{
                vehicle_dropdown.classList.add("hidden");
                main.classList.remove("hidden");
                footer.classList.remove("hidden");
            }
        })

        // CLOSING MECHANISM

        vehicle_button_close.addEventListener("click", (e)=>{
            e.preventDefault();
            vehicle_dropdown.classList.add("hidden");
            main.classList.remove("hidden");
            footer.classList.remove("hidden");
        })

        // SHOP DROPDOWN

        shop_button.addEventListener("click", (e)=>{
            e.preventDefault();
            vehicle_dropdown.classList.add("hidden");
            owners_dropdown.classList.add("hidden");
            service_dropdown.classList.add("hidden");
            if(shop_dropdown.classList.contains("hidden")){
                shop_dropdown.classList.remove("hidden");
                main.classList.add("hidden");
                footer.classList.add("hidden");
            }else{
                shop_dropdown.classList.add("hidden");
                main.classList.remove("hidden");
                footer.classList.remove("hidden");
            }
        })

        //CLOSING MECHANISM

        shop_button_close.addEventListener("click", (e)=>{
            e.preventDefault();
            shop_dropdown.classList.add("hidden");
            main.classList.remove("hidden");
            footer.classList.remove("hidden");
        })


        // OWNERS DROPDOWN

        owners_button.addEventListener("click", (e)=>{
            e.preventDefault();
            shop_dropdown.classList.add("hidden");
            vehicle_dropdown.classList.add("hidden");
            service_dropdown.classList.add("hidden");
            if(owners_dropdown.classList.contains("hidden")){
                owners_dropdown.classList.remove("hidden");
                main.classList.add("hidden");
                footer.classList.add("hidden");
            }else{
                owners_dropdown.classList.add("hidden");
                main.classList.remove("hidden");
                footer.classList.remove("hidden");
            }
        })

        // CLOSING MECHANISM
        owners_button_close.addEventListener("click", (e)=>{
            e.preventDefault();
            owners_dropdown.classList.add("hidden");
            main.classList.remove("hidden");
            footer.classList.remove("hidden");
        })


        // SERVICES DROPDOWN

        service_button.addEventListener("click", (e)=>{
            e.preventDefault();
            shop_dropdown.classList.add("hidden");
            owners_dropdown.classList.add("hidden");
            vehicle_dropdown.classList.add("hidden");
            if(service_dropdown.classList.contains("hidden")){
                service_dropdown.classList.remove("hidden");
                main.classList.add("hidden");
                footer.classList.add("hidden");
            }else{
                service_dropdown.classList.add("hidden");
                main.classList.remove("hidden");
                footer.classList.remove("hidden");
            }
        })

        // CLOSING MECHANISM
        service_button_close.addEventListener("click", (e)=>{
            e.preventDefault();
            service_dropdown.classList.add("hidden");
            main.classList.remove("hidden");
            footer.classList.remove("hidden");
        })



// Center of Canada
const map = L.map('map').setView([56.1304, -106.3468], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Marker in Ottawa (capital of Canada)
L.marker([45.4215, -75.6972])
  .addTo(map)
  .bindPopup("Ottawa, Canada")
  .openPopup();

  