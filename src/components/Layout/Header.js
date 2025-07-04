import React from 'react';
import { User, Brain } from 'lucide-react';

const Header = ({ userProfile }) => {
  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-7xl mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-blue-600 text-white p-2 rounded-lg">
              <Brain size={24} />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gray-800">Career Intelligence</h1>
              <p className="text-sm text-gray-600">AI-Powered Career Development</p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <div className="text-right">
              <p className="font-medium text-gray-800">{userProfile.name}</p>
              <p className="text-sm text-gray-600">{userProfile.role}</p>
            </div>
            <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
              <User size={20} className="text-blue-600" />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
