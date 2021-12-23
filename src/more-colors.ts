import dict from "../res/dict.json";

export default function (colorName: string) {
  return dict[colorName.trim().toLowerCase() as keyof typeof dict];
}
