import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/research_data.dart';

class ApiService {
  final String baseUrl = 'https://api.example.com';

  Future<List<ResearchData>> fetchResearchData() async {
    final response = await http.get(Uri.parse('$baseUrl/research-data'));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((e) => ResearchData.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load research data');
    }
  }
}
