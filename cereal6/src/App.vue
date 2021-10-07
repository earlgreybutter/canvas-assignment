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
        <tab-content title="STEP01" icon="ti-info">
          <step01 ref="step01"> 
          </step01>
          <!-- <mxgraphtest ref="graph-test1"> </mxgraphtest> -->
        </tab-content>

        <tab-content title="STEP02" icon="ti-shopping-cart">
          <marketplacetab ref="marketplacetab"> </marketplacetab>
          <!-- <mxgraphtest2 ref="graph-test2"> </mxgraphtest2> -->
        </tab-content>

        <tab-content title="STEP03" icon="ti-layers-alt">
          <categorytab ref="categorytab"> </categorytab>
        </tab-content>

        <tab-content
          title="STEP04"
          icon="ti-money"
          :before-change="validateFirstTab"
        >
          <pricetab
            ref="pricetab"
            @firsttabupdated="error = validateit($event)"
          >
          </pricetab>
        </tab-content>

        <tab-content title="STEP05" icon="ti-package">
          <sizeweighttab ref="sizeweighttab"> </sizeweighttab>
        </tab-content>

        <!-- <tab-content title="Marketing" icon="ti-video-clapper">
          <img
            src="https://c.tenor.com/jvbFCSjX67sAAAAC/surprise-motherfucker.gif"
            alt="Flowers in Chania"
            class="center"
          />
        </tab-content> -->
      </form-wizard>
    </div>
  </div>
</template>

<script>
import step01 from "./components/step01.vue";
import marketplacetab from "./components/marketplaceTab.vue";
import categorytab from "./components/categoryTab.vue";
import pricetab from "./components/priceTab.vue";
import sizeweighttab from "./components/sizeweightTab.vue";
// import mxgraphtest from "./components/GraphWrapper.vue";
// import mxgraphtest2 from "./components/cloudgraph.vue";

export default {
  name: "app",
  components: {
    // projectname,
    pricetab,
    marketplacetab,
    categorytab,
    sizeweighttab,
    step01,
    // mxgraphtest,
    // mxgraphtest2
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
@import "./assets/styles/custom.css";
</style>