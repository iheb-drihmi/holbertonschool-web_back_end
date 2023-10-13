export default function cleanSet(set, startString) {
    const result = [];
    if (startString === '' || startString === null || typeof startString !== 'string') {
      return '';
    }
  
    for (const string of set) {
      if (string !== undefined && string.startsWith(startString)) {
        const restOfString = string.slice(3);
        result.push(restOfString);
      }
    }
  
    return result.join('-');
  }
