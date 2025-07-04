import React from 'react';
import { TrendingUp, Briefcase, Target, BookOpen, ArrowRightLeft } from 'lucide-react';

const TabButton = ({ id, label, icon: Icon, active, onClick }) => (
  <button
    onClick={() => onClick(id)}
    className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
      active 
        ? 'bg-blue-600 text-white shadow-md' 
        : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
    }`}
  >
    <Icon size={20} />
    <span className="hidden sm:inline">{label}</span>
  </button>
);

const Navigation = ({ activeTab, setActiveTab }) => {
  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: TrendingUp },
    { id: 'jobs', label: 'Job Matches', icon: Briefcase },
    { id: 'skills', label: 'Skill Analysis', icon: Target },
    { id: 'migration', label: 'Migration Trends', icon: ArrowRightLeft },
    { id: 'learning', label: 'Learning Paths', icon: BookOpen }
  ];

  return (
    <div className="flex gap-2 overflow-x-auto pb-2">
      {tabs.map(tab => (
        <TabButton 
          key={tab.id}
          id={tab.id} 
          label={tab.label} 
          icon={tab.icon} 
          active={activeTab === tab.id} 
          onClick={setActiveTab} 
        />
      ))}
    </div>
  );
};

export default Navigation;
