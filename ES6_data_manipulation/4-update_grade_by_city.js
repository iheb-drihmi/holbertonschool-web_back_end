export default function updateStudentGradeByCity(studentList, city, newGrades) {
    const oneCityStudentList = studentList.filter((student) => student.location === city);
  
    const studentWithGrade = oneCityStudentList.map((student) => {
      const matchingGrade = newGrades.find((grade) => (grade.studentId === student.id));
      return {
        ...student,
        grade: matchingGrade ? matchingGrade.grade : 'N/A',
      };
    });
  
    return studentWithGrade;
  }
