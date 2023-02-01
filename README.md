# gs-shuffle

## Screenshot
<img src="https://user-images.githubusercontent.com/5573927/216109413-8fe347a2-572b-4754-98c9-cc82537e3bb8.gif" width="400">

## Usage
- Please create a google spreadsheet called `gs-shuffle` and remain Sheet1 be `Sheet1`

- Then using google cloud app engine to create a service account to access this spreadsheet

- Copy/Replace the `sevice_account.json` to `gspread` folder

- `docker-compose build` and `docker-compose up`

<br>

## Spreadsheet Sample
|  Fruit   | Instrument  | Peripherals |
|  ----  | ----  | ---- |
| Apple  | Piano | Mouse |
| Orange  | Violin | Keyboard |
| Melon  |  | Headphone |

| Lemon  |  |

## REST API
>http://example.com/category

>http://example.com/category/Fruit
