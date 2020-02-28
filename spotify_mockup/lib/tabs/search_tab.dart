import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SearchTab extends StatelessWidget {
  final List<String> topGenres = ['Bollywood', 'Gaming', 'Hip-Hop', 'Metal'];
  final List<String> browseAll = [
    'Podcasts',
    'New Releases',
    'Charts',
    'Mood',
    'Workout',
    'Decades',
    'Country',
    'Focus'
  ];
  final List<Color> colors = [
    Color(0xffF19821),
    Color(0xff99BACB),
    Color(0xff498D7C),
    Color(0xff4E97F2),
    Color(0xffEFB958),
    Color(0xffB196C4),
    Color(0xffF49824),
    Color(0xffF95F35),
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: NestedScrollView(
        headerSliverBuilder: (BuildContext context, bool innerBoxIsScrolled) {
          return <Widget>[
            SliverAppBar(
              expandedHeight: MediaQuery.of(context).size.height / 5,
              floating: false,
              pinned: false,
              flexibleSpace: FlexibleSpaceBar(
                  centerTitle: true,
                  title: Text("Search",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 30.0,
                      )),
                  background: Container(
                    decoration: new BoxDecoration(
                      gradient: new LinearGradient(
                        colors: [
                          Colors.blueGrey,
                          Theme.of(context).primaryColor,
                          Theme.of(context).accentColor,
                        ],
                        begin: FractionalOffset.topLeft,
                        end: FractionalOffset.bottomRight,
                      ),
                    ),
                  )),
            ),
          ];
        },
        body: Container(
          color: Theme.of(context).accentColor,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: <Widget>[
                Row(
                  children: <Widget>[
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Container(
                          height: MediaQuery.of(context).size.height / 18,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(8),
                            color: Colors.white,
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: <Widget>[
                              Padding(
                                padding:
                                    EdgeInsets.fromLTRB(8.0, 0.0, 8.0, 0.0),
                                child: Icon(
                                  Icons.search,
                                  color: Colors.grey,
                                ),
                              ),
                              Text('Artists, songs or podcasts',
                                  style: TextStyle(
                                      color: Colors.black,
                                      fontSize: 16.0,
                                      fontWeight: FontWeight.bold))
                            ],
                          ),
                        ),
                      ),
                    ),
                    IconButton(
                      icon: Icon(
                        Icons.mic,
                        color: Colors.white,
                      ),
                      onPressed: () {},
                    )
                  ],
                ),
                Expanded(
                  child: SingleChildScrollView(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.only(left: 8.0, top: 8.0),
                          child: Text(
                            'Your top genres',
                            style: TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                                fontSize: 16),
                          ),
                        ),
                        GridView.count(
                          shrinkWrap: true,
                          physics: BouncingScrollPhysics(),
                          crossAxisCount: 2,
                          childAspectRatio:
                              (MediaQuery.of(context).size.width / (250)),
                          children: List.generate(4, (index) {
                            return Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Container(
                                  width: MediaQuery.of(context).size.width / 2,
                                  decoration: BoxDecoration(
                                      borderRadius: BorderRadius.circular(8),
                                      shape: BoxShape.rectangle,
                                      color: colors[index]
                                      // gradient: new LinearGradient(
                                      //   colors: [
                                      //     Colors.blueAccent,
                                      //     Colors.red,
                                      //   ],
                                      //   begin: FractionalOffset.topLeft,
                                      //   end: FractionalOffset.bottomRight,
                                      // ),
                                      ),
                                  child: Padding(
                                    padding:
                                        const EdgeInsets.fromLTRB(8, 16, 0, 0),
                                    child: Text(
                                      topGenres[index],
                                      style: TextStyle(
                                          color: Colors.white,
                                          fontSize: 18,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  )),
                            );
                          }),
                        ),
                        Padding(
                          padding: const EdgeInsets.only(left: 8.0, top: 8.0),
                          child: Text(
                            'Browse all',
                            style: TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                                fontSize: 16),
                          ),
                        ),
                        GridView.count(
                          shrinkWrap: true,
                          physics: BouncingScrollPhysics(),
                          crossAxisCount: 2,
                          childAspectRatio:
                              (MediaQuery.of(context).size.width / 250),
                          children: List.generate(browseAll.length, (index) {
                            return Padding(
                              padding: const EdgeInsets.all(8.0),
                              child: Container(
                                  width: MediaQuery.of(context).size.width / 2,
                                  decoration: BoxDecoration(
                                      borderRadius: BorderRadius.circular(8),
                                      shape: BoxShape.rectangle,
                                      color: colors[index]
                                      // gradient: new LinearGradient(
                                      //   colors: [
                                      //     Colors.blueAccent,
                                      //     Colors.red,
                                      //   ],
                                      //   begin: FractionalOffset.topLeft,
                                      //   end: FractionalOffset.bottomRight,
                                      // ),
                                      ),
                                  child: Padding(
                                    padding:
                                        const EdgeInsets.fromLTRB(8, 16, 0, 0),
                                    child: Text(
                                      browseAll[index],
                                      style: TextStyle(
                                          color: Colors.white,
                                          fontSize: 18,
                                          fontWeight: FontWeight.bold),
                                    ),
                                  )),
                            );
                          }),
                        ),
                      ],
                    ),
                  ),
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
