import { OpenAIService } from './openaiService';

export class ChatService {
  constructor() {
    this.openaiService = new OpenAIService();
  }

  async generateResponse(userMessage, userProfile, marketData) {
    try {
      return await this.openaiService.generateResponse(userMessage, userProfile, marketData);
    } catch (error) {
      console.error('Chat error:', error);
      return this.getFallbackResponse(userMessage, marketData);
    }
  }

  getFallbackResponse(userMessage, marketData) {
    if (userMessage.toLowerCase().includes('job')) {
      return `I found ${marketData.jobCount || 0} job opportunities that match your profile. The top positions show strong compatibility with your skills.`;
    }
    if (userMessage.toLowerCase().includes('salary')) {
      return `Based on market data, your role typically earns $${marketData.salaryData?.current?.toLocaleString() || '95,000'} with strong growth potential.`;
    }
    return "I'm here to help with your career development. Ask me about jobs, skills, or salary insights!";
  }
}
