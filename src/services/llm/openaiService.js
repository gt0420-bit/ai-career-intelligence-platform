import OpenAI from 'openai';

export class OpenAIService {
  constructor() {
    const apiKey = process.env.REACT_APP_OPENAI_API_KEY;
    const isProduction = process.env.NODE_ENV === 'production';
    const isGitHubPages = !apiKey || window.location.hostname.includes('github.io');
    
    if (apiKey && !isGitHubPages) {
      // Use real OpenAI in development/local with API key
      this.openai = new OpenAI({
        apiKey: apiKey,
        dangerouslyAllowBrowser: true
      });
      this.useMockData = false;
      console.log('🤖 OpenAI service initialized with real API');
    } else {
      // Use mock data for GitHub Pages or when no API key
      this.useMockData = true;
      console.log('🎭 Using mock data for deployment');
    }
  }

  async generateResponse(message, userProfile, marketData) {
    if (this.useMockData) {
      return this.getMockResponse(message, userProfile);
    }

    try {
      const response = await this.openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "system",
            content: `You are a Career Intelligence Companion. You help professionals make data-driven career decisions using real market insights. Current user: ${userProfile.name}, Role: ${userProfile.role}. Market data shows: ${marketData.jobCount || 'loading'} jobs available.`
          },
          {
            role: "user",
            content: message
          }
        ],
        max_tokens: 200,
        temperature: 0.7
      });

      return response.choices[0].message.content;
    } catch (error) {
      console.error('OpenAI API error:', error);
      return this.getMockResponse(message, userProfile);
    }
  }

  getMockResponse(message, userProfile) {
    const responses = [
      `Hi ${userProfile?.name || 'there'}! I've analyzed the current job market and found excellent opportunities in your field. The demand for ${userProfile?.role || 'your skills'} is particularly strong right now.`,
      
      `Based on my analysis of recent market data, professionals with your background are seeing strong salary growth. Would you like me to break down the specific opportunities I'm seeing?`,
      
      `Great question! The market intelligence shows positive trends for your career path. I'm seeing increased hiring activity and competitive compensation packages in your area.`,
      
      `I've processed the latest job market data, and your profile aligns well with current industry demands. The Career Intelligence system indicates several high-potential career paths for you.`,
      
      `Excellent timing for this question! Recent market analysis shows your skill set is in high demand. I can provide specific insights about salary ranges, growth opportunities, and optimal career moves.`
    ];
    
    return responses[Math.floor(Math.random() * responses.length)];
  }
}
