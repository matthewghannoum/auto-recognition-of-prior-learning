import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header>
      <div className="w-full">
        <div className="relative h-[95px] flex w-full items-center justify-start bg-black">
          <Link className="absolute left-0 top-0" href="/">
            <Image alt="UTS logo" src="/uts-logo.png" width="95" height="95" />
          </Link>

          <div className="w-full">
            <h1 className="text-center text-3xl font-bold text-white">
              University of Technology Sydney Handbook
            </h1>
          </div>
        </div>
      </div>
    </header>
  );
}
