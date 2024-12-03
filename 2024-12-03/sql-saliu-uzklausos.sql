-- Išfiltruokite visas šalis kurių bendras vidaus produktas yra didesnis nei 11000

SELECT country_name FROM country_data WHERE gdpp > 11000;

-- Išfiltruokite visas šalis kurių importo indeksas mažesnis arba lygus 30

SELECT country_name FROM country_data WHERE imports <= 30;

-- AND - Sujungia dvi sąlygas į vieną, abi sąlygos turi būti teigiamos (TRUE)
-- OR - TIk viena sąlyga turi būti teigiama

-- Išfiltruokite visas šalis kurių bendras vidaus produktas yra didesnis nei 11000 IR importo indeksas yra mažesnis arba lygus 30

SELECT country_name FROM country_data WHERE gdpp > 11000 AND imports <= 30;

-- Išfiltruokite visas šalis kurių bendras vidaus produktas yra didesnis nei 11000 ARBA importo indeksas yra mažesnis arba lygus 30

SELECT country_name FROM country_data WHERE gdpp > 11000 OR imports <= 30;