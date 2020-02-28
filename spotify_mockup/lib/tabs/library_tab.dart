import 'package:flutter/material.dart';

class LibraryTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
        color: Theme.of(context).accentColor,
        child: Padding(
          padding: const EdgeInsets.only(top: 24.0),
          child: tabBarControllerHome(context),
        ));
  }

  Widget tabBarControllerHome(BuildContext context) {
    return DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: PreferredSize(
            preferredSize: Size.fromHeight(56.0),
            child: Material(
              color: Theme.of(context).accentColor,
              child: TabBar(
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
              child: SizedBox(
                width: 100,
                height: 100,
                  child: Icon(
                Icons.person,
                color: Colors.white,
                size: 75,
              )),
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
