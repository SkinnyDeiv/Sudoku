import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Menu extends StatefulWidget {
  createState() => MenuState();
}

enum PopUpKind { NEW, LOAD, NONE }

class MenuState extends State<Menu> {
  Map<PopUpKind, String> _menuOptions = {PopUpKind.NEW: 'Nuevo', PopUpKind.LOAD: 'Cargar', PopUpKind.NONE: 'Puntajes'};

  void _setPopUpKind(BuildContext context, PopUpKind popUpKind) {
    switch (popUpKind) {
      case PopUpKind.NEW:
        _showPopUp(context, 'Dificultad', _levelsContent());
        break;
      case PopUpKind.LOAD:
        break;
      case PopUpKind.NONE:
        break;
    }
  }

  void _showPopUp(BuildContext context, String titleText, Widget content) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10.0)),
          title: Text(
            titleText,
            textAlign: TextAlign.center,
            style: TextStyle(color: Color.fromRGBO(28, 37, 65, 1)),
          ),
          content: content,
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: _spawnMenuOptions(context),
      ),
    );
  }

  Widget _roundedButton(String text, Function onPressed) {
    return Container(
      width: MediaQuery.of(context).copyWith().size.width,
      margin: EdgeInsets.symmetric(vertical: 10.0, horizontal: 80.0),
      child: FlatButton(
        child: Text(
          text,
          style: TextStyle(color: Color.fromRGBO(58, 80, 107, 1), fontSize: 23.0),
        ),
        padding: EdgeInsets.all(20.0),
        onPressed: onPressed,
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(30.0),
            side: BorderSide(color: Color.fromRGBO(58, 80, 107, 1), width: 2.5)),
      ),
    );
  }

  Widget _levelsContent() {
    List<String> _levels = ['Principiantes', 'Fácil', 'Medio', 'Difícil', 'Avanzado', 'Experto'];

    return Container(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: _levels
            .map((level) => Container(
                  margin: EdgeInsets.only(top: 5.0, bottom: 10.0),
                  child: ButtonTheme(
                    minWidth: 200.0,
                    child: FlatButton(
                      color: Color.fromRGBO(28, 37, 65, 1),
                      textColor: Colors.white,
                      onPressed: () {},
                      child: Text(level),
                      padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10.0),
                          side: BorderSide(color: Color.fromRGBO(58, 80, 107, 1), width: 1.5)),
                    ),
                  ),
                ))
            .toList(),
      ),
    );
  }

  List<Widget> _spawnMenuOptions(BuildContext context) {
    List<Widget> content = [
      Container(
        margin: EdgeInsets.only(bottom: 80.0),
        child: Text(
          "Sudoku",
          style: TextStyle(color: Color.fromRGBO(91, 192, 190, 1), fontSize: 45.0, fontWeight: FontWeight.bold),
        ),
      )
    ];

    _menuOptions
        .forEach((popUpKind, text) => content.add(_roundedButton(text, () => _setPopUpKind(context, popUpKind))));
    return content;
  }
}
