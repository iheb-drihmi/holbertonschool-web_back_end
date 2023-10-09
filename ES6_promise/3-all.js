import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const promiseA = uploadPhoto();
  const promiseB = createUser();
  return Promise.all([promiseA, promiseB])
    .then((data) => {
      console.log(`${data[0].body} ${data[1].firstName} ${data[1].lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
