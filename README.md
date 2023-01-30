# gs-shuffle

## Usage
- Please create a google spreadsheet called `gs-shuffle` and remain Sheet1 be `Sheet1`

- Then using google cloud app engine to create a service account to access this spreadsheet

- Copy/Replace the `sevice_account.json` to `flask-app` folder

- `docker-compose build` and `docker-compose up`

<br>

## Spreadsheet Sample
|  Fruit   | Instrument  | Peripherals |
|  ----  | ----  | ---- |
| Apple  | Piano | Mouse |
| Orange  | Violin | Keyboard |
| Melon  |  | Headphone
| Lemon  |  |

## REST API
>http://example.com/category

>http://example.com/category/Fruit
