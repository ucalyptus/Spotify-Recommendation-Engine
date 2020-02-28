import 'package:flutter/material.dart';
import 'package:spotify_mockup/screens/home.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Spotify Clone',
      theme: ThemeData(
        primaryColor: Color(0xff222326),
        accentColor: Color(0xff121212),
      ),
//      darkTheme: ThemeData.dark(),
//      theme: ThemeData.light(),
//      themeMode: ThemeMode.system,
      home: HomePage(),
    );
  }
}
