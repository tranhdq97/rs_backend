<script lang="ts">
import CTableRow from "@/components/CTableRow.vue";
import { ETPCommon, ETPProfile, ETPStaff } from "@/enums/table_property";
import { ESAuth, ESStaff, ESStaffType } from "@/enums/store";
import { defineComponent, computed, ref } from "vue";
import { useStore } from "vuex";
import { IFStaff, IFStaffRep } from "@/interfaces/staff";
import { useRouter } from "vue-router";
import { ERouter } from "@/enums/routers";
import { formRouter } from "@/utils/route";
import { ERouterParams } from "@/enums/common";
import LAModal from "@/layouts/LAModal.vue";
import { concatList } from "@/utils/common";
import CStaffTypeUpdpate from "@/components/CStaffTypeUpdpate.vue";
import { IFMasterData } from "@/interfaces/common";

export default defineComponent({
  setup() {
    const columns: string[] = [
      ETPCommon.ID,
      ETPProfile.FIRST_NAME,
      ETPProfile.LAST_NAME,
      ETPProfile.SEX,
      ETPProfile.DOB,
      ETPProfile.PHONE_NUMBER,
      ETPStaff.EMAIL,
      ETPProfile.ADDRESS,
      ETPCommon.TYPE,
      ETPCommon.DETAIL,
    ];
    const classes = {
      id: "text-center",
      sex: "text-center",
      first_name: "justify-content-left",
      last_name: "justify-content-left",
      phone_number: "justify-content-right",
      email: "justify-content-right lowercase",
      dob: "no-wrap",
      detail: "text-center",
    };
    const icons = {
      detail: "info_outline",
      type: "loop",
    };
    const store = useStore();
    const router = useRouter();
    const user = store.getters[ESAuth.G_USER];
    store.dispatch(ESStaffType.A_GET_STAFF_TYPES);
    store.dispatch(ESStaff.A_GET_STAFFS);
    const staffs = computed(() => store.getters[ESStaff.G_STAFFS](user));
    const types = computed<IFMasterData[]>(
      () => store.getters[ESStaffType.G_STAFF_TYPES]
    );
    const isStatusChanging = ref(false);
    const modalStaff = ref<IFStaff>(staffs.value[0] || undefined);
    const availableTypes = ref<IFMasterData[]>([]);
    async function clickRow(column: string, row: IFStaffRep) {
      if (column === ETPCommon.DETAIL) {
        const routeURL = formRouter(ERouter.STAFF, [
          { key: ERouterParams.INDEX, value: row.id },
        ]);
        router.push(routeURL);
      } else if (column === ETPCommon.TYPE) {
        const staffObj = store.getters[ESStaff.G_STAFF](row.id);
        const user = store.getters[ESAuth.G_USER];
        modalStaff.value = staffObj;
        availableTypes.value = types.value.filter(
          (item) => (item.id || Infinity) > user.type.id
        );
        isStatusChanging.value = true;
      } else return;
    }
    return {
      columns,
      classes,
      staffs,
      icons,
      isStatusChanging,
      modalStaff,
      availableTypes,
      clickRow,
      concatList,
    };
  },
  components: { CTableRow, LAModal, CStaffTypeUpdpate },
});
</script>

<template>
  <div class="container wrap">
    <table>
      <CTableRow :isHeader="true" :columns="columns" class="header" />
      <tbody>
        <CTableRow
          v-for="(row, i) in staffs"
          :key="i"
          :isHeader="false"
          :columns="columns"
          :row="row"
          :icons="icons"
          :classes="classes"
          @spanClicked="(column) => clickRow(column, row)"
        />
      </tbody>
    </table>
    <LAModal v-if="isStatusChanging" @close="isStatusChanging = false">
      <CStaffTypeUpdpate
        :updatedStaff="modalStaff"
        :availableTypes="availableTypes"
      />
    </LAModal>
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  overflow-y: auto;
}
table {
  display: inline-block;
  height: 100%;
}
.header {
  position: sticky;
  top: 0;
}
</style>
