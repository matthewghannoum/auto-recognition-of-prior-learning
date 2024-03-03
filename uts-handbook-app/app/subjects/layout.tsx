import Link from "next/link";
import Footer from "../components/Footer";
import Image from "next/image";
import Header from "../components/Header";

const SubjectsLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <>
      <Header />

      <main>
        <div className="w-full">
          <div className="min-h-[65vh] p-16">
            <div className="mx-auto max-w-screen-lg">{children}</div>
          </div>
        </div>
      </main>

      <Footer />
    </>
  );
};

export default SubjectsLayout;
