# run tasks ON ANY FILE CHANGE DETECTION in a directory
uses a .changy file

run it using changy,
a minimum of 5 seconds of delay(by default) that is required between tasks
for changy to detect there has been a file change

## contents of .changy

changy is a yaml file
that has to be structured in this way

```
tasks:
    - ./music
    - ./your_mom
```

you may also set a custom delay here (in seconds)

```
delay: 3
tasks:
    - a
    - b
    - c
```

where a, b, c are shell commands
