export class MigrationService {
  async getCompanyMigrationTrends(companyName) {
    const migrationPatterns = {
      'Capital One': {
        totalExits: 1247,
        timeframe: '6 months',
        destinations: [
          { company: 'Amazon', count: 156, percentage: 12.5, avgSalaryIncrease: 18.3, popularRoles: ['Software Engineer', 'Data Scientist', 'Product Manager'] },
          { company: 'Microsoft', count: 134, percentage: 10.7, avgSalaryIncrease: 22.1, popularRoles: ['Cloud Engineer', 'Software Engineer', 'Principal Engineer'] },
          { company: 'Google', count: 128, percentage: 10.3, avgSalaryIncrease: 28.5, popularRoles: ['Software Engineer', 'Data Scientist', 'Technical Lead'] },
          { company: 'Meta', count: 98, percentage: 7.9, avgSalaryIncrease: 31.2, popularRoles: ['Software Engineer', 'Data Engineer', 'Research Scientist'] },
          { company: 'Apple', count: 87, percentage: 7.0, avgSalaryIncrease: 25.8, popularRoles: ['iOS Engineer', 'Software Engineer', 'Hardware Engineer'] },
          { company: 'JPMorgan Chase', count: 82, percentage: 6.6, avgSalaryIncrease: 15.4, popularRoles: ['Software Engineer', 'Vice President', 'Quantitative Analyst'] },
          { company: 'Goldman Sachs', count: 76, percentage: 6.1, avgSalaryIncrease: 28.9, popularRoles: ['Software Engineer', 'Quantitative Developer', 'Vice President'] },
          { company: 'Stripe', count: 65, percentage: 5.2, avgSalaryIncrease: 35.7, popularRoles: ['Software Engineer', 'Payment Systems Engineer', 'Product Manager'] }
        ],
        exitingSkills: [
          { skill: 'AWS', demand: 89, trend: 'Hot', migrationBoost: 25.3 },
          { skill: 'Python', demand: 85, trend: 'Growing', migrationBoost: 18.7 },
          { skill: 'Machine Learning', demand: 82, trend: 'Hot', migrationBoost: 32.1 },
          { skill: 'Kubernetes', demand: 78, trend: 'Growing', migrationBoost: 28.4 },
          { skill: 'React', demand: 75, trend: 'Stable', migrationBoost: 15.2 },
          { skill: 'Microservices', demand: 73, trend: 'Growing', migrationBoost: 22.8 }
        ],
        reasons: [
          { reason: 'Higher Compensation', percentage: 34.2 },
          { reason: 'Better Growth Opportunities', percentage: 28.7 },
          { reason: 'Tech Stack Modernization', percentage: 18.9 },
          { reason: 'Remote Work Flexibility', percentage: 12.4 },
          { reason: 'Company Culture', percentage: 5.8 }
        ]
      },
      'Goldman Sachs': {
        totalExits: 892,
        timeframe: '6 months',
        destinations: [
          { company: 'Citadel', count: 87, percentage: 9.8, avgSalaryIncrease: 42.3, popularRoles: ['Quantitative Developer', 'Software Engineer', 'Quantitative Researcher'] },
          { company: 'Two Sigma', count: 76, percentage: 8.5, avgSalaryIncrease: 38.9, popularRoles: ['Quantitative Developer', 'Data Scientist', 'Software Engineer'] },
          { company: 'Jane Street', count: 68, percentage: 7.6, avgSalaryIncrease: 45.2, popularRoles: ['Software Developer', 'Quantitative Trader', 'Software Engineer'] },
          { company: 'Google', count: 84, percentage: 9.4, avgSalaryIncrease: 28.7, popularRoles: ['Software Engineer', 'Quantitative Analyst', 'Product Manager'] },
          { company: 'Meta', count: 67, percentage: 7.5, avgSalaryIncrease: 31.8, popularRoles: ['Software Engineer', 'Data Scientist', 'Quantitative Researcher'] }
        ],
        exitingSkills: [
          { skill: 'Python', demand: 92, trend: 'Hot', migrationBoost: 28.9 },
          { skill: 'C++', demand: 78, trend: 'Stable', migrationBoost: 35.4 },
          { skill: 'Machine Learning', demand: 86, trend: 'Hot', migrationBoost: 42.1 },
          { skill: 'Quantitative Analysis', demand: 71, trend: 'Growing', migrationBoost: 38.7 }
        ]
      },
      'Microsoft': {
        totalExits: 1456,
        timeframe: '6 months',
        destinations: [
          { company: 'Google', count: 198, percentage: 13.6, avgSalaryIncrease: 15.2, popularRoles: ['Software Engineer', 'Principal Engineer', 'Technical Lead'] },
          { company: 'Amazon', count: 187, percentage: 12.8, avgSalaryIncrease: 8.9, popularRoles: ['Software Engineer', 'Principal Engineer', 'Product Manager'] },
          { company: 'Meta', count: 156, percentage: 10.7, avgSalaryIncrease: 18.7, popularRoles: ['Software Engineer', 'Research Scientist', 'Product Manager'] },
          { company: 'Apple', count: 134, percentage: 9.2, avgSalaryIncrease: 12.4, popularRoles: ['Software Engineer', 'Hardware Engineer', 'Product Manager'] },
          { company: 'OpenAI', count: 89, percentage: 6.1, avgSalaryIncrease: 45.8, popularRoles: ['Research Scientist', 'Software Engineer', 'ML Engineer'] }
        ],
        exitingSkills: [
          { skill: 'Azure', demand: 88, trend: 'Hot', migrationBoost: 22.4 },
          { skill: 'C#', demand: 72, trend: 'Stable', migrationBoost: 18.9 },
          { skill: 'Kubernetes', demand: 81, trend: 'Growing', migrationBoost: 28.5 }
        ]
      }
    };

    return migrationPatterns[companyName] || {
      totalExits: 450,
      timeframe: '6 months',
      destinations: [
        { company: 'Google', count: 45, percentage: 10.0, avgSalaryIncrease: 20.0, popularRoles: ['Software Engineer'] }
      ],
      exitingSkills: [
        { skill: 'Python', demand: 85, trend: 'Growing', migrationBoost: 20.0 }
      ]
    };
  }
}
