import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:spotify_clone_gssoc/home/home.dart';

class login extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _stateLogin();


}

class _stateLogin extends State<login>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      body:Container(
          decoration: BoxDecoration(color: Colors.black),
          child:
            Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisSize: MainAxisSize.min,
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                Expanded(
                  child:Container(
                    decoration: BoxDecoration(color: Colors.black),
                    child: Center(
                      child: Image(image: AssetImage('assets/spotify.png'),width: 200,height: 200,),
                    ),
                  ),
                ),
                Expanded(
                  child:Center(
                  child: SizedBox(
                    child: RaisedButton(shape:RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),onPressed: () {
                      Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => home()));
                    },
                    color:Colors.lightGreen,
                    child:Container(margin: EdgeInsets.all(10),child: Text('Get Started', style: TextStyle(color:Colors.white, fontWeight: FontWeight.bold, fontSize: 24)),)),
                  ),
                  )
                )
              ],
            )
        )
      
    );
  }


}