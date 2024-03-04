import Footer from "../components/navigation/Footer";
import Header from "../components/navigation/Header";

const SubjectsLayout = ({ children }: { children: React.ReactNode }) => {

  return (
    <>
      <Header />

      <main>{children}</main>

      <Footer />
    </>
  );
};

export default SubjectsLayout;
