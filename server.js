const express = require('express'); //Node.js Web 應用程式架構，用來處理路由和 HTTP 請求
const fs = require('fs'); //用來操作系統檔案(讀寫)
const bodyParser = require('body-parser'); //解析傳入請求主體的 Middleware 
const path = require('path'); //處理檔案和目錄路徑

const app = express();
app.use(bodyParser.urlencoded({ extended: false })); //解析 HTTP request 傳送的表單資料

// Dynamic route for any sniffer endpoint
app.post('/:sniffer_id', (req, res) => {
    console.log("Data received:", req.body);

    const { sniffer_id } = req.params;
    const { time, mac, type, RSSI, uuid } = req.body;

    if (!time || !mac || !type || !RSSI || !uuid) {
        console.error("Received invalid data:", req.body);
        return res.status(400).send('Invalid data');
    }

    const dataToWrite = `${time},${mac},${type},${RSSI},${uuid}\n`;
    const fileName = `${sniffer_id}.csv`;
    const filePath = path.join(__dirname, fileName);

    try {
        fs.appendFileSync(filePath, dataToWrite);
        console.log(`Data appended to file ${fileName}`);
        res.send('Data saved successfully');
    } catch (err) {
        console.error('Error writing to file:', err);
        res.status(500).send('Error writing to file'); //400 表示 client 端錯誤、500 表示 server 端錯誤
    }
});

app.listen(9527, () => {
    console.log('Server running on port 9527');
});
