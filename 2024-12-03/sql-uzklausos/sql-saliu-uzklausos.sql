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

-- Suraskite visas šalis kurių vidutinės pajamos yra didesnės nei 15001, o bendras vidaus produktas mažesnis nei 8300;

SELECT country_name FROM country_data WHERE income > 15001 AND gdpp < 8300;

-- Suraskite šalių infliacijos indeksą, kurių pavadinime yra raidė "l".

SELECT country_name, inflation FROM country_data WHERE country_name LIKE '%l%';

-- Suraskite šalių infliacijos indeksą, kurių pavadinime yra raidė "b", bet vidutinė gyvenimo trukmė yra mažesnė nei 70 metų.

SELECT country_name, inflation FROM country_data WHERE country_name LIKE '%b%' AND life_expectancy < 70;