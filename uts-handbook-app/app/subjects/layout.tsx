import Link from "next/link";
import Footer from "../components/navigation/Footer";
import Image from "next/image";
import Header from "../components/navigation/Header";

const SubjectsLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <>
      <Header />

      <main>
        {children}
      </main>

      <Footer />
    </>
  );
};

export default SubjectsLayout;
