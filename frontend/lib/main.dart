import 'package:flutter/material.dart';
import 'package:research_data_app/screens/research_data_list_screen.dart';

void main() {
  runApp(const ResearchDataApp());
}

class ResearchDataApp extends StatelessWidget {
  const ResearchDataApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Research Data App',
      theme: ThemeData(
        primarySwatch: Colors.indigo,
      ),
      home: const ResearchDataListScreen(),
    );
  }
}
