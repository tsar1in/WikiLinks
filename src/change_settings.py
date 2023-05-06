import src.config as con


def ChangeLanguage(language):
    global LANGUAGE, TargetNumber, TargetTitle, TargetLink, TargetHints, TitleEN, LinksEN, HintsEN
    LANGUAGE = language
    if LANGUAGE == 'en':
        TargetTitle = TitleEN[TargetNumber]
        TargetLink = LinksEN[TargetTitle]
        TargetHints = HintsEN[TargetTitle]
    elif LANGUAGE == 'ru':
        TargetTitle = con.TitleRU[TargetNumber]
        TargetLink = con.LinksRU[TargetTitle]
        TargetHints = con.HintsRU[TargetTitle]


def ChangeTarget(target_id):
    global LANGUAGE, TargetNumber, TargetTitle, TargetLink, TargetHints, TitleEN, LinksEN, HintsEN
    TargetNumber = target_id
    ChangeLanguage(LANGUAGE)
