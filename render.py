#!/usr/bin/env python3
"""
Procedural renderer for ai-excited-01 entry.png (1024x1024) - Revision 3
Subject: A colossal whale breaching vertically through a ring of golden clouds
above a tiny coastal town at dawn, water exploding into light around it.
Enhanced with nebula wisps, starbursts, and dramatic lighting. Smooth vignette and glowing cloud ring.
"""

from PIL import Image, ImageDraw, ImageFilter, ImageOps
import math
import random

def create_image():
    W, H = 1024, 1024
    img = Image.new("RGBA", (W, H), (10, 15, 30, 255))
    
    # 1. Background Gradient (Night sky transitioning to golden dawn at horizon)
    bg_draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        if t < 0.55:
            r = int(8 + 22 * (t/0.55))
            g = int(10 + 35 * (t/0.55))
            b = int(30 + 90 * (t/0.55))
        elif t < 0.75:
            factor = (t - 0.55) / 0.20
            r = int(30 + 225 * factor)
            g = int(45 + 170 * factor)
            b = int(120 - 90 * factor)
        else:
            factor = (t - 0.75) / 0.25
            r = int(255 - 190 * factor)
            g = int(215 - 160 * factor)
            b = int(30 - 20 * factor)
        bg_draw.line([(0, y), (W, y)], fill=(max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)), 255))

    # 2. Nebula / Aurora wisps in upper sky
    nebula_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    n_draw = ImageDraw.Draw(nebula_layer)
    random.seed(99)
    for _ in range(30):
        nx = random.randint(0, W)
        ny = random.randint(50, 500)
        nr = random.randint(80, 250)
        n_alpha = random.randint(8, 25)
        n_draw.ellipse([nx - nr, ny - int(nr*0.3), nx + nr, ny + int(nr*0.3)], fill=(120, 200, 255, n_alpha))
    
    # Stars
    for _ in range(150):
        sx = random.randint(0, W)
        sy = random.randint(0, int(H * 0.55))
        s_size = random.choice([1, 1, 2, 2, 3])
        brightness = random.randint(180, 255)
        n_draw.ellipse([sx, sy, sx + s_size, sy + s_size], fill=(255, 255, 255, brightness))

    img = Image.alpha_composite(img, nebula_layer)

    # 3. Glowing Golden Cloud Ring & Horizons (Softened with filled translucent puffs & blur)
    cloud_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(cloud_layer)
    
    center_x, center_y = W // 2, 530
    
    # Soft translucent cloud puffs forming the ring (replacing hard outlines)
    random.seed(123)
    for _ in range(140):
        theta = random.uniform(0, 2 * math.pi)
        dist_factor = random.uniform(0.55, 1.15)
        rx = center_x + math.cos(theta) * (360 * dist_factor)
        ry = center_y + math.sin(theta) * (145 * dist_factor)
        cr = random.randint(45, 130)
        c_alpha = random.randint(15, 50)
        c_draw.ellipse([rx - cr, ry - int(cr*0.6), rx + cr, ry + int(cr*0.6)], fill=(255, 215, 150, c_alpha))
    
    for _ in range(60):
        cx = random.randint(50, W - 50)
        cy = random.randint(420, 760)
        cr = random.randint(30, 110)
        c_alpha = random.randint(25, 80)
        c_draw.ellipse([cx - cr, cy - int(cr*0.5), cx + cr, cy + int(cr*0.5)], fill=(255, 215, 150, c_alpha))

    # Blur cloud layer for seamless ethereal glowing cloud appearance
    cloud_layer = cloud_layer.filter(ImageFilter.GaussianBlur(radius=12))

    img = Image.alpha_composite(img, cloud_layer)

    # 4. Colossal Whale (Dynamic vertical breach with majestic shading)
    whale_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    w_draw = ImageDraw.Draw(whale_layer)
    
    # Back / main body (deep rich indigo-slate)
    w_draw.polygon([
        (512, 200),  # head nose
        (465, 300),
        (445, 480),
        (455, 680),
        (475, 840),
        (512, 900),
        (549, 840),
        (569, 680),
        (579, 480),
        (559, 300),
    ], fill=(35, 55, 95, 255))

    # Luminous underbelly (brilliant silver-blue catching dawn light)
    w_draw.polygon([
        (512, 215),
        (508, 300),
        (513, 480),
        (523, 680),
        (533, 830),
        (512, 885),
        (549, 840),
        (559, 680),
        (549, 480),
        (539, 300),
    ], fill=(190, 220, 255, 245))

    # Ventral pleats (throat grooves characteristic of majestic baleen whales)
    for py in range(320, 650, 25):
        w_draw.line([(505, py), (519, py + 15)], fill=(150, 185, 225, 200), width=2)

    # Flukes (Tail fins) spreading grandly
    w_draw.polygon([(512, 870), (410, 810), (340, 760), (390, 830), (465, 890)], fill=(40, 60, 100, 255))
    w_draw.polygon([(512, 870), (614, 810), (684, 760), (634, 830), (559, 890)], fill=(40, 60, 100, 255))

    # Pectoral fins (swept back with power)
    w_draw.polygon([(455, 460), (325, 515), (280, 565), (365, 545), (445, 490)], fill=(30, 48, 85, 255))
    w_draw.polygon([(569, 460), (699, 515), (744, 565), (659, 545), (579, 490)], fill=(50, 75, 120, 255))

    # Eye & barnacle details
    w_draw.ellipse([494, 260, 504, 270], fill=(255, 255, 210, 255))
    for bx, by in [(498, 230), (518, 240), (508, 250), (488, 270), (528, 280)]:
        w_draw.ellipse([bx, by, bx+5, by+5], fill=(220, 240, 255, 210))

    img = Image.alpha_composite(img, whale_layer)

    # 5. Water & Light Explosions
    splash_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(splash_layer)

    # Radiant golden sunburst rays from the breach core
    for angle_deg in range(0, 360, 10):
        rad = math.radians(angle_deg)
        x2 = center_x + int(700 * math.cos(rad))
        y2 = 680 + int(700 * math.sin(rad))
        s_draw.line([(center_x, 680), (x2, y2)], fill=(255, 230, 160, 30), width=18)

    # Sparkling water droplets & light bursts
    random.seed(456)
    for _ in range(110):
        dx = random.randint(80, W - 80)
        dy = random.randint(620, 960)
        dr = random.randint(2, 14)
        d_alpha = random.randint(120, 250)
        s_draw.ellipse([dx - dr, dy - dr, dx + dr, dy + dr], fill=(210, 240, 255, d_alpha))

    # Majestic ocean surface waves & crests
    s_draw.arc([120, 630, 904, 840], start=180, end=360, fill=(230, 250, 255, 230), width=20)
    s_draw.arc([70, 660, 954, 880], start=180, end=360, fill=(190, 230, 255, 190), width=14)

    img = Image.alpha_composite(img, splash_layer)

    # 6. Tiny Coastal Town at Dawn (Scale contrast)
    town_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(town_layer)

    t_draw.polygon([
        (0, 915), (120, 895), (280, 910), (480, 890), (680, 905), (880, 895), (1024, 910),
        (1024, 1024), (0, 1024)
    ], fill=(12, 18, 30, 255))

    # Lighthouse with piercing beam
    t_draw.rectangle([860, 810, 885, 900], fill=(25, 32, 45, 255))
    t_draw.polygon([(855, 810), (872, 780), (890, 810)], fill=(220, 45, 45, 255))
    t_draw.ellipse([852, 772, 892, 798], fill=(255, 255, 180, 240))
    # Lighthouse beam cutting across water
    t_draw.polygon([(872, 785), (1024, 840), (1024, 870), (872, 785)], fill=(255, 255, 200, 40))

    # Tiny glowing windows
    for hx in [180, 220, 260, 580, 620, 660, 760, 800]:
        hy = random.randint(900, 930)
        t_draw.rectangle([hx, hy, hx + 16, hy + 14], fill=(20, 25, 40, 255))
        t_draw.rectangle([hx + 3, hy + 2, hx + 7, hy + 6], fill=(255, 225, 110, 255))

    img = Image.alpha_composite(img, town_layer)

    # 7. Smooth Radial Vignette (Darkening outer ~12% with soft radial falloff)
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    v_mask = Image.new("L", (W, H), 0)
    v_draw = ImageDraw.Draw(v_mask)
    margin = int(W * 0.12)
    v_draw.rectangle([margin, margin, W - margin, H - margin], fill=255)
    v_mask = ImageOps.invert(v_mask)
    v_mask = v_mask.filter(ImageFilter.GaussianBlur(radius=90))
    vignette.putalpha(v_mask)

    img = Image.alpha_composite(img, vignette)

    return img.convert("RGB")

if __name__ == "__main__":
    im = create_image()
    im.save("entry.png", "PNG", optimize=True)
    print("Successfully generated entry.png (Revision 3, 1024x1024)")
