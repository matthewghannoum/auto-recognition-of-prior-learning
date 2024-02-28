import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "UTS Handbook",
  description:
    "The authoritative source of information on approved courses and subjects at UTS",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
