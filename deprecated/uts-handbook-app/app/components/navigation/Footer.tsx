import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-black w-full flex flex-col items-center justify-center gap-2 p-16">
      <div className="w-full flex items-center justify-center gap-4 pb-4">
        <Link
          className="text-white hover:text-gray"
          href="https://www.uts.edu.au/about"
        >
          About UTS
        </Link>

        <Link
          className="text-white hover:text-gray"
          href="https://www.lib.uts.edu.au/"
        >
          Library
        </Link>

        <Link
          className="text-white hover:text-gray"
          href="https://www.uts.edu.au/news"
        >
          Newsroom
        </Link>

        <Link
          className="text-white hover:text-gray"
          href="https://www.uts.edu.au/staff"
        >
          Staff
        </Link>

        <Link
          className="text-white hover:text-gray"
          href="https://www.uts.edu.au/about/contacts/uts-contacts"
        >
          Contact us
        </Link>
      </div>

      <p className="text-white text-center text-sm">
        © Copyright UTS - CRICOS Provider No: 00099F - TEQSA Provider ID:
        PRV12060 - TEQSA Category:
      </p>

      <p className="text-white text-center text-sm">
        Australian University - ABN: 77 257 686 961 - 25 February 2024 12:50 PM
      </p>

      <p className="text-white text-center text-sm">
        The page is authorised by Director, Institute for Interactive Media and
        Learning Send comments to UAPO
      </p>
    </footer>
  );
}
