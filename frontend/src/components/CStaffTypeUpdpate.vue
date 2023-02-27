<script lang="ts">
import { concatList } from "@/utils/common";
import { IFMasterData } from "@/interfaces/common";
import { computed, defineComponent, ref } from "vue";
import CButton from "./CButton.vue";
import { ECommon } from "@/enums/common";
import { useStore } from "vuex";
import { ESStaff } from "@/enums/store";
import CSelection from "./CSelection.vue";

export default defineComponent({
  props: {
    updatedStaff: { type: Object, required: true },
    availableTypes: { type: Array, requied: () => [] as IFMasterData[] },
  },
  setup(props) {
    const store = useStore();
    const selectedId = ref(props.updatedStaff.type.id);
    const isChanged = computed(
      () => selectedId.value !== props.updatedStaff.type.id
    );
    async function update() {
      await store.dispatch(ESStaff.A_UPDATE_STAFF, {
        staff: props.updatedStaff,
        updateData: { type_id: selectedId.value },
      });
    }
    const log = (x: number) => {
      console.log(x);
    };
    return { concatList, update, log, ECommon, selectedId, isChanged };
  },
  components: { CButton, CSelection },
});
</script>

<template>
  <div class="wrap">
    <div class="info-row">
      <span class="material-icons">badge</span>
      {{
        concatList(
          [updatedStaff?.profile?.first_name, updatedStaff?.profile?.last_name],
          " "
        )
      }}
    </div>
    <div class="info-row">
      <span class="material-icons">contact_phone</span>
      {{ updatedStaff?.profile?.phone_number }}
    </div>
    <div class="info-row">
      <span class="material-icons">assignment_ind</span>
      <div class="container">
        <CSelection
          :selectList="availableTypes"
          :defaultID="updatedStaff?.type?.id"
          @select="(id) => (selectedId = id)"
        />
      </div>
    </div>
    <CButton v-if="isChanged" :name="ECommon.UPDATE" @click="update" />
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  flex-direction: column;
  gap: var(--s-medium);
}
.info-row {
  align-items: center;
  gap: var(--s-small);
  justify-content: left;
}
</style>
