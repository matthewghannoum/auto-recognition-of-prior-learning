import { RplSubjectPair } from "@/app/types";
import { Document, Page, Text, View } from "@react-pdf/renderer";

export default function RplPdf({
  formData,
  selectedSubjects,
}: {
  formData: {
    studentNumber: string;
    email: string;
    sName: string;
    fName: string;
    courseCode: string;
    courseName: string;
    prevInstitutionName: string;
    prevCourseName: string;
  };
  selectedSubjects: RplSubjectPair[];
}) {
  const {
    studentNumber,
    email,
    sName,
    fName,
    courseCode,
    courseName,
    prevInstitutionName,
    prevCourseName,
  } = formData;

  return (
    <Document>
      <Page size="A4" style={{ width: "100%" }}>
        <View>
          <Text>
            First Name: {fName} | Family Name: {sName}
          </Text>
        </View>

        <View>
          <Text>UTS Student Number: {studentNumber}</Text>
          <Text>Email: {email}</Text>
        </View>

        <View>
          <Text>UTS Course Code: {courseCode}</Text>
          <Text>UTS Course Name: {courseName}</Text>
        </View>

        <View>
          <Text>Previous Study, Institution and Award Details</Text>
          <Text>Name of Institution: {prevInstitutionName}</Text>
          <Text>Course Name: {prevCourseName}</Text>
        </View>

        <View style={{ width: "100%" }}>
          <View style={{ width: "100%" }}>
            <Text>{"UTS Subject(s)"}</Text>
          </View>

          <View
            style={{
              width: "100%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              gap: "0",
            }}
          >
            <Text style={{ width: "33%", border: "2px solid black" }}>Student Number</Text>
            <Text style={{ width: "33%", border: "2px solid black" }}>Student Name</Text>
            <Text style={{ width: "33%", border: "2px solid black" }}>Credits</Text>
          </View>
        </View>
      </Page>
    </Document>
  );
}
