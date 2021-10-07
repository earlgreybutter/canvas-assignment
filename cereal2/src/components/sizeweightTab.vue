<template>
  <div class="center">
    <FormulateForm
      v-model="values"
      :schema="schema"
      ref="sizeweighttab"
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
        // {
        //   "component": "div",
        //   "children": "Quantity Price"
        // },
        {
          type: "group",
          repeatable: true,
          name: "size-weight",
          validation: "required",
          addLabel: "+ Add row",
          children: [
            {
              component: "div",
              class: "input-row",
              children: [
                {
                  name: "size",
                  type: "number",
                  label: "Dimensions",
                  validation: "required|number|min:1",
                  min: "1",
                  // "@focus": "focus-qty",
                  // "error-behavior": "live",
                },
                {
                  name: "weight",
                  type: "number",
                  label: "Weight (lbs)",
                  validation: "required|number|min:1",
                  min: "1",
                  // "@focus": "focus-prc",
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

