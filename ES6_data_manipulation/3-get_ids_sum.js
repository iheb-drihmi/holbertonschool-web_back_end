export default function getStudentIdsSum(students) {
    const id = students.map((student) => student.id);
    const sum = id.reduce((a, c) => a + c, 0);
    return sum;
  }
