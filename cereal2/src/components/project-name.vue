<template>
  <div class="center">
    <FormulateForm
      v-model="values"
      :schema="schema"
      ref="project-name"
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
          type: "text",
          label: "Project Name",
          name: "project-name",
          validation: "required",
          "error-behavior": "live",
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
