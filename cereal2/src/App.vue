<template>
  <div id="app">
    <div>
      <form-wizard
        @on-complete="onComplete"
        title="profitable.ai"
        subtitle="Let's Get Profitable!!"
        color="#9ccc14"
        error-color="#a94442"
        shape="tab"
      >
        <tab-content title="Project Name" icon="ti-info">
          <projectname ref="project-name"> </projectname>
        </tab-content>

        <tab-content title="Marketplace" icon="ti-shopping-cart">
          <marketplacetab ref="marketplacetab"> </marketplacetab>
        </tab-content>

        <tab-content title="Category" icon="ti-layers-alt">
          <categorytab ref="categorytab"> </categorytab>
        </tab-content>

        <tab-content title="Origin" icon="ti-location-pin">
          <origintab ref="origintab"> </origintab>
        </tab-content>

        <tab-content
          title="Pricing"
          icon="ti-money"
          :before-change="validateFirstTab"
        >
          <pricetab
            ref="pricetab"
            @firsttabupdated="error = validateit($event)"
          >
          </pricetab>
        </tab-content>

        <tab-content title="Size/Weight" icon="ti-package">
          <sizeweighttab ref="sizeweighttab"> </sizeweighttab>
        </tab-content>

        <tab-content title="Shipping" icon="ti-truck"> </tab-content>

        <tab-content title="Marketing" icon="ti-video-clapper">
          <img
            src="https://c.tenor.com/jvbFCSjX67sAAAAC/surprise-motherfucker.gif"
            alt="Flowers in Chania"
            class="center"
          />
        </tab-content>
      </form-wizard>
    </div>
  </div>
</template>

<script>
import pricetab from "./components/priceTab.vue";
import projectname from "./components/project-name.vue";
import marketplacetab from "./components/marketplaceTab.vue";
import categorytab from "./components/categoryTab.vue";
import origintab from "./components/originTab.vue";
import sizeweighttab from "./components/sizeweightTab.vue";

export default {
  name: "app",
  components: {
    pricetab,
    projectname,
    marketplacetab,
    categorytab,
    origintab,
    sizeweighttab,
  },
  data() {
    return {
      model: {},
    };
  },

  methods: {
    onComplete: function () {
      alert("Yay. Done!");
    },
    validateFirstTab: function () {
      return this.$refs.pricetab.validate();
    },
    validateSecondTab: function () {
      return this.$refs.secondTabForm.validate();
    },
    validateit: function (validationpaylaod) {
      return !validationpaylaod;
    },
  },
};
</script>

<style>
@import "./assets/styles/profitable.css";
</style>