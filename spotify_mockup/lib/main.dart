import 'package:flutter/material.dart';
import 'home.dart';
import 'search.dart';
import 'library.dart';
import 'settings.dart';
import 'package:spotify/spotify_io.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: true,
      title: 'Spotify_mockup_main',
      theme: ThemeData.dark(),
      home: MyHomePage(title: 'Home'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

Widget show(int index) {
  switch (index) {
    case 0:
      return Home();
      break;
    case 1:
      return SearchScreen();
      break;
    case 2:
      return Library();
      break;
    case 3:
      return Settings();
      break;
  }
}

class _MyHomePageState extends State<MyHomePage> {
  int index = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: show(index),
      bottomNavigationBar: Theme(
        data: Theme.of(context).copyWith(
          canvasColor: Colors.grey[900],
        ),
        child: BottomNavigationBar(
            type: BottomNavigationBarType.fixed,
            currentIndex: index,
            showUnselectedLabels: true,
            unselectedItemColor: Colors.white54,
            selectedItemColor: Colors.white,
            onTap: ((int x) {
              setState(() {
                index = x;
                show(index);
              });
            }),
            items: [
              new BottomNavigationBarItem(
                icon: Icon(Icons.home),
                title: Text('Home'),
              ),
              new BottomNavigationBarItem(
                icon: Icon(Icons.search),
                title: Text('Search'),
              ),
              new BottomNavigationBarItem(
                icon: Icon(Icons.library_music),
                title: Text('Your Library'),
              ),
              new BottomNavigationBarItem(
                icon: Icon(Icons.settings),
                title: Text('Settings'),
              ),
            ]),
      ),
    );
  }
}
