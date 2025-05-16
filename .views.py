from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from xml.etree.ElementTree import Element, tostring
from xml.dom import minidom

class TextToXMLAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "Текст не предоставлен"}, status=status.HTTP_400_BAD_REQUEST)

        root = Element("response")
        text_element = Element("text")
        text_element.text = text
        root.append(text_element)

        # Красивое форматирование
        rough_string = tostring(root, encoding="utf-8")
        reparsed = minidom.parseString(rough_string)
        xml_pretty = reparsed.toprettyxml(indent="  ")

        return Response(xml_pretty, content_type="application/xml")
