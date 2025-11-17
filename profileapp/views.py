from django.shortcuts import render


def home(request):
    profile = {
        'name': 'Karan Tanwar',
        'title': 'DevOps Engineer | TechOps Engineer',
        'experience': '4+ years of experience in IT',
        'about': 'Passionate about Cloud, Automation, and CI/CD',
        'skills': ['Docker', 'Kubernetes', 'Terraform', 'Jenkins', 'GitHub Actions', 'AWS', 'Azure'],
        'certifications': ['Microsoft Certified: Azure Fundamentals (AZ-900)', 'Azure Administrator Associate (AZ-104)'],
    }
    return render(request, 'profile.html', {'profile': profile})
