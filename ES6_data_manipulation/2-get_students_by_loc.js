export default function getStudentsByLocation(studentList, cityStr) {
    return studentList.filter((student) => student.location === cityStr);
  }
