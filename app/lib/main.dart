import 'package:flutter/material.dart';
import 'package:flare_flutter/flare_actor.dart';

void main() {
  runApp(Sudoku());
}

class Sudoku extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: FlareActor(
        'assets/blackblock.flr',
        animation: "blackblock",
      ),
    );
  }
}
