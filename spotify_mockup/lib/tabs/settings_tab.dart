import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class SettingsTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Theme.of(context).primaryColor,
//          leading: Icon(
//            Icons.arrow_back,
//            color: Colors.white,
//          ),
          title: Center(
            child: Text(
              "Settings",
              style: TextStyle(color: Colors.white),
            ),
          )),
      body: Container(
        color: Theme.of(context).accentColor,
        child: ListView(
          children: <Widget>[
            ListTile(
              contentPadding: EdgeInsets.all(8.0),
              leading: Icon(
                Icons.account_circle,
                size: 80,
                color: Colors.white,
              ),
              title: Text(
                "Rishabh ",
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                    fontWeight: FontWeight.bold),
              ),
              subtitle: Text(
                "View Profile ",
                style: TextStyle(color: Colors.grey, fontSize: 15),
              ),
              trailing: Icon(
                Icons.arrow_forward_ios,
                color: Colors.white,
                size: 10,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            ListTile(
              contentPadding: EdgeInsets.all(22.0),
              title: Text(
                "Gapless ",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                ),
              ),
              subtitle: Text(
                "Allows gapless playback ",
                style: TextStyle(color: Colors.grey, fontSize: 15),
              ),
              trailing: Switch.adaptive(
                value: true,
                onChanged: null,
                inactiveThumbColor: Colors.green,
                activeTrackColor: Colors.greenAccent,
                inactiveTrackColor: Colors.green[900],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
