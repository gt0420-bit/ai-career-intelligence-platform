export class SkillService {
  async analyzeSkillGaps(userSkills, targetRole) {
    const marketData = {
      'AWS': { demand: 85, growth: 22, avgSalaryBoost: 15000, priority: 'High' },
      'Docker': { demand: 78, growth: 18, avgSalaryBoost: 12000, priority: 'High' },
      'Kubernetes': { demand: 72, growth: 25, avgSalaryBoost: 18000, priority: 'High' },
      'TypeScript': { demand: 75, growth: 20, avgSalaryBoost: 8000, priority: 'Medium' },
      'GraphQL': { demand: 65, growth: 15, avgSalaryBoost: 7000, priority: 'Medium' }
    };

    const gaps = [];
    Object.entries(marketData).forEach(([skill, data]) => {
      if (!userSkills.includes(skill)) {
        gaps.push({ skill, ...data });
      }
    });

    return gaps.sort((a, b) => b.demand - a.demand);
  }
}
