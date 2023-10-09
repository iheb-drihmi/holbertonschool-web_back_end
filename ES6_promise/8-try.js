export default function divideFunction(numerator, denominator) {
    if (denominator === 0) {
      throw new Error('cannot divide by 0');
    }
  
    try {
      return (numerator / denominator);
    } catch (e) {
      console.error(e);
      return 0;
    }
  }
