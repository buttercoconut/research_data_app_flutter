import 'package:flutter/material.dart';
import '../models/research_data.dart';

class ResearchDataItem extends StatelessWidget {
  final ResearchData data;

  const ResearchDataItem({Key? key, required this.data}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(data.title),
        subtitle: Text(data.description),
        trailing: Text(
          '${data.date.year}-${data.date.month.toString().padLeft(2, '0')}-${data.date.day.toString().padLeft(2, '0')}',
          style: const TextStyle(fontSize: 12, color: Colors.grey),
        ),
      ),
    );
  }
}
