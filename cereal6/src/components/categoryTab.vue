<template>
  <div class="center">
    <FormulateForm v-model="values" :schema="schema" ref="categorytab">
    </FormulateForm>
    <canvas width="300px" height="400px"></canvas>
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
          name: "category",
          label: "Choose product category",
          value: "Clothing",
          validation: "required",
          options: ["Clothing", "Electronics", "Children", "Toys", "Home"],
        },
      ],
    };
  },
  methods: {
    // sendup: function (payload) {
    //     this.$emit('firsttabupdated', payload.hasErrors);
    //     },
    validate() {
      return !this.validation.hasErrors;
    },
  },
};
</script>
