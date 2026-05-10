import 'package:flutter/material.dart';
import '../models/research_data.dart';

class DataListItem extends StatelessWidget {
  final ResearchData data;

  const DataListItem({Key? key, required this.data}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(data.title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Text('${data.researcher} • ${data.createdAt.toLocal().toShortDateString()}'),
        trailing: const Icon(Icons.chevron_right),
        onTap: () {
          // Navigate to detail screen if needed
        },
      ),
    );
  }
}

extension DateTimeExtension on DateTime {
  String toShortDateString() => '${this.year}-${this.month.toString().padLeft(2, '0')}-${this.day.toString().padLeft(2, '0')}';
}
