# ChatGPT에서 ProductPlanning 사용하기

ProductPlanning은 `visual-product-planning` 스킬, 참조 지침 4개, 산출물 양식 6개를 묶는 스킬 전용 플러그인이다. 기획 인터뷰 → 실제 화면 → 기획서·명세·가이드 → 화면 평가 → 사용자 테스트를 연결한다. 현재 버전은 **0.1.0**이다.

## 설치와 시작

Plugin Creator를 통해 현재 계정의 비공개 플러그인으로 등록한다. 계정에 활성 워크스페이스가 있으면 그 범위를 따른다. 등록과 설치 상태를 각각 확인하며 공개 디렉터리 제출이나 다른 사람에게 공유하는 작업은 별도로 다룬다.

ChatGPT에서 플러그인을 설치한 뒤 새 대화의 `@` 메뉴에서 **ProductPlanning**을 선택하고 다음처럼 요청한다.

> 내 아이디어를 제품으로 구체화해 줘. 먼저 의도를 인터뷰하고 첫 사용 화면을 보여 줘. 화면을 보며 기획서와 사용자 가이드를 함께 발전시키자.

이미 만든 화면이 있으면 평가나 테스트 준비부터 시작할 수 있다. 화면 파일·기존 결정·기획서를 함께 제공하면 같은 내용을 다시 설명하는 일을 줄일 수 있다.

화면 제작과 파일 저장에는 실행 환경에서 제공하는 도구를 사용한다. 이미지 생성·디자인 도구·실행 환경이 별도로 포함되는 것은 아니다. 정적인 시안, 실제 동작, 실제 사용자 관찰을 구분한다. 이 버전에는 별도 서버, 계정 연동이나 API 키 설정이 없다.

## 원본과 패키지

- 스킬 원본: [visual-product-planning](../.agents/skills/visual-product-planning/SKILL.md).
- 플러그인 메타데이터: [plugin.json](../plugins/product-planning/plugin.json).
- 기본 아이콘: [icon.svg](../plugins/product-planning/assets/icon.svg).
- 패키징: [package_plugin.py](../scripts/package_plugin.py).

저장소 루트에서 Python 3.9 이상으로 실행한다.

```bash
python3 scripts/package_plugin.py
```

`dist/product-planning-0.1.0.zip`이 생성된다. ZIP에는 하나의 `product-planning/` 디렉터리 아래 `plugin.json`, `assets/`, `skills/visual-product-planning/`이 들어간다. 스킬은 원본 폴더에서 그대로 가져오며 복사본을 Git에 따로 관리하지 않는다. 지침·양식의 상대 링크도 보존한다.

재배포할 때는 스킬 원본을 수정하고 메타데이터의 버전을 올린 뒤 패키지를 다시 만든다. 검증·Git 검토·병합 후 기존 플러그인의 ID와 현재 release ID를 조회해 **업데이트**한다. 같은 플러그인을 새로 만들지 않는다. 저장소를 수정하거나 병합하는 것만으로 설치된 플러그인이 자동 업데이트되지는 않는다.

업로드 전에는 ZIP 목록과 JSON/YAML, 참조 파일, 원본과의 일치를 확인한다. 등록 뒤에는 서버에 저장된 스킬과 버전, 설치 상태를 확인한다. 형식 검사는 실제 인터뷰나 화면 결과의 품질 검증을 대신하지 않는다.

## 형식 근거

확인일: **2026-11-15**. 패키지 형식과 설치 화면은 바뀔 수 있으므로 재배포할 때 현재 문서와 도구 결과를 확인한다.

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins): 루트 매니페스트, 스킬 경로, 상대 경로와 배포 구조.
- [OpenAI: Plugin architecture](https://developers.openai.com/plugins/concepts/plugins): 스킬을 포함하는 설치 단위.

설치·검증 결과는 [검증 기록](validation.md)에 남긴다.
