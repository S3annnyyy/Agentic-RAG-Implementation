import React, { useEffect, useState, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { waveform } from 'ldrs';
waveform.register();

type RecipeSchema = {
  dish: string;
  ingredients: string[];
  instructions: { step: number; description: string }[];
};

const useQuery = () => {
  return new URLSearchParams(useLocation().search);
};

const GPTResponse: React.FC = () => {
  
  const query = useQuery();
  const dishName = query.get('dishName');
  const navigate = useNavigate();
  const apiCalled = useRef<boolean>(false)  
  const [isLoading, setIsLoading] = useState(true);
  const [recipe, setRecipe] = useState<RecipeSchema | null>(null);

  useEffect(() => {
    if (!dishName) {
      navigate('/');
    } else if (apiCalled.current === false) {
      fetchRecipe(dishName);
      apiCalled.current = true;
    }
  }, [dishName, navigate]);

  const fetchRecipe = async (dishName: string) => {
    try {
      const response = await fetch('GPT_ENDPOINT', {
        // 1. Call GPT API endpoint asynchronously sing POST + headers configuration as Content-Type': 'application/json' + { dish: dishName } as body 
        // TODO
      });
      if (response.ok) {
        // 2. If response is ok, await for data and then setRecipe
        //TODO
      } else {
        console.error('Failed to fetch the recipe');
        alert("Failed to call API, please try again later")
        navigate('/');
      }
    } catch (error) {
      console.error('Error:', error);
      alert("Failed to call API, please try again later")
      navigate('/');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      {isLoading ? (
        <div className="flex justify-center items-center h-screen">
          <l-waveform size="50" bg-opacity="0.1" speed="1" color="#3266D3"></l-waveform>
        </div>
      ) : (
        recipe && (
          <div className='bg-white p-6 rounded-lg shadow-lg'>
            <h1 className="text-3xl font-bold mb-4 text-center">Recipe for {recipe.dish}</h1>
            <h2 className="text-2xl font-semibold mb-2">Ingredients:</h2>
            <ul className="mb-4">
              {recipe.ingredients.map((ingredient, index) => (
                <li key={index}>{ingredient}</li>
              ))}
            </ul>
            <h2 className="text-2xl font-semibold mb-2">Instructions:</h2>
            <ol>
              {recipe.instructions.map((instruction, index) => (
                <li key={index} className="mb-2">
                  <span className="font-bold">Step {instruction.step}: </span>
                  {instruction.description}
                </li>
              ))}
            </ol>
          </div>
        )
      )}
    </div>
  );
};

export default GPTResponse;
