// need to refactor

import React, { Fragment } from "react";
import { Text, View, StyleSheet } from "@react-pdf/renderer";

const styles = StyleSheet.create({
  row: {
    flexDirection: "row",
    alignItems: "center",
  },
});

const PdfTableRow = ({ items }: any) => {
  const keys = Object.keys(items);

  const rows = items.map((item: any, index: number) => {
    return (
      <View style={styles.row} key={index}>
        {keys.map((key: string, index: number) => (
          <Text key={index}>{item[key]}</Text>
        ))}
      </View>
    );
  });
  return <Fragment>{rows}</Fragment>;
};

export default PdfTableRow;
