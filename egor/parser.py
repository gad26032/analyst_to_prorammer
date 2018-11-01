def cut_table(text):
    open_tag = '<tag>'
    close_tag = '</tag>'
    some_text = text.split(open_tag)[-1]
    some_text = some_text.split(close_tag)[0]
    return some_text



df['raw_table'] = df['raw_data'].apply(cut_table)

