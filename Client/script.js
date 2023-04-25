function populateLocations() {
    let locationDropdown = document.getElementById("location");
    fetch("http://127.0.0.1:5000/get_location_names")
        .then(res => res.json())
        .then(out => {
            out.locations.forEach(loc => {
                let option = document.createElement("option");
                option.text = loc;
                option.value = loc;
                locationDropdown.appendChild(option);
            });
        })
        .catch(err => {console.log(err)});
}

function handlePredictionSubmit(event) {
    let location = document.getElementById("location").value;
    let sqft = document.getElementById("sqft").value;
    let size_num = document.getElementById("size_num").value;
    let bath = document.getElementById("bath").value;
    let formData = new FormData();
    formData.append("location", location);
    formData.append("total_sqft", sqft);
    formData.append("size_num", size_num);
    formData.append("bath", bath);
    fetch("http://127.0.0.1:5000/predict_home_price", {
        method: "POST",
        body: formData,
    })
        .then(res => res.json())
        .then(out => {
            let url = "http://127.0.0.1:5500/prediction.html?location="+encodeURIComponent(location)+"&sqft="+encodeURIComponent(sqft)+"&bed="+encodeURIComponent(size_num)+"&bath="+encodeURIComponent(bath)+"&price="+encodeURIComponent(out.estimated_price);
            document.location.href = url;
        })
        .catch(err => {console.log(err)});
    event.preventDefault();
}

window.addEventListener("DOMContentLoaded", (event) => {
    const el = document.getElementById('predictionForm');
    if (el) {
      el.addEventListener('submit', handlePredictionSubmit);
    }
});

function load_data() {
    let url = document.location.href;
    let params = url.split('?')[1].split('&');
    let data = {};
    let tmp;
    for (let i = 0; i < params.length; i++) {
        tmp = params[i].split('=');
        data[tmp[0]] = tmp[1];
    }

    console.log(data);
    document.getElementById("input_location").innerHTML = decodeURIComponent(data["location"]);
    document.getElementById("input_sqft").innerHTML = data["sqft"];
    document.getElementById("input_bed").innerHTML = data["bed"];
    document.getElementById("input_bath").innerHTML = data["bath"];
    document.getElementById("output_price").innerHTML = data["price"];
}