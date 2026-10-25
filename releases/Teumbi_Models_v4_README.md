# 틈비 V4 — 참고 비례와 픽셀 표현을 적용한 수정본

사용자가 제시한 가디안·뮤츠·디아루가·피카츄를 비례와 인상의 기준으로 삼았습니다. 초기형은 친근한 작은 생물, 최종형은 작은 얼굴과 긴 팔다리·늘어진 외형을 가진 성숙한 실루엣으로 구분했습니다. 형태와 텍스처는 새로 제작한 원본 디자인입니다.

## V4에서 바뀐 것

- **틈비:** 별도 머리·양팔·받침 발 구성을 없애고, 표정 있는 한 개의 코어를 세 개의 비대칭 껍질이 감쌉니다.
- **불꽃:** 작은 동물형 머리, 길게 이어지는 몸통·역관절 다리, 긴 균형 꼬리와 팔 자체인 초승달 도끼를 갖습니다.
- **전기:** 얼굴과 허리를 좁히고 목·팔·다리를 길게 했습니다. 흐르는 망토와 비대칭 번개 볏, 몸에 연결된 한 갈래 피뢰침을 배치했습니다.
- **풀:** 작은 가면형 얼굴과 뒤로 뻗는 잎 장식, 긴 뿌리 다리, 하나로 맞물리는 잎 모양 손을 갖습니다.
- **물:** 작은 얼굴과 긴 목·팔다리, 뒤로 흐르는 지느러미 망토를 갖습니다. 하프는 팔에서 자라고, 연주 손과 현의 접촉 위치를 맞췄습니다.

눈과 입은 돌출된 흰자·동공 큐브 대신 두께 0의 픽셀 면으로 표현했습니다. 잎·망토·지느러미 가장자리도 알파 컷아웃으로 윤곽을 만들었습니다. 기본 텍셀 밀도는 모델 1단위당 1픽셀이며 128×128 아틀라스를 사용합니다. 속성별로 13~17색 팔레트를 정했습니다. 코어·고열부는 별도 발광 마스크를 제공하고 일반 눈은 발광하지 않습니다.

## 먼저 확인하기

압축 해제 후 `VIEW_MODELS.html`을 Chrome·Edge 등의 WebGL 브라우저에서 여세요. 인터넷 연결 없이 모델을 회전하고 모션을 재생할 수 있습니다. 재생/정지·처음부터·시간 슬라이더·정면/뒤쪽 보기로 확인하세요.

`previews`의 `_game.png`와 GIF는 실제 모델과 텍스처를 브라우저에서 렌더링한 것입니다. `role-motions.gif`는 최종형 4종의 고유 동작을 동시에 비교합니다. 생성형 콘셉트 이미지가 아닙니다.

## 포함 파일

| 폴더 | 내용 |
|---|---|
| `blockbench` | PNG와 모션을 내장한 편집 원본 `.bbmodel` |
| `models` | Bedrock 형식 `.geo.json` |
| `textures` | 이진 알파 픽셀 텍스처, 발광 마스크 |
| `animations` | 대기·이동·공격·고유기·피격·쓰러짐, 모델별 6개씩 합계 54개 |
| `glb` | 알파 컷아웃과 양면 재질을 포함한 정적 3D 검사 파일 |
| `source` | 큐브·평면·본·UV·정방향 모션 데이터 |
| `previews` | 실제 모델 이미지·GIF·원본 해시 기록 |
| `tools` | 모델·텍스처·뷰어 생성과 검증 도구 |

기절 모션은 마지막 자세를 유지합니다. 다른 고유 동작에는 준비·실행·반동·회복 구간이 있습니다. 불꽃의 꼬리, 전기의 피뢰침, 풀의 손바닥과 다리, 물의 현·물줄기·망토를 별도 본으로 나눴습니다.

## 검증과 게임 연결

솔리드와 두께 0 평면, 평면의 유효 양면 UV, 알파 0/255, 본 계층과 좌표 변환, 원본/내보내기 모션 참조를 검사했습니다. 뷰어와 GLB에서 알파 컷아웃과 양면 표시를 확인했습니다. 게임 이벤트 연결을 포함한 Minecraft/Cobblemon 내 실행은 아직 검증하지 않았습니다. 사용하는 버전에 맞는 종·진화·스폰 데이터와 resolver/poser, 전투 동작 연결이 별도로 필요합니다. GLB는 정적 검사 파일이며 모션 편집은 bbmodel/animation.json을 사용하세요.

## 스타일 조사

공식 Cobblemon 소스의 [Ralts](https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/resources/assets/cobblemon/bedrock/pokemon/models/0280_ralts), [Golett](https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/resources/assets/cobblemon/bedrock/pokemon/models/0622_golett), [Litwick](https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/resources/assets/cobblemon/bedrock/pokemon/models/0607_litwick)을 조사해 텍셀 밀도와 표정·윤곽용 평면 사용 방식을 참고했습니다. 이 패키지에 해당 모델이나 텍스처를 복제해 넣지 않았습니다.

재생성은 `tools`에서 `python build.py`, 구조 검증은 `python validate.py`입니다. Python 3와 Pillow가 필요합니다. 정적 GLB 도구는 Blender 4.3+, 브라우저 검사·캡처는 Node.js/Playwright/Chromium을 사용합니다. 한글 시트 폰트 경로는 OS에 맞게 조정할 수 있습니다.
