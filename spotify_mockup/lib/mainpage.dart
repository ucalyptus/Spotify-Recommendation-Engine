import 'package:flutter/material.dart';

class MainPage extends StatelessWidget {
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [
          Color.fromRGBO(40, 96, 65, 7.0),
          Color(0xFF191414),
        ], begin: Alignment.topLeft, end: FractionalOffset(0.3, 0.3)),
      ),
      child: ListView(
        children: <Widget>[
          SingleChildScrollView(
            scrollDirection: Axis.vertical,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: EdgeInsets.all(45.0),
                ),
                Container(
                  height: 250.0,
                  child: Column(
                    children: <Widget>[
                      Text(
                        'Recently Played',
                        style: TextStyle(
                            color: Colors.white.withOpacity(1.0),
                            fontSize: 23.0,
                            fontFamily: 'SpotifyFont',
                            fontWeight: FontWeight.bold),
                      ),
                      Padding(
                        padding: EdgeInsets.all(10.0),
                      ),
                      Container(
                        height: 165.0,
                        child: ListView.builder(
                          itemCount: 10,
                          scrollDirection: Axis.horizontal,
                          itemBuilder: (BuildContext context, int index) {
                            return Column(
                              children: <Widget>[
                                SizedBox(
                                  height: 130.0,
                                  width: 140.0,
                                  child: Image.asset(
                                    'assets/eminem.jpeg',
                                    fit: BoxFit.fitHeight,
                                  ),

                                ),
                                Padding(padding: EdgeInsets.all(5.0)),
                                Text('This Is Eminem',
                                style: TextStyle(
                                  color: Colors.white.withOpacity(1.0),
                                  fontFamily: 'SpotifyFont',
                                  fontSize: 10.0,
                                ),
                                )
                              ],
                            );
                          },
                        ),
                      ),
                    ],
                  ),
                ),

                Container(
                  height: 290.0,
                  child: Column(
                    children: <Widget>[
                      Text(
                        'Made for you',
                        style: TextStyle(
                            color: Colors.white.withOpacity(1.0),
                            fontSize: 23.0,
                            fontFamily: 'SpotifyFont',
                            fontWeight: FontWeight.bold),
                      ),
                      SizedBox(
                        height: 210.0,
                        width: 210.0,
                        child: Image.asset('assets/Selection_004.png',fit: BoxFit.fill,),
                      ),
                      Text('Songs you loved most this year,\nall wrapped up',
                      style: TextStyle(
                        color: Colors.white70,
                        fontSize: 12.5,
                        fontFamily: 'SpotifyFont'
                      ),
                        textAlign: TextAlign.center,
                      )
                    ],
                  ),
                ),
                Container(
                  height: 250.0,
                  child: Column(
                    children: <Widget>[
                      Text(
                        'Recommendation',
                        style: TextStyle(
                            color: Colors.white.withOpacity(1.0),
                            fontSize: 23.0,
                            fontFamily: 'SpotifyFont',
                            fontWeight: FontWeight.bold),
                      ),
                      Padding(
                        padding: EdgeInsets.all(10.0),
                      ),
                      Container(
                        height: 165.0,
                        child: ListView.builder(
                          itemCount: imageurl.length,
                          scrollDirection: Axis.horizontal,
                          itemBuilder: (BuildContext context, int index) {
                            return Column(
                              children: <Widget>[
                                SizedBox(
                                  height: 130.0,
                                  width: 140.0,
                                  child: Image.asset(
                                    imageurl[index],
                                    fit: BoxFit.fitHeight,
                                  ),

                                ),
                                Padding(padding: EdgeInsets.all(5.0)),
                                Text(txt[index],
                                  style: TextStyle(
                                    color: Colors.white.withOpacity(1.0),
                                    fontFamily: 'SpotifyFont',
                                    fontSize: 10.0,
                                  ),
                                )
                              ],
                            );
                          },
                        ),
                      ),
                    ],
                  ),
                ),

              ],
            ),
          ),
        ],
      ),
    );
  }
}
List<String> imageurl = [
  'assets/Billie.jpeg',
  'assets/download.jpeg',
  'assets/Billie.jpeg',
  'assets/download.jpeg',
  'assets/Billie.jpeg',
  'assets/download.jpeg',
  'assets/Billie.jpeg',
  'assets/download.jpeg',
];
List<String> txt = [
  'This Is Billie',
  "Today's top hits",
  'This Is Billie',
  "Today's top hits",
  'This Is Billie',
  "Today's top hits",
  'This Is Billie',
  "Today's top hits",
];