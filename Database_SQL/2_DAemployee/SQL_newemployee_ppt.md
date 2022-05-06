
```SQL
---------------- 第10页PPT ---------------------  
/*删除表格*/


DROP TABLE if EXISTS EMP_Family,EMP_Family_2;
CREATE TABLE EMP_Family(
	`emp_no` INT,
	`Name` VARCHAR(20),
	`Age` INT,
	`tall` float
);


/*创建类似的表*/ 


CREATE TABLE EMP_Family_2 LIKE EMP_Family;
SELECT * FROM EMP_Family;
SELECT * FROM EMP_Family_2;


---------------- 第11页PPT ---------------------  


DROP TABLE if EXISTS	EMP_Family;
CREATE TABLE EMP_Family(
	`emp_no` INT,
	`Name` VARCHAR(20),
	`Age` INT,
	`tall` FLOAT,
	PRIMARY KEY(emp_no)
);


---------------- 第12页PPT ---------------------   


DROP TABLE if EXISTS	newtable;
CREATE TABLE newtable AS (
	SELECT `Date`,`County`,`City`,`AQI`
	FROM HistoryWeather
	WHERE `AQI` > 30
);
SELECT * FROM newtable;


---------------- 第13页PPT ---------------------   


/*新增資料到資料表EMP_Family*/  
insert into EMP_Family  
/*指定要新增的欄位*/
(emp_no,Name,Age,tall)
/*新增的資料*/
values(100001,'張小明',5,67.5)
/*第二筆用,連接*/
,(100002,'張大明',7,83.2)
,(100003,'張小小',1,31.9);
SELECT * FROM EMP_Family;


---------------- 第14页PPT ---------------------   


# 略過新增，因為100001跟張曉明Key值重複
INSERT IGNORE INTO EMP_Family(`emp_no`,`Name`,`Age`,`tall`)
VALUES(100001,'張小明',9,9);

# 取代新增，會把張大明的Age跟tall取代成9跟99.9
REPLACE INTO EMP_Family(`emp_no`,`Name`,`Age`,`tall`)
VALUES(100002,'張大明',9,99.9);
SELECT * FROM EMP_Family;


---------------- 第19页PPT ---------------------


/*過濾高溫43度以上的歷史天氣*/
SELECT * FROM study.HistoryWeather WHERE High_Temp > 43;
/*過濾2019-05-10之後的歷史天氣*/
SELECT * FROM study.HistoryWeather WHERE DATE >= '2019-05-10';
/*用最高溫減去最低溫算出所有歷史天氣的溫差*/
SELECT *,(High_Temp-Low_Temp) AS Temp_Diff FROM study.HistoryWeather;


---------------- 第21页PPT ---------------------
/*過濾温度20度以上,且在Guangdong省內的未来天氣*/
SELECT * FROM study.FutureWeather WHERE High_Temp > 20 AND Province = 'Guangdong';
/*過濾不是Guangdong省的未来天氣*/
SELECT * FROM study.FutureWeather WHERE NOT Province = 'Guangdong';
/*只查看Beijing和Shanghai的未来天气*/
SELECT * FROM study.FutureWeather WHERE Province = 'Shanghai' OR Province = 'Beijing';


---------------- 第22页PPT ---------------------
/*只查看Beijing和Shanghai在2019-05-12的歷史天气*/
SELECT * FROM study.HistoryWeather
WHERE (Province = 'Shanghai' OR Province = 'Beijing')
AND Date = '2019-05-12';
/*列出城市是jiujiang、beitun的历史天气*/
SELECT * FROM study.HistoryWeather WHERE City IN('jiujiang','beitun');


---------------- 第23页PPT ---------------------
SELECT * FROM study.HistoryWeather WHERE City LIKE 'an%';
/*查询城市名称第二三個字元是an的历史天气*/
SELECT * FROM study.HistoryWeather WHERE City LIKE '_an%';
/*查询城市名称第四五個字元是er的历史天气*/
SELECT * FROM study.HistoryWeather WHERE City LIKE '___er%';


---------------- 第26页PPT ---------------------
SELECT FLOOR(36.6),CEIL(36.6),ROUND(36.6),EXP(2),LOG(7.38905609893065);


---------------- 第27页PPT ---------------------
/*取得风力WindPower中第二個字元開始的兩個字元*/
/*寻找风力WindPower中的第一個'e'的位置*/
/*测量天气概况1 weatherInfo1的字符串长度*/
/*取代天氣概況1 WeatherInfo1中的‘sunshine’为‘goodday’*/
SELECT WindPower,SUBSTRING(WindPower,2,2),LOCATE('e',WindPower),
WeatherInfo1,CHAR_LENGTH(WeatherInfo1)
WindDir,REPLACE(WeatherInfo1,'sunshine','goodday')
FROM study.HistoryWeather LIMIT 1000;


---------------- 第28页PPT ---------------------
/*Trim 去除字串左右兩邊空白*/
SELECT ' A B ' AS 'before',CHAR_LENGTH(' A B ') AS 'before_length',
TRIM(' A B ') AS 'after',CHAR_LENGTH(TRIM(' A B ')) AS 'after_length' FROM dual;
/*Left 取左邊開始3個字元，Right 取右邊開始4個字元*/
SELECT LEFT('ABCDEF',3) AS 'left3',RIGHT('ABCDEF',4) AS 'Right4' FROM dual;
/*isnull 測試是否空值*/
SELECT ISNULL(NULL) AS 'IsNull1',ISNULL('') AS 'IsNull2' FROM dual;
/*upper 字符串轉大寫 Lower 字符串轉小寫*/
SELECT UPPER('aBcD') AS 'Upper1',LOWER('aBcD') AS 'Lower1' FROM dual;


---------------- 第29页PPT ---------------------
SELECT YEAR('2020-03-14 17:17:17') AS 'Year1',
MONTH('2020-03-14 17:17:17') AS 'Month1',
DAYOFMONTH('2020-03-14 17:17:17') AS 'Day1',
HOUR('2020-03-14 17:17:17') AS 'Hour1',
MINUTE('2020-03-14 17:17:17') AS 'Minute1',
SECOND('2020-03-14 17:17:17') AS 'Second1',
NOW() AS 'Now1'
FROM dual;


---------------- 第32页PPT ---------------------
SELECT County,MAX(High_Temp),MIN(Low_Temp),COUNT(*),AVG(High_Temp),SUM(AQI)
FROM study.HistoryWeather WHERE province = 'Guangdong' GROUP BY County;


---------------- 第33页PPT ---------------------
/*取得歷史天氣溫度最高前10的城市*/
SELECT * FROM study.HistoryWeather ORDER BY High_Temp DESC LIMIT 10;
/*表列天氣概況WeatherInfo1的類型*/
SELECT DISTINCT WeatherInfo1 FROM study.HistoryWeather;
/*把低溫的數據類型轉換成體溫感覺的文字描述*/
SELECT *,CASE
when Low_Temp < -10 then 'super cold'
when Low_Temp < 0 then 'very cold'
when Low_Temp < 10 then 'cold'
ELSE 'comfortable' END AS 'Temp_feel'
FROM study.HistoryWeather LIMIT 1000;



---------------- 第40页PPT ---------------------
SELECT *
FROM ZHongshan_Weather_old temp
JOIN Zhongshan_Weather_new wea
ON temp.Date = wea.Date AND temp.Time = wea.Time
AND temp.City = wea.City ;


---------------- 第41页PPT ---------------------
SELECT temp.City,temp.Date,temp.Time,temp.Temperature,wea.Wind_speed
FROM ZHongshan_Weather_old temp
left JOIN Zhongshan_Weather_new wea
ON temp.Date = wea.Date AND temp.Time = wea.Time
AND temp.City = wea.City ;


---------------- 第43页PPT ---------------------
SELECT * 
FROM ZHongshan_Humidity_Temperature
WHERE Humidity = 100 AND Temperature = 11.11
UNION 
SELECT * 
FROM ZHongshan_Humidity_Temperature
WHERE Humidity = 88 AND Temperature = 20;


---------------- 第44页PPT ---------------------
/*沒有用Rollup之前的Group,產生324列*/
SELECT Province,County,City,SUM(AQI) AS SUM_AQI
FROM HistoryWeather
WHERE Province = 'Guangdong'
GROUP BY City,WindPower;
/*用Rollup之前的Group,產生465列*/
SELECT Province,County,City,SUM(AQI) AS SUM_AQI
FROM HistoryWeather
WHERE Province = 'Guangdong'
GROUP BY City,WindPower WITH ROLLUP;


---------------- 第45页PPT ---------------------
/* 從歷史天氣篩選最高溫度小於50的廣東縣市，并從大到小排序*/
SELECT County,MAX(High_Temp)
FROM study.HistoryWeather 
WHERE Province = 'Guangdong'
GROUP BY County
HAVING MAX(High_Temp) < 50
ORDER BY MAX(High_Temp) DESC;


---------------- 第47页PPT ---------------------
/*选取工资比 Boy 高的员工名字与工资 */
SELECT `name`,`salary`
FROM employees
WHERE `salary` > (
	SELECT `salary`
	FROM employees
	WHERE `name` = 'Boy'
	);
	
/*选取部门号与gigi相同，工资比double高的 
  员工姓名和工资 */
SELECT `name`,`salary`
FROM employees
WHERE `dept` = (
	SELECT `dept`
	FROM employees
	WHERE `name` = 'gigi'
	)
AND `salary` > (
	SELECT `salary`
	FROM employees
	WHERE `name` = 'double'
	);


---------------- 第48页PPT ---------------------
/*查詢未來天氣的數據，這些地區在歷史天氣中滿足篩選要求*/
SELECT * FROM study.FutureWeather
WHERE (Province,County,City) IN (
	SELECT Province,County,City
	FROM study.HistoryWeather
	WHERE DATE > '2019-05-10'
	AND DATE < '2019-05-20'
	AND High_Temp > 30
	);

---------------- 第49页PPT ---------------------

SELECT *
FROM (
	SELECT City,COUNT(*) AS `count`
	FROM HistoryWeather
	WHERE `AQILevel` >= 3
	GROUP BY City
) AS temp
WHERE `count` >= 10;

```