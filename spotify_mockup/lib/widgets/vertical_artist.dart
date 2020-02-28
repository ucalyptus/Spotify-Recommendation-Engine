import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:spotify_mockup/modal_class/artist.dart';

class VArtistList extends StatefulWidget {
  final List<Artist> artists;
  final VoidCallback onPressed;
  VArtistList({this.artists, this.onPressed});

  @override
  VArtistListState createState() {
    return new VArtistListState();
  }
}

class VArtistListState extends State<VArtistList> {
  Widget stories() {
    return Expanded(
      child: ListView.builder(
          scrollDirection: Axis.vertical,
          itemCount: widget.artists.length,
          itemBuilder: (context, index) => InkWell(
                // onTap: (){
                //   Navigator.push(context, MaterialPageRoute(
                //     builder: (context) => SongPlayer()
                //   ));
                // },
                onTap: widget.onPressed,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: <Widget>[
                    Container(
                      margin: EdgeInsets.all(8.0),
                      width: 80.0,
                      height: 80.0,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        image: DecorationImage(
                          fit: BoxFit.fill,
                          image: AssetImage(widget.artists[index].imageSrc),
                        ),
                      ),
                    ),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: <Widget>[
                        Padding(
                          padding: const EdgeInsets.only(top: 8.0, left: 8.0),
                          child: Text(
                            widget.artists[index].title,
                            style: TextStyle(
                                fontSize: 16,
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
      margin: EdgeInsets.all(8.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: <Widget>[stories()],
      ),
    );
  }
}
