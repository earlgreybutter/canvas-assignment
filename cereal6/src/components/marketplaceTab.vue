<template>
  <div class="center">
    <FormulateForm
      v-model="values"
      :schema="schema"
      ref="marketplacetab"
      @validation="(validation = $event), sendup($event)"
    >
    </FormulateForm>
    <!-- <pre>
            {{validation}}
        </pre>   -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      values: {},
      validation: {},
      schema: [
        {
          type: "select",
          name: "marketplace",
          label: "Choose your marketplace",
          value: "Amazon",
          validation: "required",
          options: {
            Amazon: "Amazon",
            ebay: "ebay",
            Etsy: "Etsy",
          },
        },
      ],
    };
  },
  props: {
    // radius: {
    //   type: Number,
    //   default: 50
    // }
  },
  watch: {
  //   radius() {
  //     this.draw(this.radius)
  //  }
  },
  methods: {
    // sendup: function (payload) {
    //     this.$emit('firsttabupdated', payload.hasErrors);
    //     },
    validate() {
      return !this.validation.hasErrors;
    },
    // draw(radius) {
    //   // this.ctx.beginPath()
    //   // this.ctx.clearRect(0, 0, 200, 200)
    //   // this.ctx.arc(100, 100, radius, 0, Math.PI * 2)
    //   // this.ctx.fill()
    // }
  },
  mounted() {
    console.log(this.$el)
    // this.ctx = this.$el.getContext('2d')
    //this.draw(this.radius)
  }
};
</script>

<style scoped>
.canvas {
  border: 1px solid #000;
}
</style>