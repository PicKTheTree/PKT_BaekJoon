
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
	values (1, 1, '어려운 영화', 15000, 48), (3, 1, '멋진 영화', 7500, 120), (3, 2, '재밌는 영화', 8000, 110);
INSERT INTO 고객
	values (3, '홍길동', '강남'), (4,'김철수',"잠실"), (9, '박영희', '강남');
INSERT INTO 예약
	values (3, 2, 3, 15, '2014-09-01'), (3, 1, 4, 16, '2014-09-01'),(1, 1, 9, 48, '2014-09-01');

/* 1-1모든 극장의 이름과 위치를 보이시오. */
SELECT 	극장이름, 위치
FROM	극장

/* 1-2 '잠실'에 있는 극장을 보이시오. */
SELECT 	*
FROM 	극장
WHERE 	극장.위치 = '잠실';

/* 1-3 ‘잠실’에 사는 고객의 이름을 오름차순으로 보이시오. */
SELECT 	*
FROM 	고객
WHERE 	고객.주소 = '잠실'
ORDER BY 고객.주소;

/* 1-4 가격이 8,000 원 이하인 영화의 극장번호, 상영관번호, 영화제목을 보이시오. */
SELECT 	극장번호, 상영관번호, 영화제목
FROM 	상영관
WHERE 	가격<=8000
