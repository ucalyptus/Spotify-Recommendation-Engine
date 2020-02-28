import 'package:flutter/material.dart';
import 'package:spotify_mockup/modal_class/artist.dart';
import 'package:spotify_mockup/widgets/vertical_artist.dart';

class LibraryTab extends StatelessWidget {
  final List<Artist> following = [
    Artist(
        imageSrc: "assets/hailee.jpg",
        title: 'Hailee Steinfeld',
        circular: true),
    Artist(
        imageSrc: "assets/stoney.jpg",
        title: 'Stoney(deluxe)',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_queen.jpg",
        title: 'This is Queen',
        circular: false),
    Artist(
        imageSrc: "assets/pink_floyd.jpg", title: 'Pink Floyd', circular: true),
    Artist(
        imageSrc: "assets/queen_best_of.jpg",
        title: 'Queen : Best of',
        circular: false),
    Artist(
        imageSrc: "assets/this_is_post_malone.jpg",
        title: 'This is Post Malone',
        circular: false),
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
              child: SizedBox(
                  width: 100,
                  height: 100,
                  child: Icon(
                    Icons.library_music,
                    color: Colors.white,
                    size: 75,
                  )),
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
              child: SizedBox(
                  width: 100,
                  height: 100,
                  child: Icon(
                    Icons.album,
                    color: Colors.white,
                    size: 75,
                  )),
              color: Theme.of(context).accentColor,
            ),
          ]),
        ));
  }
}
