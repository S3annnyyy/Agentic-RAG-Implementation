import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { waveform } from 'ldrs';
waveform.register();

const useQuery = () => {
  return new URLSearchParams(useLocation().search);
};

const GPTResponse: React.FC = () => {
  const query = useQuery();
  const dishName = query.get('dishName');
  const navigate = useNavigate();
  
  const [isLoading, setIsLoading] = useState(true);
  const [recipe, setRecipe] = useState<{ dish: string, ingredients: string[], instructions: { step: number, description: string }[] } | null>(null);

  useEffect(() => {
    if (!dishName) {
      navigate('/');
    } else {
      fetchRecipe(dishName);
    }
  }, []);

  const fetchRecipe = async (dishName: string) => {
    try {
      const response = await fetch('http://localhost:8000/v1/gpt/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ dish: dishName })
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data)
        setRecipe(data.data.response);
      } else {
        console.error('Failed to fetch the recipe');
      }
    } catch (error) {
      console.error('Error:', error);
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
          <div>
            <h1 className="text-3xl font-bold mb-4">Recipe for {recipe.dish}</h1>
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
