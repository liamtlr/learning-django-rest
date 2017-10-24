console.log("yo")


Vue.component('my-comp', {
  template: '<div> {{ whatever }} is twice {{ newValue}}</div>',
  props: ['whatever'],
  computed: {
    newValue: function(){
      console.log(this.whatever)
      return this.whatever / 2
    }
  },
})
var app = new Vue({
  el: '#app',
  data: {
    value: 3,
    dynamicishId: "your-mum",
    hams: [
      {yo: this.dynamicishId},
      {yo: "<3<3<3"},
      {yo: 445346}
    ]
  },
  computed: {
    computedValue: function(){
      return parseInt(this.value) * 2
    }
  }

})
