# 원문에서 질문과 평가 기준으로 연결하기

확인일: **2026-11-14**. [초기 조사](2026-11-08-methods.md)에 이어, 공개 원문의 실제 방법 설명과 사례를 읽고 인터뷰·화면 평가·사용자 테스트의 운영 기준으로 옮겼다. 유료 도서 전체나 ISO 전문을 읽었다는 의미는 아니다.

## 열람 범위와 반영 위치

아래의 ‘적용’은 이 저장소의 조합과 제안이다. 표준의 성공 기준, 전문가의 휴리스틱, 개별 조직의 운영법을 구분한다. 원문과 유료 자료를 저장소에 복제하지 않는다.

| ID | 원문과 실제 열람 범위 | 추출한 요점과 적용 | 반영 위치 |
|---|---|---|---|
| R01 | Ryan Singer, [Find the Elements](https://basecamp.com/shapeup/1.3-chapter-04)의 Breadboarding·Autopay 사례와 [Write the Pitch](https://basecamp.com/shapeup/1.5-chapter-06)의 다섯 구성·시각화 설명 | 장소·행동·연결로 의미를 탐색하고, 이번 범위와 위험을 드러낸다. 이를 실제 화면 그림으로 구체화하는 부분은 사용자의 진행 방식에 맞춘 적용이다. | 기획서·화면 명세 |
| R02 | Jeff Patton, [The New User Story Backlog is a Map](https://jpattonassociates.com/the-new-backlog/)의 flat backlog·Build a story map | 활동과 사용자 과업의 맥락을 보존한다. 개발 작업 목록과 사용자가 끝낼 일을 구분한다. | 핵심 과업과 흐름 |
| R03 | Karl Wiegers·Candase Hokanson, [Software Requirements Essentials 공개 샘플](https://www.softwarereqs.com/files/Software%20Requirements%20Essentials%20sample.pdf), 3장 Practice 6, 인쇄 47~52쪽 | 기능 요청보다 달성할 일을 묻는다. 역할·시작 사건·전제·완료·정상·대안·예외로 과업을 구체화한다. 사용 흐름에 드러나지 않는 처리도 확인한다. 기존 조사에 나온 3판과 다른 책이다. | 인터뷰·기획서·명세 |
| R04 | Teresa Torres, [Customer Interviews](https://www.producttalk.org/customer-interviews/)의 인터뷰 목적 구분·과거 행동·snapshot | 구체적 과거 사건을 따라가고 목표·맥락·기회를 기록한다. 미래 제품의 선택과 현재 행동 근거를 나눈다. | 인터뷰 |
| R05 | Militello·Hutton, [ACTA 논문 사본](https://assets.super.so/0ace7157-3bf6-491e-a8e0-fe9e6715c2db/files/eb1e3fa9-c697-4632-b91c-ef28a428466c.pdf), 2.1~2.2절, 인쇄 1620~1622쪽. [DOI](https://doi.org/10.1080/001401398186108) | 큰 과업 지도에서 어려운 판단을 골라 실제 단서·전략·초보자의 실수를 묻는다. 미래 의도 발견에 같은 효과가 입증됐다고 확대하지 않는다. | 전문가 인터뷰 |
| R06 | Matt Wynne, [Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/)의 How it works·Known unknowns·Gherkin 설명 | 규칙·사례·질문을 구분한다. 결과가 미정인 예시는 검증 사례로 확정하지 않는다. | 인터뷰·명세·전환 판단 |
| R07 | Jakob Nielsen, [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)의 원칙·설명·예시 | 상태·언어·통제·일관성·예방·기억 부담·효율·정보 집중·복구·도움을 과업에 적용한다. 표준 인증이나 사용자 테스트 결과와 구분한다. | 화면 품질 지침 |
| R08 | W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/)와 아래 선택 성공 기준의 Understanding 문서 | 검증 가능한 접근성 요구와 정적 시안에서 알 수 없는 부분을 나눈다. 선택 항목 점검으로 전체 준수를 선언하지 않는다. | 화면 품질 지침·명세 |
| R09 | GOV.UK, [심층 인터뷰](https://www.gov.uk/service-manual/user-research/using-in-depth-interviews)의 설계·진행, [사용성 테스트](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing)의 과업 설계·진행·데이터·보조기술 | 실제 또는 잠재 사용자를 정하고, 답을 주지 않는 과업과 진행 가이드를 준비한다. 파일럿과 본 세션을 구분한다. | 사용자 테스트 지침·양식 |
| R10 | GOV.UK, [연구 분석](https://www.gov.uk/service-manual/user-research/analyse-a-research-session)의 관찰 추출·분류·발견·행동, [기록 안내](https://www.gov.uk/service-manual/user-research/taking-notes-and-recording-user-research-sessions)의 동의·관찰 기록 | 실제로 본 사실, 해석과 다음 조치를 분리한다. 기록·이용에 동의를 받고 공개 저장소에는 식별 정보를 올리지 않는다. | 세션 기록·문제 목록 |
| R11 | Daniele Procida, [Tutorials](https://diataxis.fr/tutorials/)와 [How-to guides](https://diataxis.fr/how-to-guides/)의 목적·독자·진행 설명 | 학습용 첫 경험과 특정 과업 해결 안내를 구분한다. 제품 설명과 실제 사용 절차의 목적을 맞춘다. | 사용자 가이드 |

## 접근성 원문의 성격

WCAG의 성공 기준은 규범적 본문이다. Understanding은 해설 자료이며 별도의 필수 요구를 만드는 문서가 아니다. 이번에 읽은 해설은 [텍스트 대비](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [비텍스트 대비](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [최소 타깃 크기](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [포커스 가림](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html), [리플로](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)다.

대비와 크기의 수치는 예외·적용 조건과 함께 사용한다. 시안의 좌표를 실제 클릭 영역이나 CSS 크기로 단정하지 않는다. 키보드·보조기술·동적 알림은 실행 화면에서 확인해야 한다.

## 원칙이 실제 행동을 바꾸는 예

| 상황 | 피할 진행 | 개선한 진행과 남길 결과 |
|---|---|---|
| ‘AI가 알아서 처리’라는 기획 | 자동 확정을 요구사항으로 바로 채택 | 이유와 최근 사례를 듣고 실행 권한·확인·취소의 다른 화면을 제안한다. 사용자가 결정한 것과 제안을 구분한다. |
| ‘검토를 완료할 수 있다’는 요구 | 버튼을 그렸으므로 완료 처리 | 시작·완료 조건과 미확인 0건·1건·저장 실패 사례를 적고 화면 상태·가이드·검증 증거를 연결한다. |
| 미확인 항목이 남은 시안 | 회색 버튼을 접근성 위반으로 판정 | 비활성 이유가 보이는지 검토한다. 비활성 컴포넌트의 대비 예외를 확인하고 실제 의미·포커스는 미확인으로 남긴다. |
| 사용자 테스트 | ‘출처 보기 버튼을 누르고 확인 표시하세요’ | ‘이 초안을 검토해 완료로 남겨 주세요’처럼 목적을 제시한다. 평가자용 완료 조건은 별도로 두고 도움 제공을 기록한다. |
| 화면을 본 사람이 멈춤 | ‘사용자가 이해하지 못했다’만 기록 | 실제 행동·발언, 해석, 개선안, 재검증할 항목을 구분한다. 역할극은 사용자 관찰에 포함하지 않는다. |

## 충분성을 판단하는 기준

문서 수나 총점보다 중요한 것은 현재 과업에서 의도·규칙·화면·관찰·다음 결정이 연결되는가이다. 문제의 심각도와 근거 수준은 별개로 기록한다. 이 저장소의 심각도·전환 조건은 운영 제안이며 외부 자료의 인증 체계가 아니다.

이번 보강에는 [기존 화면의 자체 평가](../../examples/report-review/quality-review.md)와 [실행 전 사용자 테스트 계획](../../examples/report-review/usability-plan.md)을 포함한다. 실제 참여자 세션은 수행하지 않았다. 선택 기준의 실제 유용성과 에이전트의 인터뷰 품질은 실제 프로젝트에서 추가 검증해야 한다.
