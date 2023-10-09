function signUpUser(firstNam, lastNam) {
    return new Promise((resolve) => {
      resolve({ firstName: firstNam, lastName: lastNam });
    });
  }
  export default signUpUser;
