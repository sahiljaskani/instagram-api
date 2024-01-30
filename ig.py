import requests

access_token = 'IGQWROWk5IUDBFVGhIQ1JFNkZASSVRqajd6M0ZA3ZAVctaFNGWFJPOGZAhMUNJN0ZApNXV5VVpnOUlpX1JiQUN0SzNuVjJoWkVQaHBOczRxU25JcXdTeXJDakVlZA0ZAIRWg3ZAEdSLUwtZA2drbG96ckJZAUHFZAeGVLYmluMm8ZD' 
user_id = '7158133747610422'  

url = f'https://graph.instagram.com/7158133747610422?fields=id,username&access_token=IGQWROWk5IUDBFVGhIQ1JFNkZASSVRqajd6M0ZA3ZAVctaFNGWFJPOGZAhMUNJN0ZApNXV5VVpnOUlpX1JiQUN0SzNuVjJoWkVQaHBOczRxU25JcXdTeXJDakVlZA0ZAIRWg3ZAEdSLUwtZA2drbG96ckJZAUHFZAeGVLYmluMm8ZD'

response = requests.get(url)
data = response.json()

print(data)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Fikk ikke hentet dataen:", response.status_code)

def get_user_profile_with_pagination(access_token):
    url = f'https://graph.instagram.com/me/media?fields=id,caption&access_token={access_token}&limit=10'
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

    # Implement pagination logic here


