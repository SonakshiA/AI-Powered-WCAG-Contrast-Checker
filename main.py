def get_rgb_to_linear(c):
    c/=255.0
    if c<=0.03928:
        c=c/12.92
    else:
        c = ((c+0.055)/1.055)**2.4
    return c

def get_luminance(rgb): #rgb is a tuple
    r,g,b = rgb
    l = 0.2126*get_rgb_to_linear(r) + 0.7152*get_rgb_to_linear(g) + 0.0722*get_rgb_to_linear(b)
    return l

def get_contrast_ratio(l1,l2):
    contrast_ratio = (l1+0.05)/(l2+0.05)
    print(contrast_ratio)
    return contrast_ratio

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2],16) for i in (0,2,4))

def is_normal_text_compliant(foreground_color, background_color):
    rgb_foreground = hex_to_rgb(foreground_color)
    rgb_background = hex_to_rgb(background_color)

    luminance_foreground = get_luminance(rgb_foreground)
    luminance_background = get_luminance(rgb_background)

    if(luminance_foreground>luminance_background):
        l1  = luminance_foreground
        l2 = luminance_background
    else:
        l1 = luminance_background
        l2 = luminance_foreground
    
    contrast_ratio = get_contrast_ratio(l1,l2)
    if(contrast_ratio>=4.5):
        return True
    else:
        return False

def is_large_text_compliant(foreground_color, background_color):
    rgb_foreground = hex_to_rgb(foreground_color)
    rgb_background = hex_to_rgb(background_color)

    luminance_foreground = get_luminance(rgb_foreground)
    luminance_background = get_luminance(rgb_background)

    if(luminance_foreground>luminance_background):
        l1  = luminance_foreground
        l2 = luminance_background
    else:
        l1 = luminance_background
        l2 = luminance_foreground
    
    contrast_ratio = get_contrast_ratio(l1,l2)
    if(contrast_ratio>=3):
        return True
    else:
        return False

def is_ui_components_compliant(foreground_color, background_color):
    rgb_foreground = hex_to_rgb(foreground_color)
    rgb_background = hex_to_rgb(background_color)

    luminance_foreground = get_luminance(rgb_foreground)
    luminance_background = get_luminance(rgb_background)

    if(luminance_foreground>luminance_background):
        l1  = luminance_foreground
        l2 = luminance_background
    else:
        l1 = luminance_background
        l2 = luminance_foreground
    
    contrast_ratio = get_contrast_ratio(l1,l2)
    if(contrast_ratio>=3):
        return True
    else:
        return False





