import axios from 'axios'

const IS_PRODUCTION = process.env.NODE_ENV === 'production';
const API_URL = IS_PRODUCTION ? '/api/' : 'http://localhost:5000/api/';

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 100000,
  headers: {'Content-Type': 'application/json'}
});


// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error);
  return Promise.reject(error)
});


export default {

  'post': $axios.post,
  'get': $axios.get,
  'domain': IS_PRODUCTION ? '' : 'http://localhost:5000'
}
