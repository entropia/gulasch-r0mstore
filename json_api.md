Request and Responses
=====================

/roms/json/list/
----------------
List all roms and available tags without filtering.

```json
{
    "filter_tag": "<always empty string here>",
    "tags": {
		"<slug>" : "<tag name>",
        "foo": "Foo",
        "bar": "Bar"
    },
    "roms": {
		"<id>" : "<rom name>",
        "2": "Annother Test",
        "3": "SuperDuperRom",
        "4": "LolRom",
        "5": "RoflRom",
        "6": "FooRom",
        "7": "Annother Test2"
    }
}
```


/roms/json/list/< tag slug >/
------------------------------
List roms that are tagged with the tag associated to **tag slug**.
Still list *all* available tags.
```json
{
    "filter_tag": "<tag slug>",
    "tags": {
		"<slug>" : "<tag name>",
        "foo": "Foo",
        "bar": "Bar"
    },
    "roms": {
		"<id>" : "<rom name>",
        "6": "FooRom",
        "7": "Annother Test2"
    }
}
```

/roms/json/details/< rom id >/
------------------------------
Returns details about rom associated by **rom id**.
```json
{
    "id": 7,
    "name": "Annother Test2",
    "description": "Lalalala\r\n\r\nBeschreibung, Dinge und anderen Kram\r\n\r\nLadida",
    "tags": [
        "Foo",
        "Bar"
    ],
    "low_binary": "/media/roms/1ba99feb-eed9-47c5-b626-2f39ebe8c164.bin",
    "high_binary": "/media/roms/594d1c79-87e2-4fec-81b8-76845bf8016b.bin",
    "creation_time": "2017-05-12T19:13:20.703Z",
    "edit_time": "2017-05-12T19:13:20.746Z"
}
```
