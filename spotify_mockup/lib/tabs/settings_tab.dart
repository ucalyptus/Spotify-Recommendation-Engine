import 'package:flutter/material.dart';

class SettingsTab extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Theme.of(context).accentColor,
      child: Center(
        child: Text('Settings',
            style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: 24)),
      ),
    );
  }
}
