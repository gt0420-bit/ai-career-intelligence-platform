import React, { useState, useEffect } from 'react';
import { TrendingUp, ArrowRight, Users, DollarSign, Search } from 'lucide-react';
import { MigrationService } from '../../services/api/migrationService';

const MigrationAnalytics = () => {
  const [selectedCompany, setSelectedCompany] = useState('Capital One');
  const [migrationData, setMigrationData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [migrationService] = useState(() => new MigrationService());

  const popularCompanies = [
    'Capital One', 'Goldman Sachs', 'Microsoft', 'Google', 'Meta', 
    'Amazon', 'Apple', 'Netflix', 'Stripe', 'JPMorgan Chase'
  ];

  useEffect(() => {
    loadMigrationData();
  }, [selectedCompany]);

  const loadMigrationData = async () => {
    setLoading(true);
    try {
      const data = await migrationService.getCompanyMigrationTrends(selectedCompany);
      setMigrationData(data);
    } catch (error) {
      console.error('Migration data error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6 text-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
        <p className="mt-2 text-gray-600">Loading migration trends...</p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Company Talent Migration Trends</h2>
        <p className="text-gray-600 mb-4">
          See where professionals are moving from their current companies and discover migration patterns.
        </p>
        
        <div className="flex items-center gap-3">
          <Search size={20} className="text-gray-400" />
          <select
            value={selectedCompany}
            onChange={(e) => setSelectedCompany(e.target.value)}
            className="px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {popularCompanies.map(company => (
              <option key={company} value={company}>{company}</option>
            ))}
          </select>
          <span className="text-gray-600">talent migration trends</span>
        </div>
      </div>

      {migrationData && (
        <>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center gap-3">
                <Users className="text-blue-600" size={24} />
                <div>
                  <p className="text-gray-600 text-sm">Total Exits</p>
                  <p className="text-2xl font-bold">{migrationData.totalExits.toLocaleString()}</p>
                  <p className="text-sm text-gray-500">in {migrationData.timeframe}</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center gap-3">
                <TrendingUp className="text-green-600" size={24} />
                <div>
                  <p className="text-gray-600 text-sm">Top Destination</p>
                  <p className="text-xl font-bold">{migrationData.destinations[0]?.company}</p>
                  <p className="text-sm text-gray-500">{migrationData.destinations[0]?.count} people</p>
                </div>
              </div>
            </div>
            
            <div className="bg-white rounded-lg shadow-md p-6">
              <div className="flex items-center gap-3">
                <DollarSign className="text-yellow-600" size={24} />
                <div>
                  <p className="text-gray-600 text-sm">Avg Salary Boost</p>
                  <p className="text-xl font-bold text-green-600">
                    +{migrationData.destinations[0]?.avgSalaryIncrease}%
                  </p>
                  <p className="text-sm text-gray-500">at top destination</p>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">
              Where {selectedCompany} Talent is Going
            </h3>
            <div className="space-y-3">
              {migrationData.destinations.slice(0, 8).map((dest, index) => (
                <div key={dest.company} className="flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors">
                  <div className="flex items-center gap-4">
                    <div className="bg-blue-100 text-blue-800 rounded-full w-8 h-8 flex items-center justify-center font-bold text-sm">
                      {index + 1}
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-bold text-gray-800">{selectedCompany}</span>
                        <ArrowRight size={16} className="text-gray-400" />
                        <span className="font-bold text-blue-600">{dest.company}</span>
                      </div>
                      <div className="flex items-center gap-4 text-sm text-gray-600 mt-1">
                        <span>{dest.count} people ({dest.percentage}%)</span>
                        <span className="text-green-600 font-medium">+{dest.avgSalaryIncrease}% salary</span>
                      </div>
                    </div>
                  </div>
                  <div className="text-right">
                    <div className="text-sm text-gray-500 mb-1">Popular roles:</div>
                    <div className="flex flex-wrap gap-1">
                      {dest.popularRoles.slice(0, 2).map(role => (
                        <span key={role} className="px-2 py-1 bg-blue-100 text-blue-700 rounded text-xs">
                          {role}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4">
              Skills Driving {selectedCompany} Exits
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {migrationData.exitingSkills.map(skill => (
                <div key={skill.skill} className="p-4 border rounded-lg">
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-bold text-gray-800">{skill.skill}</span>
                    <span className={`px-2 py-1 rounded text-xs font-medium ${
                      skill.trend === 'Hot' ? 'bg-red-100 text-red-700' :
                      skill.trend === 'Growing' ? 'bg-green-100 text-green-700' :
                      'bg-gray-100 text-gray-700'
                    }`}>
                      {skill.trend}
                    </span>
                  </div>
                  <div className="text-sm text-gray-600">
                    <div>Market demand: <span className="font-medium">{skill.demand}%</span></div>
                    <div className="text-green-600 font-medium">
                      Migration salary boost: +{skill.migrationBoost}%
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {migrationData.reasons && (
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-4">
                Why People Leave {selectedCompany}
              </h3>
              <div className="space-y-3">
                {migrationData.reasons.map(reason => (
                  <div key={reason.reason} className="flex items-center justify-between">
                    <span className="text-gray-700">{reason.reason}</span>
                    <div className="flex items-center gap-3">
                      <div className="w-32 bg-gray-200 rounded-full h-2">
                        <div 
                          className="bg-blue-600 h-2 rounded-full" 
                          style={{ width: `${reason.percentage}%` }}
                        />
                      </div>
                      <span className="text-sm font-medium w-12">{reason.percentage}%</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </>
      )}
    </div>
  );
};

export default MigrationAnalytics;
