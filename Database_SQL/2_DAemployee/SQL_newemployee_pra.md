练习1：
1. 请列出2019年5月1号的历史天气（提示: 使用 = 运算符）
2. 找出省份Province不是Guangdong的未来天气资料 (提示: 使用 != 运算符)
3. 如果想要低温低于零度的的未来天气，SQL指令该怎么下?（提示: 使用 < 运算符）


练习2：
1. 请从历史天气中列出省份Province是Sichuan而且县市County是panzhihua的资料（提示: 使用 = 与 AND 运算符）
2. 请从历史天气查询空气质量AQI为 50、100、180的天气资料 （提示: 使用 AND 或 IN 运算符）
3. 请从历史天气查询天气概况WeatherInfo1没有”rain”的资料 （提示: 使用NOT LIKE以及%）

练习3：
1. 请从历史天气把天气概况WeatherInfo1作替换，有”雪”的，替换成有雪，有”雨”的，替换成下雨，其它的，替换成晴天。 （提示：使用Replace及Case when.. then.. else..）
2. 从历史天气依省份、县市、统计日期作每个县市的最高温度排序。 (提示：使用group by、max()、desc)
3. 请从历史天气计算出各地方平均空气质量AQI。 (提示：使用group by、average())

练习4:
1. 请从HistoryWeather表，查询天气概况WeatherInfo1没有“rain”的全部资料。（10分）

```SQL
SELECT * FROM study.HistoryWeather WHERE WeatherInfo1 NOT LIKE '%rain%';
```

2. 请从HistoryWeather表，依城市（City）分组求每个城市的High_Temp的最大值，并从大到小排序，最后只要City和High_Temp最大值。（15分）

```SQL
SELECT City,MAX(High_Temp) AS max_temp FROM study.HistoryWeather 
GROUP BY City ORDER BY max_temp DESC;
```

3. 请从HistoryWeather表，筛选5月份的数据，对月份及City进行分组求AQI的平均值，筛选平均AQI>100，最后展示月份、城市、平均AQI。（15分）

```SQL
SELECT MONTH(`Date`) AS month,`City`,AVG(AQI)
FROM HistoryWeather
WHERE MONTH(`Date`)=5
GROUP BY MONTH(`Date`),City
HAVING AVG(AQI) > 100;
```

4. 请从employees表，利用SubString函数或Like语法，
选取部门前缀(首字母)与gigi相同，工资比boy高的，员工姓名和工资 （提示：利用SubString或Like语法）（30分）

```SQL
/*（方法1）*/

SELECT `name`,`salary`
FROM employees
WHERE SUBSTRING(`dept`,1,1) = (
	SELECT SUBSTRING(`dept`,1,1)
	FROM employees
	WHERE `name` = 'gigi'
	)
AND `salary` > (
	SELECT `salary`
	FROM employees
	WHERE `name` = 'boy'
	);

/*（方法2）:*/
SELECT `name`,`salary`
FROM employees
WHERE `dept` LIKE  (
	SELECT CONCAT(SUBSTRING(`dept`,1,1),'%')
	FROM employees
	WHERE `name` = 'gigi'
	)
AND `salary` > (
	SELECT `salary`
	FROM employees
	WHERE `name` = 'boy'
	);
```

5. 对Zhongshan_Weather_new/old两张表，通过City、Date、Humidity、Time进行右链接，取得new表的Pressure数据，并保留一位小数，命名为为 Pressure，筛选Humidity为100的数据，最后只要这五列数据。（30分）
  

```SQL
SELECT temp_old.City,temp_old.Date,temp_old.Time,temp_old.Humidity,
Round(temp_new.Pressure,1) AS Pressure
FROM Zhongshan_Weather_new `temp_new`
Right Join ZHongshan_Weather_old `temp_old`
ON temp_old.City = temp_new.City AND temp_old.Date = temp_new.Date
AND temp_old.Humidity = temp_new.Humidity 
AND temp_old.Time = temp_new.Time
WHERE temp_new.Humidity = 100;
```