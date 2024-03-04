export default function getHeaderId(headerText: string | string[]) {
  return encodeURIComponent(
    (Array.isArray(headerText) ? headerText.join("-") : headerText)
      .toLowerCase()
      .replaceAll(" ", "-")
      .replaceAll("(", "")
      .replaceAll(")", "")
  );
}
