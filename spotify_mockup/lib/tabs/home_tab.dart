import 'package:flutter/material.dart';
import 'package:spotify_mockup/modal_class/artist.dart';
import 'package:spotify_mockup/widgets/horizontal_artist.dart';

class HomeTab extends StatefulWidget {
  final VoidCallback onPressed;
  HomeTab({this.onPressed});
  @override
  HomeTabState createState() {
    return new HomeTabState();
  }
}

class HomeTabState extends State<HomeTab> {
  bool isShown = true;
  bool isPlaying = false;
  final List<Artist> recentlyPlayed = [
    Artist(
        imageSrc: "assets/favourite.jpg",
        title: 'Favourite Songs',
        circular: false),
    Artist(imageSrc: "assets/slander.png", title: 'Slander', circular: true),
    Artist(
        imageSrc: "assets/this_is_illenium.png",
        title: 'This is Illenium',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_post_malone.jpg",
        title: 'This is Post Malone',
        circular: false),
  ];

  final List<Artist> heavyRotation = [
    Artist(
        imageSrc: "assets/arijit.png", title: 'Arijit Singh', circular: true),
    Artist(
        imageSrc: "assets/this_is_alan_walker.png",
        title: 'This is Alan Walker',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_queen.jpg",
        title: 'This is Queen',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_illenium.png",
        title: 'This is Illenium',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_post_malone.jpg",
        title: 'This is Post Malone',
        circular: false),
  ];

  final List<Artist> madeForYou = [
    Artist(imageSrc: "assets/dm1.png", title: 'Daily Mix 1', circular: false),
    Artist(imageSrc: "assets/dm2.png", title: 'Daily Mix 2', circular: false),
  ];
  void handleTap() {
    print('tap registered');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: NestedScrollView(
        headerSliverBuilder: (BuildContext context, bool innerBoxIsScrolled) {
          return <Widget>[
            SliverAppBar(
              backgroundColor: Theme.of(context).accentColor,
              floating: false,
              pinned: false,
            ),
          ];
        },
        body: Container(
          color: Theme.of(context).accentColor,
          child: Padding(
            padding: const EdgeInsets.only(top: 8.0),
            child: SingleChildScrollView(
              child: Column(
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0, left: 16),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        Text('Recently played',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 24,
                                fontWeight: FontWeight.bold))
                      ],
                    ),
                  ),
                  SizedBox(
                    child: HArtistList(
                      artists: recentlyPlayed,
                      onPressed: widget.onPressed,
                    ),
                    height: MediaQuery.of(context).size.height / 4 + 20,
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0, left: 16.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        Text('Your heavy rotation',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 24,
                                fontWeight: FontWeight.bold))
                      ],
                    ),
                  ),
                  SizedBox(
                    child: HArtistList(
                      artists: heavyRotation,
                      onPressed: widget.onPressed,
                    ),
                    height: MediaQuery.of(context).size.height / 4 + 20,
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0, left: 16.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        Text('Made for you',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 24,
                                fontWeight: FontWeight.bold))
                      ],
                    ),
                  ),
                  SizedBox(
                    child: HArtistList(
                      artists: madeForYou,
                      onPressed: widget.onPressed,
                    ),
                    height: MediaQuery.of(context).size.height / 4 + 20,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
