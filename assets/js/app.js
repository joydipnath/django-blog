var dashboard_app = new Vue({
  el: '#dashboard_contant',
  data: {
    name: 'Vue.js'
  },
  // define methods under the `methods` object
  methods: {
    show_dashboard_contant: function (event) {
      alert(this.id);
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    }

  }
});

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

// var example2 = new Vue({
//   el: '#example-2',
//   data: {
//     name: 'Vue.js'
//   },
//   // define methods under the `methods` object
//   methods: {
//     greet: function (event) {
//       // `this` inside methods points to the Vue instance
//       alert('Hello ' + this.name + '!')
//       // `event` is the native DOM event
//       if (event) {
//         alert(event.target.tagName)
//       }
//     }
//   }
// });