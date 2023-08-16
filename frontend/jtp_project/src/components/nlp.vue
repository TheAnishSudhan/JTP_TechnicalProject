<template>
    <section>
    <div class="main-header landing-container" id="landing-container">
    <div>
        <h1 class="cool-animation2">IndiaMate</h1>
    </div>
    <div>
        <h2 class="cool-animation3"> &nbsp Find out where you want to be</h2>
    </div>

</div>
<div class="main-form landing-container" id="main-form">
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="user_input">What do you want to do &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input type="text" class="form-control" id="user_input" placeholder="I want to go to an old temple" v-model="user_input" required>
      </div>
      <div class="button-group">
        <button type="submit" class="btn btn-primary" >Submit</button>
        <router-link to="places" style="padding-left: 2%;">
        <button type="submit" class="btn btn-primary" >Go to results</button>
        </router-link>
      </div>
      
    </form>
</div>
    </section>
  </template>
  
<script>
import axios from 'axios';

let axiosConfig = {
  headers: {
      'Content-Type': 'application/json;charset=UTF-8',
      "Access-Control-Allow-Origin": "*",
      "authorization": "*",
      "Access-Control-Allow-Methods": "OPTIONS, GET, POST, PUT, DELETE",
      "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization",
  }
};

export default {
  name: 'NLP',
  data() {
    return {
      user_input: '',
    };
  },
  methods: {
    async handleSubmit() {
      const formData = {
        user_input: this.user_input,
      };
      try {
        const response = await axios.post('http://0.0.0.0:5001/nlp', formData, axiosConfig)
        .then((res) => {
            console.log("RESPONSE RECEIVED: ", res);
        })
        console.log('status:', response.status)
      } catch (error) {
        console.log(error.response.data)
      }
    },
    //   async handleSubmit() {    
    //     fetch('http://localhost:5001/nlp', {
    //             method: 'POST',
    //             headers: {
    //                 'Accept': 'application/json',
    //                 'Content-Type': 'application/json'
    //             },
    //             body: JSON.stringify(this.user_input)
    //         })
    //         .then(response => response.json())
    //         .then(data => this.user_input = data)
    // }
  },
};

</script>

<style>

.form-group {
    /* padding: 1%; */
    font-size: 5rem;
    color: #3b6fb8;
}

.button-group {

  padding: 5%;
  display: flexbox;
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
      /* display: flexbox; */
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