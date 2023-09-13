export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    if (trueOrFalse) {
      const newtask = false;
      const newtask2 = true;
      return [newtask, newtask2];
    }
  
    return [task, task2];
  }
