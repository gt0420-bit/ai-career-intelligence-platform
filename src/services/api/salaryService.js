export class SalaryService {
  async getSalaryData(role, location, experience) {
    const baseSalaries = {
      'Software Developer': 85000,
      'Senior Software Developer': 125000,
      'Full Stack Developer': 95000
    };

    const locationMultipliers = {
      'San Francisco': 1.4,
      'New York': 1.3,
      'Seattle': 1.25,
      'Austin': 1.1
    };

    const base = baseSalaries[role] || 85000;
    const locationMult = this.getLocationMultiplier(location, locationMultipliers);
    const experienceMult = 1 + (experience * 0.08);
    
    const current = Math.round(base * locationMult * experienceMult);
    
    return {
      current,
      growth: 12,
      demand: 'High',
      marketPosition: current > 120000 ? 'Top 25%' : 'Above Average',
      percentiles: {
        50: current,
        75: Math.round(current * 1.15),
        90: Math.round(current * 1.3)
      }
    };
  }

  getLocationMultiplier(location, multipliers) {
    const key = Object.keys(multipliers).find(city => 
      location?.includes(city)
    );
    return multipliers[key] || 1.0;
  }
}
