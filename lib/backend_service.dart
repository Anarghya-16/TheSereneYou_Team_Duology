import 'dart:convert';
import 'package:http/http.dart' as http;

Future<Map<String, dynamic>> callBackend(String userInput) async {
  final url = Uri.parse('http://172.16.34.115:5000'); // replace port if needed

  final response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'user_input': userInput}),
  );

  if (response.statusCode == 200) {
    return jsonDecode(response.body);
  } else {
    throw Exception('Backend error: ${response.statusCode}');
  }
}