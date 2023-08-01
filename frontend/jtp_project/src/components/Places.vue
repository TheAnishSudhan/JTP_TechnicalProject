<template>
    <section>
    <div class="main-header">
    <div>
        <h1 class="cool-animation2">TravelMate</h1>
    </div>
    <div>
        <h2 class="cool-animation3"> &nbsp Where do you want to go?</h2>
    </div>
</div>
<div class="main-table" style="background-color:#cbdef8">
    <table class="table table-hover">
            <thead>
              <tr style="background-color: #ffffff;">
                <th class="table-cell" scope="col">Place</th>
                <th class="table-cell" scope="col">Address</th>
                <th></th>
              </tr>
            </thead>
            <tbody  style="background-color #ffffff;">
              <tr v-for="(place, index) in places" :key="index">
                <td>{{ place.name }}</td>
                <td>{{ place.address }}</td>
              </tr>
            </tbody>
          </table>
</div>
        <div type="button" class="btn btn-primary link-button" style="align: center;">
          <router-link to="ping" style="color: #ffffff;">Go back</router-link>
        </div>
        

    </section>
  </template>

<script>

function button_redirect()
{ 
  this.$router.push('http://localhost:5001/ping');
}

  import axios from 'axios';
  
  export default {
    data() {
      return {
        places: [],
      };
    },
    methods: {
      getPlaces() {
        const path = 'http://localhost:5001/places';
        axios.get(path)
          .then((res) => {
            this.places = res.data.places;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
    created() {
      this.getPlaces();
    },
  };

</script>

<style>

.link-button {
  margin: 20%;
  align: center;
  text-align: center;
}

.main-table {
  margin-left: 20%;
  margin-right: 20%;
  align-items: center;
}

section {
  text-align: center;
  height: 100vh;
  background-color: #cbdef8;
  color: #cbdef8;

}
.table-cell{

  text-align: center;
}

.form-group {
    padding: 5%;
    font-size: 2rem;
}

template {
    background-color: #cbdef8;
    color: #cbdef8;
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

.cool-animation2 {

    color: #ffffff;

}
.cool-animation3 {
    
    color: #3b6fb8;

}

</style>