create database car_insurance; 
use car_insurance;
select * from car_ins; 		-- 자동차 보험 할인 특약 정보
select * from car_ins_com;	-- 자동차 보험 회사 정보

ALTER DATABASE car_insurance CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;



## car_ins_com 회사명 전처리 // Parent
update	car_ins_com 
set 	회사명 = replace(회사명, '주식회사', '')
where	회사명 like '%주식회사';

## car_ins 회사명 전처리 // children
UPDATE car_ins
SET 회사명 = CASE
    WHEN 회사명 LIKE '%손보' THEN REPLACE(회사명, '손보', '손해보험')
    WHEN 회사명 LIKE '%화재' THEN REPLACE(회사명, '화재', '화재보험')
    WHEN 회사명 LIKE '%해상' THEN REPLACE(회사명, '해상', '해상화재보험')
	WHEN 회사명 = '삼성화재보험' THEN '삼성화재해상보험'
    WHEN 회사명 = '흥국화재보험' THEN '흥국화재해상보험'
    ELSE 회사명
END
WHERE 회사명 LIKE '%손보' OR 회사명 LIKE '%화재' OR 회사명 LIKE '%해상' or 회사명 = '삼성화재보험' or 회사명 = '흥국화재보험';

## my sql에서는 blob 또는 text type의 길이를 정해주지 않으면 컬럼을 pk로 등록하지 못함.
## type 변경 후  pk로 등록 
ALTER TABLE car_ins_com MODIFY 회사명 VARCHAR(10);
alter table car_ins_com
add primary key(회사명);

## type 변경 후 fk로 등록
ALTER TABLE car_ins MODIFY 회사명 VARCHAR(10);
alter table car_ins add constraint car_ins_fk
foreign key (회사명) references car_ins_com(회사명);
