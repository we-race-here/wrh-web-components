<template>
  <div>
     <v-app>
       <v-row class="ma-2">
      <v-col cols="12" sm="2">
        <b>Filters</b>

        <v-col  class="ma-0 pa-0">
          <v-text-field
            v-model="search"
            label="Search (Name ,Team)"
            single-line
            hide-details
          ></v-text-field>
          
        </v-col>

        <v-col class="ma-0 pa-0 mt-3">
          <div
            color="#8a8d93"
            elevation="0"
            class="d-flex justify-space-between"
          >
            <v-btn color="primary" outlined @click="ClearFilter">Clear</v-btn>

            <v-btn  @click="getEvent(null)">Search</v-btn>
          </div>
        </v-col>
      </v-col>
      <v-col >
        <!-- <b>Results</b> -->

        <v-data-table
          :loading="ClubLoader"
          dense
          :footer-props="{
            'items-per-page-options': ['all'],
          }"
          :headers="Eventheaders"
          :items="Club"
          item-key="name"
          :search="search"
          :options.sync="pagination_events"
          :server-items-length="totalCount"
          class="elevation-1 mt-2"
        >
          
        </v-data-table>
      </v-col>
    </v-row>
     </v-app>
    
    <!-- Filter Code -->

    <!-- Filter Code End-->
  </div>
</template>

<script>
import axios from "axios";
import {VBtn, VDataTable , VRow, VCol , VApp} from 'vuetify/lib'

export default {
  components: {
    VBtn, VDataTable,VRow,VCol,VApp
  },
  computed: {
    totalCount() {
      var count = 25;
      // this.Club.count
      if (this.Club ) {
        return this.Club.length;
      }
      return count;
    },
  },

  data() {
    return {
      Club: [],
      DateRange: [],
      State: null,
      StateList: [],
      Labels: [],
      DisciplineList: [],

      pagination_events: {},
      search: "",
      ClubLoader: false,
      Eventheaders: [
        {text: "Name", value: "name" },
        {text: "Race Type", value: "f_t" },
        {text: "Team Name", value: "tname" },
      ],
      is_featured: false,
      is_usac_sanctioned: false,
    };
  },
  mounted() {
    
  },
  watch: {
    pagination_events: {
      handler(value) {
        this.getEvent(value);
      },
      deep: true,
    },
  },
  methods: {
    ClearFilter() {
      this.State = null;
      this.search = null;
    },
    FormURL(event, endpoint) {
      var query_param = "";
      var link = endpoint;
      try {
        // Ordering Logic
        if (event && event.sortBy.length >= 1) {
          for (var [i, v] of event.sortBy.entries()) {
            if (event.sortDesc[i]) {
              query_param += "&ordering=-" + v + "&";
            } else {
              query_param += "&ordering=" + v + "&";
            }
          }
        }
        // Pagination
        if (event) {
          link += "&page=" + event.page;
        }

        // Filtering

        if (this.State) {
          link += "&club_aff_type__aff_type_description=" + this.State;
        }

        return link + query_param;
      } catch (err) {
        console.log(err);
        return link;
      }
    },
    getEvent(event) {
      this.Club = [];
      this.ClubLoader = true;
      axios
        .get(
          this.FormURL(event, "http://165.232.188.93:8004/api/teamresult/?") +
            "&search=" +
            this.search
        )
        .then((data) => {
          this.Club = data.data;
          this.ClubLoader = false;
        });
    },
  },
};
</script>

<style > 
  @import 'https://cdn.jsdelivr.net/npm/vuetify/dist/vuetify.min.css';
</style>
