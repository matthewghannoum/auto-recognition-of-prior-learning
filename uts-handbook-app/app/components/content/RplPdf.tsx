import { Document, Page, Text, View } from "@react-pdf/renderer";

export default function RplPdf(formData: {
  studentNumber: string;
  email: string;
  sName: string;
  fName: string;
  courseCode: string;
  courseName: string;
  prevInstitutionName: string;
  prevCourseName: string;
}) {
  return (
    <Document>
      <Page size="A4">
        <View>
          <Text>
            First Name: {formData.fName} | Family Name: {formData.sName}
          </Text>
        </View>

        <View>
          <Text>UTS Student Number: {formData.studentNumber}</Text>
          <Text>Email: {formData.email}</Text>
        </View>

        <View>
          <Text>UTS Course Code: {formData.courseCode}</Text>
          <Text>UTS Course Name: {formData.courseName}</Text>
        </View>

        <View>
          <Text>Previous Study, Institution and Award Details</Text>
          <Text>Name of Institution: {formData.prevInstitutionName}</Text>
          <Text>Course Name: {formData.prevCourseName}</Text>
        </View>
      </Page>
    </Document>
  );
}
