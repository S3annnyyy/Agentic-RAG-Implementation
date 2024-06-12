import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { slideInFromTop } from '../utils/motion';
import { motion } from 'framer-motion'
import { FaBurger } from 'react-icons/fa6';

const Home: React.FC = () => {

    const [dishName, setDishName] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      console.log(dishName)
      if (dishName.replace(/\s/g,'') === "") {
        alert("Input cannot be empty, please try again~😊")
        setDishName("")
      } else {
        navigate(`/response?dishName=${dishName}`);
      }
    }

  return (
    <motion.div 
      variants={slideInFromTop}
      initial="hidden" 
      animate="visible" 
      className="flex flex-col items-center justify-center px-6 py-8 mx-auto h-screen w-screen content-center"
    >    
      <h1 className="text-7xl font-bold  text-center align-middle">ChefGPT</h1>
      <p className="text-lg mb-8 text-center">Type any dish you want and get the recipe</p>
      
      <form className='w-3/5' onSubmit={handleSubmit}>   
          <label htmlFor="search" className="mb-2 text-sm font-medium text-gray-900 sr-only">Search</label>
          <div className="relative">
              <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                  <FaBurger />
              </div>
              <input 
                type="search" 
                id="search" 
                className="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Enter your dish here"
                value={dishName} 
                onChange={(e) => setDishName(e.target.value)}
                required 
              />
              <button type="submit" className="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2">Search</button>
          </div>
      </form>
    
    </motion.div>
  );
};

export default Home;
