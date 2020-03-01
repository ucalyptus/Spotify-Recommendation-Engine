import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';


class home extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _stateHome();


}

class _stateHome extends State<home> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0.0,
        actions: <Widget>[RaisedButton(
          child: Icon(Icons.settings, color:Colors.white, size: 30,),
        )],
      ),
      bottomNavigationBar:
        Container(padding:EdgeInsets.all(10),color:Colors.black,child:Row(
           mainAxisAlignment: MainAxisAlignment.spaceAround
          ,
           mainAxisSize: MainAxisSize.max,

          children: <Widget>[
            Flexible(
              child:Column(
                  mainAxisSize: MainAxisSize.min,
                  children:[Icon(Icons.home, size:23, color:Colors.white),Text('Home', style: TextStyle(color:Colors.white),)]),
            ),
            Flexible(
              child:Column(
                  mainAxisSize: MainAxisSize.min,
                  children:[Icon(Icons.search, size:23, color:Colors.white),Text('Search', style: TextStyle(color:Colors.white),)]),
            ),
            Flexible(
              child:Column(
                  mainAxisSize: MainAxisSize.min,
                  children:[Icon(Icons.library_music, size:23, color:Colors.white),Text('Your library', style: TextStyle(color:Colors.white),)]),
            ),
            Flexible(
              child:Column(
                  mainAxisSize: MainAxisSize.min,
                  children:[Icon(Icons.perm_identity, size:23, color:Colors.white),Text('Your profile', style: TextStyle(color:Colors.white),)]),
            ),


          ],
        )),
      body: Container(
        color:Colors.black,
        child: ListView(
          children: <Widget>[
            Container(
              margin: EdgeInsets.all(10),
              child: Text('Recently Played', style: TextStyle(color:Colors.white, fontSize: 36, fontWeight: FontWeight.bold),),
            ),
            Container(height:200,child:ListView.builder(shrinkWrap: true, scrollDirection:Axis.horizontal, itemCount: 10,itemBuilder: (context, i) {

                return Container(margin:EdgeInsets.all(10),child:SizedBox(
                  width: 150,
                  height: 150,
                  child:Column(

                    children: <Widget>[
                     Container(color:Colors.white,child: Image(image: AssetImage('assets/jesus.png'),)),
                     Container(margin:EdgeInsets.only(top:5),alignment:Alignment.centerLeft,child:Text('JESUS IS KING', style: TextStyle(color:Colors.white, fontSize: 16, fontWeight: FontWeight.bold),))
                    ],

                  ),
                ));


              })),
            Container(
              margin: EdgeInsets.all(10),
              child: Text('Your Heavy Rotation', style: TextStyle(color:Colors.white, fontSize: 36, fontWeight: FontWeight.bold),),
            ),

            Container(height:200,child:ListView.builder(shrinkWrap: true, scrollDirection:Axis.horizontal, itemCount: 10,itemBuilder: (context, i) {

              return Container(margin:EdgeInsets.all(10),child:SizedBox(
                width: 150,
                height: 150,
                child:Column(

                  children: <Widget>[
                    Container(color:Colors.white,child: Image(image: AssetImage('assets/ye.jpg'),)),
                    Container(margin:EdgeInsets.only(top:5),alignment:Alignment.centerLeft,child:Text('Ye', style: TextStyle(color:Colors.white, fontSize: 16, fontWeight: FontWeight.bold),))
                  ],

                ),
              ));


            })),

            Container(
              margin: EdgeInsets.all(10),
              child: Text('Popular Albums', style: TextStyle(color:Colors.white, fontSize: 36, fontWeight: FontWeight.bold),),
            ),

            Container(height:200,child:ListView.builder(shrinkWrap: true, scrollDirection:Axis.horizontal, itemCount: 10,itemBuilder: (context, i) {

              return Container(margin:EdgeInsets.all(10),child:SizedBox(
                width: 150,
                height: 150,
                child:Column(

                  children: <Widget>[
                    Container(color:Colors.white,child: Image(image: AssetImage('assets/brodha.jpg'),)),
                    Container(margin:EdgeInsets.only(top:5),alignment:Alignment.centerLeft,child:Text('Way too easy', style: TextStyle(color:Colors.white, fontSize: 16, fontWeight: FontWeight.bold),))
                  ],

                ),
              ));


            })),






          ],
        ),
      ),
    );
  }

}