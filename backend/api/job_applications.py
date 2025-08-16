from flask import Blueprint, request, jsonify
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.job_application_service import JobApplicationService
from services.google_sheets_service import create_sheets_service
from models import ApplicationStatus

# Create blueprint
job_apps_bp = Blueprint('job_applications', __name__, url_prefix='/api/job-applications')

# Initialize services
sheets_service = create_sheets_service()
job_service = JobApplicationService(sheets_service)

@job_apps_bp.route('/', methods=['GET'])
def get_applications():
    """Get all job applications for user with optional filters"""
    try:
        # For now, using user_id = 1 (you can add authentication later)
        user_id = 1
        
        # Get filters from query parameters
        filters = {}
        if request.args.get('status'):
            filters['status'] = ApplicationStatus(request.args.get('status'))
        if request.args.get('company'):
            filters['company_name'] = request.args.get('company')
        if request.args.get('position'):
            filters['position'] = request.args.get('position')
        
        applications = job_service.get_applications(user_id, filters)
        
        return jsonify({
            "success": True,
            "applications": applications,
            "total": len(applications)
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/', methods=['POST'])
def create_application():
    """Create a new job application"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error": "No data provided"
            }), 400
        
        # Validate required fields
        required_fields = ['position_title', 'company']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    "success": False,
                    "error": f"Field '{field}' is required"
                }), 400
        
        # For now, using user_id = 1
        user_id = 1
        
        result = job_service.create_application(user_id, data)
        
        if result["success"]:
            return jsonify(result), 201
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/<int:application_id>', methods=['GET'])
def get_application(application_id):
    """Get specific job application"""
    try:
        user_id = 1  # For now
        
        application = job_service.get_application(application_id, user_id)
        
        if application:
            return jsonify({
                "success": True,
                "application": application
            })
        else:
            return jsonify({
                "success": False,
                "error": "Application not found"
            }), 404
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    """Update job application"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error": "No data provided"
            }), 400
        
        result = job_service.update_application(application_id, data)
        
        if result["success"]:
            return jsonify(result)
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    """Delete job application"""
    try:
        user_id = 1  # For now
        
        result = job_service.delete_application(application_id, user_id)
        
        if result["success"]:
            return jsonify(result)
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/stats', methods=['GET'])
def get_application_stats():
    """Get application statistics"""
    try:
        user_id = 1  # For now
        
        stats = job_service.get_application_stats(user_id)
        
        return jsonify({
            "success": True,
            "stats": stats
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/sync-sheets', methods=['POST'])
def sync_to_sheets():
    """Sync all applications to Google Sheets"""
    try:
        user_id = 1  # For now
        
        # Get spreadsheet ID from request
        data = request.get_json() or {}
        spreadsheet_id = data.get('spreadsheet_id')
        
        if not spreadsheet_id:
            return jsonify({
                "success": False,
                "error": "spreadsheet_id is required"
            }), 400
        
        # Setup spreadsheet if sheets service is available
        if sheets_service:
            if not sheets_service.setup_spreadsheet(spreadsheet_id):
                return jsonify({
                    "success": False,
                    "error": "Failed to setup spreadsheet"
                }), 400
        
        result = job_service.sync_all_to_sheets(user_id)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/setup-sheets', methods=['POST'])
def setup_sheets():
    """Setup Google Sheets integration"""
    try:
        data = request.get_json()
        spreadsheet_id = data.get('spreadsheet_id')
        
        if not spreadsheet_id:
            return jsonify({
                "success": False,
                "error": "spreadsheet_id is required"
            }), 400
        
        if not sheets_service:
            return jsonify({
                "success": False,
                "error": "Google Sheets service not available. Check credentials."
            }), 400
        
        success = sheets_service.setup_spreadsheet(spreadsheet_id)
        
        if success:
            return jsonify({
                "success": True,
                "message": "Google Sheets setup successful"
            })
        else:
            return jsonify({
                "success": False,
                "error": "Failed to setup Google Sheets"
            }), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

# Status options endpoint for UI
@job_apps_bp.route('/status-options', methods=['GET'])
def get_status_options():
    """Get available application status options"""
    status_options = [
        {"value": status.value, "label": status.value.replace('_', ' ').title()}
        for status in ApplicationStatus
    ]
    
    return jsonify({
        "success": True,
        "status_options": status_options
    })

@job_apps_bp.route('/sync-gmail', methods=['POST'])
def sync_from_gmail():
    """Sync job applications from Gmail"""
    try:
        data = request.get_json() or {}
        days_back = data.get('days_back', 7)
        user_id = 1  # For now
        
        # Import the email integration service
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        from services.email_job_integration import EmailJobIntegration
        
        integration = EmailJobIntegration()
        
        # Setup Gmail authentication
        if not integration.setup_gmail_sync():
            return jsonify({
                "success": False,
                "error": "Gmail authentication failed. Please check credentials."
            }), 400
        
        # Sync applications
        results = integration.sync_gmail_applications(days_back, user_id)
        
        return jsonify({
            "success": True,
            "message": f"Gmail sync completed",
            "results": {
                "created": results['success'],
                "skipped": results['skipped'], 
                "failed": results['failed'],
                "applications": results['applications']
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/<int:application_id>/emails', methods=['POST'])
def add_follow_up_email(application_id):
    """Add a follow-up email to an application and categorize it"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "error": "No data provided"
            }), 400
        
        email_content = data.get('email_content', '')
        sender = data.get('sender', '')
        subject = data.get('subject', '')
        
        if not email_content:
            return jsonify({
                "success": False,
                "error": "email_content is required"
            }), 400
        
        # Categorize the email
        from services.email_categorizer import EmailCategorizer
        categorizer = EmailCategorizer()
        
        email_type = categorizer.categorize_email(email_content, subject)
        
        result = job_service.add_follow_up_email(
            application_id, 
            email_content, 
            sender, 
            subject, 
            email_type
        )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/deduplicate', methods=['POST'])
def deduplicate_applications():
    """Remove duplicate applications"""
    try:
        # Import the deduplication service
        from services.deduplication_service import DeduplicationService
        
        dedup_service = DeduplicationService()
        result = dedup_service.remove_duplicates()
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/rejection-stats', methods=['GET'])
def get_rejection_stats():
    """Get statistics about rejection emails"""
    try:
        user_id = 1  # For now
        
        stats = job_service.get_rejection_stats(user_id)
        
        return jsonify({
            "success": True,
            "stats": stats
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@job_apps_bp.route('/resync-cleaned-sheets', methods=['POST'])
def resync_cleaned_to_sheets():
    """Resync cleaned applications to Google Sheets after deduplication"""
    try:
        user_id = 1  # For now
        
        result = job_service.resync_cleaned_data_to_sheets(user_id)
        
        if result.get("success"):
            return jsonify(result)
        else:
            return jsonify(result), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500