import streamlit as st
import re

questions = [
    {"ko": "1. 신체적 염려", "en": "1. Somatic Concern - Preoccupation with physical health, fear of physical illness, hypochondriasis."},
    {"ko": "2. 불안", "en": "2. Anxiety - Worry, fear, over-concern for present or future, uneasiness."},
    {"ko": "3. 정서적 위축", "en": "3. Emotional Withdrawal - Lack of spontaneous interaction, isolation, deficiency in relating to others."},
    {"ko": "4. 사고 혼란", "en": "4. Conceptual Disorganization - Thought processes confused, disconnected, disorganized, disrupted."},
    {"ko": "5. 죄책감", "en": "5. Guilt Feelings - Self-blame, shame, remorse for past behavior."},
    {"ko": "6. 긴장", "en": "6. Tension - Physical and motor manifestations of nervousness, over-activation."},
    {"ko": "7. 기이한 자세 및 버릇", "en": "7. Mannerisms and Posturing - Peculiar, bizarre, unnatural motor behavior (not including tic)."},
    {"ko": "8. 과대감", "en": "8. Grandiosity - Exaggerated self-opinion, arrogance, conviction of unusual power or abilities."},
    {"ko": "9. 우울한 기분", "en": "9. Depressive Mood - Sorrow, sadness, despondency, pessimism."},
    {"ko": "10. 적대감", "en": "10. Hostility - Animosity, contempt, belligerence, disdain for others."},
    {"ko": "11. 의심", "en": "11. Suspiciousness - Mistrust, belief others harbor malicious or discriminatory intent."},
    {"ko": "12. 환각행동", "en": "12. Hallucinatory Behavior - Perceptions without normal external stimulus correspondence."},
    {"ko": "13. 운동 지연", "en": "13. Motor Retardation - Slowed, weakened movements or speech, reduced body tone."},
    {"ko": "14. 협조성 부족", "en": "14. Uncooperativeness - Resistance, guardedness, rejection of authority."},
    {"ko": "15. 이상한 사고 내용", "en": "15. Unusual Thought Content - Unusual, odd, strange, bizarre thought content."},
    {"ko": "16. 정서 둔마", "en": "16. Blunted Affect - Reduced emotional tone, reduction in formal intensity of feelings, flatness."},
    {"ko": "17. 동요", "en": "17. Excitement - Heightened emotional tone, agitation, increased reactivity."},
    {"ko": "18. 지남력 장애", "en": "18. Disorientation - Confusion or lack of proper association for person, place or time."}
]

score_options = [
    "Not assessed (0)",
    "Not present (1)",
    "Very mild (2)",
    "Mild (3)",
    "Moderate (4)",
    "Moderately severe (5)",
    "Severe (6)",
    "Extremely severe (7)"
]

user_responses = []
st.title("The Brief Psychiatric Rating Scale (BPRS)")

for idx, q in enumerate(questions):
    choice = st.selectbox(q["ko"], score_options, index=1, key=idx)
    user_responses.append(f"{q['en']} {choice}")

if st.button("Show Result"):
    if len(user_responses) != 18:
        st.warning("모든 18개 문항에 응답해 주세요.")
    else:
        # 총점 계산
        scores = [int(re.search(r"\((\d+)\)", response).group(1)) for response in user_responses]
        total_score = sum(scores)

        # 증상군 점수 계산
        cognitive = sum([scores[i - 1] for i in [4, 12, 15]])
        retardation = sum([scores[i - 1] for i in [3, 13, 16]])
        anxiety = sum([scores[i - 1] for i in [2, 5, 9]])
        hostility = sum([scores[i - 1] for i in [10, 11, 14]])
        excitement = sum([scores[i - 1] for i in [6, 17]])

        # 출력 생성
        output_lines = ["The Brief Psychiatric Rating Scale (BPRS)", ""]
        output_lines.extend(user_responses)
        output_lines.append("")
        output_lines.append("**총점**")
        output_lines.append(str(total_score))
        output_lines.append("")
        output_lines.append("**증상군 별 점수**")
        output_lines.append(f"사고장애: {cognitive}")
        output_lines.append(f"철퇴/지연: {retardation}")
        output_lines.append(f"불안/우울: {anxiety}")
        output_lines.append(f"적대/의심: {hostility}")
        output_lines.append(f"동요/흥분: {excitement}")

        final_output = "\n".join(output_lines)
        st.code(final_output, language="markdown")
