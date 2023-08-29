import src.config as con


def ChangeLanguage(language):
    con.LANGUAGE = language
    if con.LANGUAGE == 'en':
        con.TargetTitle = con.TitleEN[con.TargetNumber]
        con.TargetLink = con.LinksEN[con.TargetTitle]
        con.TargetHints = con.HintsEN[con.TargetTitle]
    elif con.LANGUAGE == 'ru':
        con.TargetTitle = con.TitleRU[con.TargetNumber]
        con.TargetLink = con.LinksRU[con.TargetTitle]
        con.TargetHints = con.HintsRU[con.TargetTitle]


def ChangeTarget(target_id):
    con.TargetNumber = target_id
    ChangeLanguage(con.LANGUAGE)
