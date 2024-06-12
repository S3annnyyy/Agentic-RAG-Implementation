import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Home from '../pages/Home'
import GPTResponse from '../pages/GPTResponse';

export const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      { path: "", element: <Home /> },    
      { path: "/response", element: <GPTResponse />} 
    ],
  },
]);