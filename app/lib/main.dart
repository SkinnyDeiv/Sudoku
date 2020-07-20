import 'package:app/components/Menu.dart';
import 'package:flutter/material.dart';
import 'package:flare_flutter/flare_actor.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    title: "Intro",
    home: Sudoku(),
  ));
}

class Sudoku extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: FlareActor(
        'assets/blackblock.flr',
        animation: "blackblock",
        callback: (value) => Navigator.push(context, MaterialPageRoute(builder: (context) => Menu())),
      ),
    );
  }
}
