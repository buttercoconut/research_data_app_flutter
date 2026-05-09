import 'package:flutter/material.dart';
import '../models/research_data.dart';
import '../widgets/research_data_item.dart';

class ResearchDataListScreen extends StatefulWidget {
  const ResearchDataListScreen({Key? key}) : super(key: key);

  @override
  State<ResearchDataListScreen> createState() => _ResearchDataListScreenState();
}

class _ResearchDataListScreenState extends State<ResearchDataListScreen> {
  late Future<List<ResearchData>> _futureData;

  @override
  void initState() {
    super.initState();
    _futureData = Future.value([]); // placeholder, will be replaced by provider
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Research Data'),
      ),
      body: FutureBuilder<List<ResearchData>>(
        future: _futureData,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text('No research data found.'));
          }
          final data = snapshot.data!;
          return ListView.builder(
            itemCount: data.length,
            itemBuilder: (context, index) {
              return ResearchDataItem(data: data[index]);
            },
          );
        },
      ),
    );
  }
}
