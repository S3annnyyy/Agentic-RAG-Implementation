import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const useQuery = () => {
  return new URLSearchParams(useLocation().search);
};

const GPTResponse: React.FC = () => {
  const query = useQuery();
  const dishName = query.get('dishName');
  const navigate = useNavigate();

  useEffect(() => {
    if (!dishName) {
      navigate('/');
    }
  }, [dishName, navigate]);

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Recipe for {dishName}</h1>
      {/* Add your recipe fetching and display logic here */}
    </div>
  );
};

export default GPTResponse;
