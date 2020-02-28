import 'package:flutter/material.dart';
import 'package:spotify_mockup/modal_class/artist.dart';

class ArtistList extends StatefulWidget {
  final List<Artist> artists;
  final VoidCallback onPressed;
  ArtistList({this.artists, this.onPressed});

  @override
  ArtistListState createState() {
    return new ArtistListState();
  }
}

class ArtistListState extends State<ArtistList> {
  Widget stories() {
    return Expanded(
      child: ListView.builder(
          scrollDirection: Axis.horizontal,
          itemCount: widget.artists.length,
          itemBuilder: (context, index) => InkWell(
                // onTap: (){
                //   Navigator.push(context, MaterialPageRoute(
                //     builder: (context) => SongPlayer()
                //   ));
                // },
                onTap: widget.onPressed,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Container(
                      margin: EdgeInsets.symmetric(horizontal: 8.0),
                      width: 150.0,
                      height: 150.0,
                      decoration: BoxDecoration(
                        shape: widget.artists[index].circular
                            ? BoxShape.circle
                            : BoxShape.rectangle,
                        image: DecorationImage(
                          fit: BoxFit.fill,
                          image: AssetImage(widget.artists[index].imageSrc),
                        ),
                      ),
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.only(top: 8.0, left: 8.0),
                          child: Text(
                            widget.artists[index].title,
                            style: TextStyle(
                                fontSize: 14,
                                color: Colors.white,
                                fontWeight: FontWeight.bold),
                          ),
                        )
                      ],
                    )
                  ],
                ),
              )),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(top: 8.0, left: 8.0, right: 8.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: <Widget>[stories()],
      ),
    );
  }
}
