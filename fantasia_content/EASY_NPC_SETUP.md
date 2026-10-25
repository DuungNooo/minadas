# Fantasia NPC UX — 일반 유저 명령어 0개

원칙:
일반 유저는 명령어를 입력하지 않는다.

유저가 하는 행동:
1. NPC 우클릭
2. 대화 버튼 클릭
3. 선물 버튼 클릭
4. 의뢰 수락/완료 버튼 클릭
5. 관계 보기 버튼 클릭
6. FTB Quests에서 진행 확인
7. 실제 전투/탐험/제작/퍼즐 수행

명령어는 Easy NPC의 Action에서 내부적으로 실행할 뿐
유저에게 보여주거나 직접 입력하게 하지 않는다.

권장 NPC 공통 버튼

[대화]
내부 Action:
fantasia_npc <NPC_ID> talk

[선물하기]
내부 Action:
fantasia_npc <NPC_ID> gift

[관계]
내부 Action:
fantasia_npc <NPC_ID> status

[메인 진행 확인]
내부 Action:
fantasia_story status

[인연 목록]
내부 Action:
fantasia_bonds

위 문자열은 관리자/NPC 제작자가 설정할 내부 액션이며
일반 유저에게 명령어 안내를 하지 않는다.

입학 검사
- 첫 접속 시 자동 시작
- 유저는 채팅에 표시된 선택지를 클릭
- 클릭이 내부 명령을 실행하지만 사용자는 명령어를 알 필요 없음
- 과거 문항 버튼은 재사용 불가

캐릭터 상태 확인
- 학생회/접수 NPC에 [내 정보] 버튼 생성
- 내부 Action으로 fantasia_stats 호출
- 유저는 버튼만 누름

스토리/컨텐츠 확인
- 아카데미 게시판 NPC 또는 안내 NPC에 [현재 목표] 버튼 생성
- 내부 Action으로 fantasia_content 또는 fantasia_story status 호출
- 유저는 버튼만 누름

퀘스트
- FTB Quests UI로 확인
- 퀘스트 완료는 실제 행동/스토리 이벤트에서 자동 처리
- 유저가 명령어로 완료시키는 구조 금지

OP 명령은 서버 관리자 테스트/복구용으로만 유지한다.
