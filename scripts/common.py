from PIL import Image, ImageColor

def save_img(chars, target_path, resize=False):
    for idx, cc in enumerate(chars):
        layers = [ Image.open(src) for src in cc ]
        # create random bgcolor image
        # hue = random.randint(0, 360)
        # bg_color = ImageColor.getrgb('hsl({},100%,70%)'.format(hue)) # 70% brightness
        bg_color = (255, 255, 255, 255) # white
        new_img = Image.new("RGBA", layers[0].size, bg_color)
        # overlay layers
        for layer in layers:
            if layer.mode != "RGBA":
                layer = layer.convert("RGBA")
            new_img = Image.alpha_composite(new_img, layer)
        # debug
        if resize:
            new_img = new_img.resize((500, 500))
        # save to file
        out_path = target_path.format(idx+1)
        print('{}..'.format(out_path))
        new_img.save(out_path, "PNG")
