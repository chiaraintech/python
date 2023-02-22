def markdown(input):
    res = '<p>'
    block_is_active = False
    strikethrough_began = False

    i = 0
    while i < len(input):
        current_characters = input[i: i+2]
        single_char = input[i:i + 1]

        if single_char == '\n':
            if input[i + 1: i + 2] == '\n':
                res += close_blockquote(block_is_active)
                res += '</p><p>'
                i += 2
            else:
                res += '<br />'
                i += 1

        elif current_characters == '> ':
            res += handle_blockquote(block_is_active)
            i += 2
        elif current_characters == '~~':
            res += handle_strikethrough(strikethrough_began)
            i += 2
        else:
            current_characters += input[i]
            i += 1
        
    res += '</p>'
    return res

def handle_blockquote(block_is_active):
    if not block_is_active:
        block_is_active = True
        return '<blockquote>'
    return ''

def handle_strikethrough(strikethrough_began):
    if not strikethrough_began:
        strikethrough_began = True
        return '<del>'
    else:
        strikethrough_began = False
        return '</del>'

def close_blockquote(block_is_active):
    if block_is_active:
        block_is_active = False
        return '</blockquote>'
    return ''
