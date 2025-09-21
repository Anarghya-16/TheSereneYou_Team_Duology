import 'package:flutter/material.dart';
import 'api_service.dart';

void main() {
  runApp(const SereneYouApp());
}

class SereneYouApp extends StatelessWidget {
  const SereneYouApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "The Serene You",
      theme: ThemeData(
        primaryColor: const Color(0xFF94C9D8),
        scaffoldBackgroundColor: const Color(0xFFF8FAFB),
        fontFamily: 'Sans',
        textTheme: const TextTheme(
          headlineLarge: TextStyle(fontSize: 28, fontWeight: FontWeight.w600, color: Colors.black87),
          bodyMedium: TextStyle(fontSize: 16, color: Colors.black54),
        ),
        useMaterial3: true,
      ),
      darkTheme: ThemeData.dark().copyWith(
        primaryColor: const Color(0xFF6EA4BF),
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String _response = "";

  final cards = [
    {"title": "Guided Meditation", "icon": Icons.self_improvement, "color": const Color(0xFFC9E4DE), "endpoint": "/meditation"},
    {"title": "Mood Tracking", "icon": Icons.emoji_emotions, "color": const Color(0xFFF5D5CB), "endpoint": "/mood"},
    {"title": "Dear Diary", "icon": Icons.book_rounded, "color": const Color(0xFFEFCFE3), "endpoint": "/diary"},
    {"title": "AI Companion", "icon": Icons.chat_bubble_rounded, "color": const Color(0xFFD8E2DC), "endpoint": "/greet"},
  ];

  void _onFeatureTap(String endpoint) async {
    setState(() {
      _response = "Loading...";
    });
    try {
      String res = "";
      final api = ApiService();
      switch (endpoint) {
        case '/meditation':
          res = await api.getMeditation();
          break;
        case '/mood':
          res = await api.getMoodTracking();
          break;
        case '/diary':
          res = await api.getDiary();
          break;
        case '/greet':
          res = await api.getGreeting();
          break;
        default:
          res = "Not implemented";
      }
      setState(() {
        _response = res;
      });
    } catch (e) {
      setState(() {
        _response = "Error: $e";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: _buildLeftDrawer(context),
      appBar: AppBar(
        elevation: 0, backgroundColor: Colors.transparent, foregroundColor: Colors.black87,
        title: const Text("The Serene You", style: TextStyle(fontWeight: FontWeight.w600)), centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text("Welcome back, dear friend 🌿", style: TextStyle(fontSize: 24, fontWeight: FontWeight.w500)),
            const SizedBox(height: 14),
            const Text("How can we support your wellness journey today?", style: TextStyle(fontSize: 16, color: Colors.black54)),
            const SizedBox(height: 30),
            Expanded(
              child: GridView.builder(
                itemCount: cards.length,
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, mainAxisSpacing: 20, crossAxisSpacing: 20, childAspectRatio: 1.1),
                itemBuilder: (context, index) {
                  final card = cards[index];
                  return GestureDetector(
                    onTap: () => _onFeatureTap(card["endpoint"] as String),
                    child: Container(
                      decoration: BoxDecoration(color: card["color"] as Color, borderRadius: BorderRadius.circular(20)),
                      child: Center(
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(card["icon"] as IconData, size: 50, color: Colors.black87),
                            const SizedBox(height: 12),
                            Text(card["title"] as String,
                                style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w500, color: Colors.black87)),
                          ],
                        ),
                      ),
                    ),
                  );
                },
              ),
            ),
            if (_response.isNotEmpty)
              Container(
                padding: const EdgeInsets.all(16),
                margin: const EdgeInsets.only(top: 16),
                decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: Colors.white),
                child: Text(_response, style: const TextStyle(fontSize: 16)),
              ),
          ],
        ),
      ),
    );
  }

  Drawer _buildLeftDrawer(BuildContext context) {
    return Drawer(
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.only(topRight: Radius.circular(30), bottomRight: Radius.circular(30)),
      ),
      child: Column(
        children: [
          const UserAccountsDrawerHeader(
            decoration: BoxDecoration(color: Color(0xFF94C9D8)),
            accountName: Text("Your Profile", style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
            accountEmail: Text("Feel calm. Feel supported."),
            currentAccountPicture: CircleAvatar(
              backgroundColor: Colors.white, child: Icon(Icons.person, size: 40, color: Colors.grey),
            ),
          ),
          ListTile(leading: const Icon(Icons.settings), title: const Text("Settings"), onTap: () {}),
          ListTile(leading: const Icon(Icons.info_outline), title: const Text("About"), onTap: () {}),
          const Spacer(),
          ListTile(leading: const Icon(Icons.logout), title: const Text("Log Out"), onTap: () {}),
        ],
      ),
    );
  }
}
