async function predict(){
    const data={
        city: document.getElementById('city').value,
        neighbourhood_group: document.getElementById('neighbourhood_group').value,
        neighbourhood: document.getElementById('neighbourhood').value,
        latitude: parseFloat(document.getElementById('latitude').value),
        longitude: parseFloat(document.getElementById('longitude').value),
        price: parseFloat(document.getElementById('price').value),
        minimum_nights: parseInt(document.getElementById('minimum_nights').value),
        number_of_reviews: parseInt(document.getElementById('number_of_reviews').value),
        reviews_per_month: parseFloat(document.getElementById('reviews_per_month').value),
        calculated_host_listings_count: parseInt(document.getElementById('calculated_host_listings_count').value),
        availability_365: parseInt(document.getElementById('availability_365').value),
        number_of_reviews_ltm: parseInt(document.getElementById('number_of_reviews_ltm').value)
    };

    const res=await fetch('/predict',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(data)
    });

    const result=await res.json();
    document.getElementById('output').innerText=result.prediction;
}