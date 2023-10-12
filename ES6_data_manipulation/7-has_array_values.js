export default function hasValuesFromArray(set, array) {
    const result = array.map((num) => set.has(num));
    return !result.includes(false);
  }