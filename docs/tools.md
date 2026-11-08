# 도구 선택과 도입 판단

아래 프레임워크는 2026-11-08에 공식 문서와 공개 지침을 읽어 비교한 후보다. 이 저장소에 설치하거나 실행 성능을 비교하지는 않았다.

## 공개 에이전트 워크플로

| 후보와 원문 | 확인한 동작 | 채택할 부분 | 도입 전 확인 |
|---|---|---|---|
| [Superpowers brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md) | 자료를 먼저 읽고 열린 의도 질문, 한 번에 한 질문, 중간 이해 재진술을 한다. | 짧은 인터뷰, 답변 재진술, 대안 비교 | 전체 승인·개발 절차와 기존 규칙의 충돌 |
| [BMad 기획](https://docs.bmad-method.org/plan/define-requirements-and-a-specification/)과 [UX](https://docs.bmad-method.org/plan/design-ux-and-architecture/) | Brief·PRFAQ·PRD를 구분한다. 외형의 `DESIGN.md`와 동작·상태·접근성·흐름의 `EXPERIENCE.md`를 만든다. | 기획과 UX 연결, 단계별 코칭 | 작은 프로젝트의 문서량과 역할 전환 부담 |
| [BMad Forge Idea](https://docs.bmad-method.org/plan/explore-and-validate-an-idea/) | 아이디어 명확화·검증·개선 대화와 초안 비판을 지원한다. | 모호한 용어 구분, 가정 반론 | 역할극과 실제 고객 근거의 구분 |
| [Spec Kit clarify](https://github.com/github/spec-kit/blob/main/templates/commands/clarify.md)와 [흐름](https://github.github.com/spec-kit/reference/agentic-sdd.html) | 명세의 모호함을 분류하고 영향·불확실성이 큰 질문부터 묻는다. | 미정 사항 정리, 명세 누락 점검 | 기존 명세를 명확히 하는 단계와 처음 의도를 발견하는 단계의 구분 |

현재 채택한 절차는 [저장소 내 스킬](../.agents/skills/visual-product-planning/SKILL.md)에 적힌 범위다. 외부 지침 자체는 실행 지시가 아니다.

## 화면을 그리는 도구

| 표현 | 적합한 검토 | 보관할 것 | 적용 제안 |
|---|---|---|---|
| 편집 가능한 SVG | 구성·문구·상태 차이·주석 | 원본과 PNG 미리보기 | 작은 초기 화면과 예제에 사용 |
| Figma 등 디자인 도구 | 여러 화면·컴포넌트·시각 규칙·협업 | 원본 위치, 내보낸 화면, 버전 | 접근 가능한 도구가 있을 때 사용 |
| 이미지 생성 | 분위기·구도·스타일의 대안 | 이미지와 선택 이유 | 텍스트·동작이 중요한 화면은 편집 가능한 시안으로 구체화 |
| 로컬 HTML 등 클릭 시안 | 전환·입력·기다림·복구 | 소스·실행법·캡처·모의 데이터 범위 | 정적인 그림으로 판단하기 어려울 때 추가 |
| 흐름도·Mermaid | 화면과 상태의 관계 | 원문 | 실제 화면 그림에 덧붙임 |

이미지의 정교함과 기능의 완성도를 따로 표시한다. 정적인 버튼은 조작 검증, 모의 응답은 실제 서비스 검증의 증거가 아니다. 새 계정·연결·설치는 별도 선택이다.

## 첫 프로젝트의 비교 항목

같은 핵심 과업으로 작은 한 사이클을 실행하고 질문 수·시간·바로잡은 오해·문서 불일치·미정 사항 발견을 기록한다. 질문 수와 함께 결과가 기획자의 판단을 얼마나 잘 담았는지 본다.

설치 방식·명령·지원 에이전트·출력 구조는 도입 시 최신 공식 문서로 다시 확인한다.
