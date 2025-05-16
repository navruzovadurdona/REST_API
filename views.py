from django.http import HttpResponse, JsonResponse
import xml.etree.ElementTree as ET

def convert_to_xml(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)
        
        root = ET.Element("response")
        text_element = ET.SubElement(root, "text")
        text_element.text = text
        xml_data = ET.tostring(root, encoding='utf-8', method='xml')

        return HttpResponse(xml_data, content_type='application/xml')
    
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
