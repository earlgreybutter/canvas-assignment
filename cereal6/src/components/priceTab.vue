<template>
  <div class="center">
    <FormulateForm
      v-model="values"
      :schema="schema"
      ref="pricetab"
      @validation="(validation = $event), sendup($event)"
    >
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
        // {
        //   "component": "div",
        //   "children": "Quantity Price"
        // },
        {
          type: "group",
          repeatable: true,
          name: "qty-price",
          validation: "required",
          addLabel: "+ Add row",
          children: [
            {
              component: "div",
              class: "input-row",
              children: [
                {
                  name: "quantity",
                  type: "number",
                  label: "Quantity",
                  validation: "required|number|min:1",
                  min: "1",
                  "@focus": "focus-qty",
                  // "error-behavior": "live",
                },
                {
                  name: "Price",
                  type: "number",
                  label: "$ Price",
                  validation: "required|number|min:1",
                  min: "1",
                  "@focus": "focus-prc",
                  // "error-behavior": "live",
                },
              ],
            },
          ],
        },
      ],
    };
  },
  methods: {
    sendup: function (payload) {
      this.$emit("firsttabupdated", payload.hasErrors);
    },
    validate() {
      return !this.validation.hasErrors;
    },
  },
};
</script>

