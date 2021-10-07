<template>
  <div class="center">
    <FormulateForm
      v-model="values"
      :schema="schema"
      ref="origintab"
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
          name: "origin",
          label: "Select product origin",
          value: "US",
          validation: "required",
          options: ["US", "China", "EU", "Japan", "South America"],
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

