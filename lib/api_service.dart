import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = "http://172.16.34.115:5000"; // Replace with your backend IP and port

  Future<String> getMeditation() async {
    final url = Uri.parse('$baseUrl/meditation');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      return response.body;
    }
    throw Exception("Failed to load meditation data");
  }

  Future<String> getMoodTracking() async {
    final url = Uri.parse('$baseUrl/mood');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      return response.body;
    }
    throw Exception("Failed to load mood tracking data");
  }

  Future<String> getDiary() async {
    final url = Uri.parse('$baseUrl/diary');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      return response.body;
    }
    throw Exception("Failed to load diary data");
  }

  Future<String> getGreeting() async {
    final url = Uri.parse('$baseUrl/greet');
    final response = await http.get(url);
    if (response.statusCode == 200) {
      return response.body;
    }
    throw Exception("Failed to load greeting");
  }
}
