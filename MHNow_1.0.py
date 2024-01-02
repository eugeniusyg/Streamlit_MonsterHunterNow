import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Monster Hunter Now",
    page_icon="./images/MHNow_Logo.png"
)

st.title("Monster Hunter Now")

weapons = [
    {
        "name":"헌터나이프",
        "type":"한손검",
        "property":"무속성",
        "skill":"독 내성 Lv 1",
        "skill_level":4
    },
    {
        "name":"쟈그라스에지",
        "type":"한손검",
        "property":"물",
        "skill":"체력 증강 Lv 1",
        "skill_level":4
    },
    {
        "name":"블룸나이프",
        "type":"한손검",
        "property":"독",
        "skill":"기습 Lv 1",
        "skill_level":8
    },
    {
        "name":"트윈대거",
        "type":"쌍검",
        "property":"무속성",
        "skill":"독 내성 Lv 1",
        "skill_level":4
    },
    {
        "name":"비크대거",
        "type":"쌍검",
        "property":"무속성",
        "skill":"불굴 Lv 1",
        "skill_level":4
    },
    {
        "name":"펄서해체트",
        "type":"쌍검",
        "property":"번개",
        "skill":"회피 거리 UP Lv 1",
        "skill_level":8
    }
]

equipment, skill = st.columns([2,1])
with equipment:
    st.subheader("장비")
    weapon, armor = st.tabs(["무기", "방어구"])
    with weapon:
        type, property = st.columns(2)
        with type:
            choice1 = st.multiselect(
                "무기 종류",
                ('한손검','쌍검','대검','태도','해머','랜스','라이트보우건','활'),
                placeholder="무기 종류를 선택하세요.")
        with property:
            choice2 = st.multiselect(
                "속성",
                ('불','물','번개','얼음','용','독','마비','수면','무속성'),
                placeholder="속성을 선택하세요."
            )
        if not choice1 and not choice2:
            weapon_table = pd.DataFrame(
                {"무기 종류":[weapons[i]['type'] for i in range(len(weapons))],
                 "속성":[weapons[i]['property'] for i in range(len(weapons))],
                 "장비 스킬":[weapons[i]['skill'] for i in range(len(weapons))]
                },
                index = [weapons[i]['name'] for i in range(len(weapons))]
            )
            st.table(weapon_table)
        elif choice1 and not choice2:
            weapon_choice = list()
            for i in range(len(choice1)):
                for x in weapons:
                    if x["type"]==choice1[i]:
                        weapon_choice.append(x)
            weapon_table_choice = pd.DataFrame(
                {"무기 종류":[weapon_choice[i]['type'] for i in range(len(weapon_choice))],
                 "속성":[weapon_choice[i]['property'] for i in range(len(weapon_choice))],
                 "장비 스킬":[weapon_choice[i]['skill'] for i in range(len(weapon_choice))]
                },
                index = [weapon_choice[i]['name'] for i in range(len(weapon_choice))]
            )
            st.table(weapon_table_choice)
        elif not choice1 and choice2:
            weapon_choice = list()
            for i in range(len(choice2)):
                for x in weapons:
                    if x["property"]==choice2[i]:
                        weapon_choice.append(x)
            weapon_table_choice = pd.DataFrame(
                {"무기 종류":[weapon_choice[i]['type'] for i in range(len(weapon_choice))],
                 "속성":[weapon_choice[i]['property'] for i in range(len(weapon_choice))],
                 "장비 스킬":[weapon_choice[i]['skill'] for i in range(len(weapon_choice))]
                },
                index = [weapon_choice[i]['name'] for i in range(len(weapon_choice))]
            )
            st.table(weapon_table_choice)
with skill:
    st.subheader("장비 스킬")





