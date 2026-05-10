import 'package:json_annotation/json_annotation.dart';

part 'research_data.g.dart';

@JsonSerializable()
class ResearchData {
  final String id;
  final String title;
  final String description;
  final DateTime createdAt;
  final String researcher;

  ResearchData({
    required this.id,
    required this.title,
    required this.description,
    required this.createdAt,
    required this.researcher,
  });

  factory ResearchData.fromJson(Map<String, dynamic> json) =>
      _$ResearchDataFromJson(json);

  Map<String, dynamic> toJson() => _$ResearchDataToJson(this);
}
