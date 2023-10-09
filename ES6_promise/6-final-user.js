import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handlePromise(p) {
  return p.then((status) => ({ status: 'fulfilled', value: status }))
    .catch((e) => ({ status: 'rejected', value: `Error: ${e.message}` }));
}

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);

  const promises = [promise1, promise2].map(handlePromise);

  return Promise.all(promises);
}
