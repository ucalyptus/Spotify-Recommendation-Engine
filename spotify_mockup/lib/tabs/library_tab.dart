import 'package:flutter/material.dart';
import 'package:spotify_mockup/modal_class/artist.dart';
import 'package:spotify_mockup/widgets/vertical_artist.dart';

class LibraryTab extends StatelessWidget {
  final List<Artist> playlists = [
    Artist(
        imageSrc: "assets/placeholder_add.png",
        title: 'Create playlist',
        circular: true),
    Artist(
        imageSrc: "assets/favourite.jpg",
        title: 'Liked Songs',
        circular: false),
  ];

  final List<Artist> following = [
    Artist(
        imageSrc: "assets/arijit.png", title: 'Arijit Singh', circular: true),
    Artist(
        imageSrc: "assets/this_is_alan_walker.png",
        title: 'This is Alan Walker',
        circular: true),
    Artist(
        imageSrc: "assets/this_is_queen.jpg",
        title: 'This is Queen',
        circular: true),
    Artist(imageSrc: "assets/slander.png", title: 'Slander', circular: true),
    Artist(
        imageSrc: "assets/this_is_illenium.png",
        title: 'This is Illenium',
        circular: true),
    Artist(
        imageSrc: "assets/this_is_post_malone.jpg",
        title: 'This is Post Malone',
        circular: true),
  ];
  @override
  Widget build(BuildContext context) {
    return Container(
        color: Theme.of(context).accentColor,
        child: Padding(
          padding: const EdgeInsets.only(top: 0),
          child: tabBarControllerHome(context),
        ));
  }

  Widget tabBarControllerHome(BuildContext context) {
    return DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: AppBar(
            bottom: TabBar(
              isScrollable: false,
              tabs: [
                Tab(
                  text: "Playlists",
                ),
                Tab(
                  text: "Artists",
                ),
                Tab(
                  text: "Albums",
                ),
              ],
              labelColor: Colors.white,
              unselectedLabelColor: Colors.grey,
              indicatorSize: (TabBarIndicatorSize.label),
              indicatorColor: Colors.green,
            ),
          ),
          body: TabBarView(children: [
            Container(
              child: SingleChildScrollView(
                child: Stack(
                  children: <Widget>[
                    SizedBox(
                      child: VArtistList(
                        artists: playlists,
                        onPressed: () {},
                      ),
                      height: MediaQuery.of(context).size.height,
                    ),
                  ],
                ),
              ),
              color: Theme.of(context).accentColor,
            ),
            Container(
              child: SingleChildScrollView(
                child: Stack(
                  children: <Widget>[
                    SizedBox(
                      child: VArtistList(
                        artists: following,
                        onPressed: () {},
                      ),
                      height: MediaQuery.of(context).size.height,
                    ),
                  ],
                ),
              ),
              color: Theme.of(context).accentColor,
            ),
            Container(
              color: Theme.of(context).accentColor,
              child: Center(
                child: Text('Your albums will appear here',
                    style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 24)),
              ),
            ),
          ]),
        ));
  }
}
