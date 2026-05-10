import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'screens/home_screen.dart';
import 'services/api_service.dart';

void main() {
  runApp(const ResearchDataApp());
}

class ResearchDataApp extends StatelessWidget {
  const ResearchDataApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider<ApiService>(create: (_) => ApiService()),
      ],
      child: MaterialApp(
        title: 'Research Data App',
        theme: ThemeData(
          primarySwatch: Colors.indigo,
        ),
        home: const HomeScreen(),
        debugShowCheckedModeBanner: false,
      ),
    );
  }
}
