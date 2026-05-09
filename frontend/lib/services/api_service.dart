import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/research_data.dart';

class ApiService {
  static const String _baseUrl = 'http://localhost:8000/api';

  Future<List<ResearchData>> fetchResearchData() async {
    final response = await http.get(Uri.parse('$_baseUrl/research-data'));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body) as List<dynamic>;
      return data.map((e) => ResearchData.fromJson(e as Map<String, dynamic>)).toList();
    } else {
      throw Exception('Failed to load research data');
    }
  }
}
