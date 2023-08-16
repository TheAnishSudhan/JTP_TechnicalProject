<template >
  <section >
  <div class="main-header">
    <div>
        <h1 class="cool-animation2">IndiaMate</h1>
    </div>
    <div >
        <h2 class="cool-animation3"> &nbsp Top 10 recommendations</h2>
    </div>
</div>
<div style="background-color:#cbdef8;">
  <div class="main-table" style="background-color:#e1ecfb" >
    <table class="table table-hover" >
            <thead>
              <tr style="background-color: #ffffff;">
                <th class="table-cell" scope="col">Place</th>
                <th class="table-cell" scope="col">City</th>
                <th class="table-cell" scope="col">A traveller's review</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(recommendation, index) in recommendations" :key="index">
                <td>{{ recommendation.Place }}</td>
                <td>{{ recommendation.City }}</td>
                <td>{{ recommendation.Raw_Review }}</td>
              </tr>
            </tbody>
          </table>
  </div>
  
    <div type="button" class="btn btn-primary link-button" style="align: center;">
          <router-link to="nlp" style="color: #ffffff;">Go back</router-link>
        </div>

</div>
    </section>
  </template>

<script>

  import axios from 'axios';
  
  export default {
    data() {
      return {
        recommendations: [],
      };
    },
    methods: {
      getPlaces() {
        const path = 'http://0.0.0.0:5001/places';
        axios.get(path)
          .then((res) => {
            this.recommendations = res.data.recommendations;
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
  margin: 5%;
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

template {
    background-color: #cbdef8;
    color: #cbdef8;
}

.btn-primary{
    color: #3b6fb8;
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