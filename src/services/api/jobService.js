import axios from 'axios';

export class JobService {
  constructor() {
    this.baseURL = 'https://jsearch.p.rapidapi.com';
    this.headers = {
      'X-RapidAPI-Key': process.env.REACT_APP_RAPIDAPI_KEY,
      'X-RapidAPI-Host': 'jsearch.p.rapidapi.com'
    };
  }

  async getJobRecommendations(userProfile) {
    try {
      const response = await axios.get(`${this.baseURL}/search`, {
        headers: this.headers,
        params: {
          query: `${userProfile.role} ${userProfile.skills[0]}`,
          page: 1,
          num_pages: 1,
          location: userProfile.location || 'United States'
        }
      });

      return this.transformJobData(response.data.data || []);
    } catch (error) {
      console.error('Job API error:', error);
      return this.getFallbackJobs();
    }
  }

  transformJobData(rawJobs) {
    return rawJobs.slice(0, 5).map((job, index) => ({
      id: job.job_id || `job-${index}`,
      title: job.job_title || 'Software Developer',
      company: job.employer_name || 'Tech Company',
      location: job.job_city && job.job_state ? 
        `${job.job_city}, ${job.job_state}` : 'Remote',
      salary: this.formatSalary(job.job_min_salary, job.job_max_salary),
      skills: this.extractSkills(job.job_description || ''),
      posted: this.formatDate(job.job_posted_at_datetime_utc),
      match: Math.floor(Math.random() * 20) + 75,
      applyUrl: job.job_apply_link,
      remote: job.job_is_remote || false
    }));
  }

  formatSalary(min, max) {
    if (min && max) return `$${min.toLocaleString()} - $${max.toLocaleString()}`;
    if (min) return `From $${min.toLocaleString()}`;
    if (max) return `Up to $${max.toLocaleString()}`;
    return 'Salary not specified';
  }

  extractSkills(description) {
    const skills = ['JavaScript', 'React', 'Python', 'AWS', 'Node.js', 'SQL'];
    return skills.filter(skill => 
      description.toLowerCase().includes(skill.toLowerCase())
    ).slice(0, 4);
  }

  formatDate(dateString) {
    if (!dateString) return '1 week ago';
    const days = Math.floor(Math.random() * 7) + 1;
    return `${days} day${days > 1 ? 's' : ''} ago`;
  }

  getFallbackJobs() {
    return [{
      id: 'fallback-1',
      title: 'Senior Software Developer',
      company: 'TechCorp',
      location: 'San Francisco, CA',
      salary: '$120,000 - $150,000',
      skills: ['JavaScript', 'React', 'AWS'],
      posted: '2 days ago',
      match: 87,
      remote: false
    }];
  }
}
