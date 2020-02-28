import 'package:flutter/material.dart';

class SongPlayer extends StatefulWidget {
  final VoidCallback onPressed;
  SongPlayer({this.onPressed});
  @override
  SongPlayerState createState() {
    return new SongPlayerState();
  }
}

class SongPlayerState extends State<SongPlayer>
    with SingleTickerProviderStateMixin {
  AnimationController controller;
  Animation<double> animation;
  bool isPlaying = false;
  var _value = 0.0;
  @override
  void initState() {
    super.initState();
  }

  void startTimer() {
    controller = AnimationController(
        duration: const Duration(seconds: 120), vsync: this);
    animation = Tween(begin: 0.0, end: 1.0).animate(controller)
      ..addListener(() {
        setState(() {
          // the state that has changed here is the animation object’s value
        });
      });
    controller.repeat();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: BoxDecoration(
          shape: BoxShape.rectangle,
          image: DecorationImage(
            fit: BoxFit.cover,
            image: AssetImage('assets/bohemian.jpg'),
          ),
        ),
        child: Container(
          child: Column(
            children: <Widget>[
              AppBar(
                backgroundColor: Colors.transparent,
                title: Text('Playing'),
                centerTitle: true,
                leading: IconButton(
                  icon: Icon(Icons.keyboard_arrow_down),
                  onPressed: widget.onPressed,
                ),
                actions: <Widget>[
                  IconButton(
                    icon: Icon(Icons.more_vert),
                    onPressed: () {},
                  )
                ],
              ),
              Expanded(
                child: Container(),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  'Bohemian Rhapsody - Remastered',
                  style: TextStyle(color: Colors.white, fontSize: 20),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  'Queen',
                  style: TextStyle(color: Colors.grey, fontSize: 18),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Slider(
                  //value: animation == null ? 0 : animation.value,
                  value: _value,
                  onChanged: (value) {
                    //print(value);
                    setState(() {
                      _value = value;
                    });
                  },
                  activeColor: Colors.white,
                  inactiveColor: Colors.grey,

                  // valueColor: AlwaysStoppedAnimation(Color(0xff828A8A)),
                  // backgroundColor: Color(0xff666666),
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: <Widget>[
                    IconButton(
                      iconSize: 30,
                      icon: Icon(Icons.favorite_border, color: Colors.white),
                      onPressed: () {},
                    ),
                    IconButton(
                      iconSize: 30,
                      icon: Icon(Icons.skip_previous, color: Colors.white),
                      onPressed: () {},
                    ),
                    IconButton(
                      iconSize: 50,
                      icon: Icon(
                          isPlaying
                              ? Icons.pause_circle_filled
                              : Icons.play_circle_filled,
                          color: Colors.white),
                      onPressed: () {
                        setState(() {
                          if (isPlaying) {
                            isPlaying = false;
                          } else {
                            isPlaying = true;
                          }
                        });
                      },
                    ),
                    IconButton(
                      iconSize: 30,
                      icon: Icon(Icons.skip_next, color: Colors.white),
                      onPressed: () {},
                    ),
                    IconButton(
                      iconSize: 30,
                      icon: Icon(Icons.clear, color: Colors.white),
                      onPressed: () {},
                    ),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
