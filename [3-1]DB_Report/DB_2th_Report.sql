/*	20190739 박경태		*/
/*	데이터베이스 리포트_2th	*/
/*	2023.04.17~18 작성 	*/
/*	교재 P.201~202		*/

CREATE DATABASE	극장;
USE		극장;

CREATE TABLE 극장(
	극장번호	INTEGER PRIMARY KEY,
    극장이름	VARCHAR(20),
    위치		VARCHAR(20)
);

CREATE TABLE 상영관(
	극장번호	INTEGER NOT NULL,
	상영관번호	INTEGER NOT NULL CHECK(상영관번호 BETWEEN 0 AND 10),
    영화제목	VARCHAR(20),
    가격		INTEGER CHECK(가격<20000),
    좌석수	INTEGER,
    FOREIGN KEY(극장번호)
		REFERENCES 극장 (극장번호),
	PRIMARY KEY(극장번호, 상영관번호)
);

CREATE TABLE 고객(
	고객번호	INTEGER PRIMARY KEY,
    이름		VARCHAR(20),
    주소		VARCHAR(20)
);

CREATE TABLE 예약(
	극장번호 	INTEGER NOT NULL,
    상영관번호	INTEGER NOT NULL,
    고객번호	INTEGER NOT NULL,
    좌석번호	INTEGER UNIQUE,
    날짜		DATE,
    FOREIGN KEY(극장번호, 상영관번호)
		REFERENCES 상영관 (극장번호 ,상영관번호),
	FOREIGN KEY(고객번호)
		REFERENCES 고객 (고객번호),
	PRIMARY KEY(극장번호, 상영관번호, 고객번호)
);





INSERT INTO 극장
	VALUES (1, '롯데', '잠실'), (2, '메가', '강남'), (3, '대한', '잠실');
INSERT INTO 상영관
	VALUES (1, 1, '어려운 영화', 15000, 48), (3, 1, '멋진 영화', 7500, 120), (3, 2, '재밌는 영화', 8000, 110);
INSERT INTO 고객
	VALUES (3, '홍길동', '강남'), (4,'김철수',"잠실"), (9, '박영희', '강남');
INSERT INTO 예약
	VALUES (3, 2, 3, 15, '2014-09-01'), (3, 1, 4, 16, '2014-09-01'),(1, 1, 9, 48, '2014-09-01');





/* 1-1모든 극장의 이름과 위치를 보이시오. */
SELECT 	극장이름, 위치
FROM	극장;

/* 1-2 '잠실'에 있는 극장을 보이시오. */
SELECT 	*
FROM 	극장
WHERE 	극장.위치 = '잠실';

/* 1-3 ‘잠실’에 사는 고객의 이름을 오름차순으로 보이시오. */
SELECT 	*
FROM 	고객
WHERE 	고객.주소 = '잠실'
ORDER BY	고객.주소;

/* 1-4 가격이 8,000 원 이하인 영화의 극장번호, 상영관번호, 영화제목을 보이시오. */
SELECT 	극장번호, 상영관번호, 영화제목
FROM 	상영관
WHERE 	가격<=8000;

/* 1-5 극장 위치와 고객의 주소가 같은 고객을 보이시오.  */
SELECT 	고객.*
FROM 	극장, 고객
WHERE 	극장.위치 = 고객.주소;

/* 2-1 극장의 수는 몇 개인가?  */
SELECT 	COUNT(*) AS '극장의 수'
FROM	극장;

/* 2-2 상영되는 영화의 평균 가격은 얼마인가?  */
SELECT 	AVG(가격) AS '평균 가격'
FROM	상영관;

/* 2-3 2014년 9월 1일에 영화를 관람한 고객의 수는 얼마인가?  */
SELECT 	COUNT(*) AS '2014.09.01 예약 고객'
FROM	예약, 고객
WHERE 	예약.고객번호 = 고객.고객번호 AND 날짜 = '2014-09-01';

/* 3-1 '대한'극장에서 상영된 영화제목을 보이시오.  */
SELECT	상영관.영화제목
FROM	극장, 상영관
WHERE	극장.극장이름 = '대한' AND 극장.극장번호=상영관.극장번호;

/* 3-2 '대한'극장에서 영화를 본 고객의 이름을 보이시오. */
SELECT	고객.이름
FROM	극장, 예약, 고객
WHERE	극장.극장이름 = '대한' 
	AND 극장.극장번호=예약.극장번호
	AND 고객.고객번호=예약.고객번호;
    
/* 3-3 '대한'극장의 전체 수입을 보이시오. */
SELECT	SUM(상영관.가격) AS '대한 극장의 전체 수입'
FROM	극장, 상영관
WHERE	극장.극장이름 = '대한' 
	AND 극장.극장번호=상영관.극장번호;
    
/* 4-1 극장별 상영관 수를 보이시오. */
SELECT		극장.극장번호, 극장이름, COUNT(*) AS '상영관 수'
FROM 		극장, 상영관
WHERE		극장.극장번호=상영관.극장번호
GROUP BY	극장.극장번호;

/* 4-2 '잠실'에 있는 극장의 상영관을 보이시오. */
SELECT		극장.위치, 상영관.*
FROM 		극장, 상영관
WHERE		극장.극장번호=상영관.극장번호
		AND	극장.위치='잠실';
        
/* 4-3 2014년 9월 1일의 극장별 평균 관람 고객 수를 보이시오. */
SELECT		극장번호, COUNT(*) AS '2014.09.01 평균 관람 고객 수'
FROM		예약
WHERE 		날짜 = '2014-09-01'
GROUP BY	극장번호;

/* 4-4 2014년 9월 1일에 가장 많은 고객이 관람한 영화를 보이시오. */
SELECT		MAX(영화제목) AS '2014.09.01 최다관객 영화'
FROM		상영관, 예약
WHERE 		날짜 = '2014-09-01'
		AND	상영관.극장번호=예약.극장번호
		AND 상영관.상영관번호=예약.상영관번호
GROUP BY	예약.극장번호, 예약.상영관번호;

/* 5-1 각 테이블에 데이터를 삽입하는 INSERT 문을 하나씩 실행시켜 보시오. */
INSERT INTO 극장 	VALUES (4, 'CGV', '동래');
INSERT INTO 상영관 	VALUES (4, 1, '무서운 영화', 12000, 60);
INSERT INTO 고객 	VALUES (12, '박경태', '동래');
INSERT INTO 예약		VALUES (4, 1, 12, 20, '2023-04-18');

/* 5-2 영화의 가격을 10%씩 인상하시오. */
UPDATE 	상영관	SET 	가격=가격*1.1;
SELECT	가격		FROM	상영관;  
