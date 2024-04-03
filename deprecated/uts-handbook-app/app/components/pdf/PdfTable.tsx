// need to refactor

import React from "react";
import { View, StyleSheet } from "@react-pdf/renderer";
import PdfTableRow from "./PdfTableRow";

const styles = StyleSheet.create({
  tableContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
  },
});

const PdfTable = ({ data }: any) => (
  <View style={styles.tableContainer}>
    {/*<TableHeader />*/}
    <PdfTableRow items={data.items} />
    {/*<TableFooter items={data.items} />*/}
  </View>
);

export default PdfTable;