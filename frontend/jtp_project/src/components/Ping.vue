<template>
    <section>
    <div class="main-header landing-container" id="landing-container">
    <div>
        <h1 class="cool-animation2">TravelMate</h1>
    </div>
    <div>
        <h2 class="cool-animation3"> &nbsp Where do you want to go?</h2>
    </div>
</div>
<div class="main-form landing-container" id="main-form">
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="destination">Enter Destination City:</label>
        <input type="text" class="form-control" id="destination" placeholder="Enter location" v-model="destination" required>
      </div>
      <div class="form-group">
        <label for="category">Choose the kind of place you are looking for:</label>
        <!-- <input type="text" class="form-control" id="category" placeholder="Enter type" v-model="category" required> -->
        <select class="form-control" v-model="category" name="cars" id="cars">
        <option value="commercial.marketplace">Commercial / Marketplace</option>
        <option value="commercial.outdoor_and_sport">Commercial / Outdoor & Sport</option>
        <option value="commercial.hobby">Commercial / Hobby</option>
        <option value="commercial.gift_and_souvenir">Commercial / Gift & Souvenir</option>
        <option value="commercial.garden">Commercial / Garden</option>
        <option value="commercial.food_and_drink">Commercial / Food & Drink</option>
        <option value="commercial.art">Commercial / Art</option>
        <option value="catering.restaurant">Catering / Restaurant</option>
        <option value="catering.bar">Catering / Bar</option>
        <option value="catering.food_court">Catering / Food court</option>
        <option value="accomodation.hotel">Accomodation / Hotel</option>
        <option value="accomodation.hostel">Accomodation / Hostel</option>
        <option value="accomodation.guest_house">Accomodation / Guest House</option>
        <option value="entertainment.culture">Entertainment / Culture</option>
        <option value="entertainment.museum">Entertainment / Museum</option>
        <option value="entertainment.Zoo">Entertainment / Zoo</option>
        <option value="healthcare.hospital">Healthcare / Hospital</option>
        <option value="leisure.picnic">Leisure / Picnic</option>
        <option value="saab">Saab</option>
        <option value="mercedes">Mercedes</option>
        <option value="audi">Audi</option>
        </select>
      </div>
      <div class="form-group">
        <label for="limit">How many results would you like:</label>
        <input type="text" class="form-control" id="limit" placeholder="Enter type" v-model="limit" required>

      </div>

      <div class="form-group">
        <button type="submit" class="btn btn-primary" >Submit</button>
      </div>
      
    </form>
</div>
    </section>
  </template>
  
<script>
import axios from 'axios';

// const headers ={
//     'Content-Type' : 'application/json'
// }

let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
      "Authorization": "*",
      "Access-Control-Allow-Methods": "*",
      "Access-Control-Allow-Headers": "*",
  }
};

export default {
  name: 'Ping',
  data() {
    return {
    //   msg: '',
      destination: '',
      category: '',
      limit: '',
    };
  },
  methods: {
    async handleSubmit() {
      const formData = {
        destination: this.destination,
        category: this.category,
        limit: this.limit
      };
      try {
        // this.$router.push('/places');
        const response = await axios.post('http://localhost:5001/ping', formData, axiosConfig)
        .then((res) => {
            console.log("RESPONSE RECEIVED: ", res);
        })
        // console.log('status:', response.status)
        // this.msg = response.data.message;
      } catch (error) {
        this.msg = '';
      }
    },
  },
};

</script>

<style>

.form-group {
    padding: 5%;
    font-size: 2rem;
    color: #3b6fb8;
}

template {
    background-color: #cbdef8;

}

.btn-primary{
    color: #3b6fb8;
}

.landing-container {
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
background-color: #cbdef8;
    }

.main-header {

    text-align: center;
  padding: 100px 0;
  background-color: #cbdef8;
}

.h1 {
font-size: 5rem;
  font-weight: bold;
  color: #ffffff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  letter-spacing: 2px;
  line-height: 1.2;
  margin-bottom: 20px;
}
.h2 {
font-size: 2rem;
  font-weight: bold;
  color: #b3b3b3;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  letter-spacing: 2px;
  line-height: 1.2;
  margin-bottom: 10px;
}

@keyframes slideIn {
  0% {
    opacity: 0;
    transform: translateY(0);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.cool-animation2 {
    animation: slideIn 2s ease-in-out;
    color: #ffffff;

}
.cool-animation3 {
    animation: slideIn 4s ease-in-out;
    color: #3b6fb8;

}
</style>