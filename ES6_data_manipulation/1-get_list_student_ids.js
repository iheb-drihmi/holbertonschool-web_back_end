export default function getListStudentIds(objArray) {
    let idArray = [];
    if (Array.isArray(objArray) === false) {
      return idArray;
    }
    idArray = objArray.map((student) => student.id);
    return idArray;
  }