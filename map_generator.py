import random

nations = ['Yenianorth', 'Nestates Roonbra Territories', 'Ngothe', 'Dodenswe', 'Coconguilla', 'Nivirfrench', 'Western Reale Briwales', 'Ustswa', 'Eastern Viacogi', 'Grobai', 'New Ngagia Ilyi', 'Lapuama Republic']
landforms = ['in a plain', 'in a forest', 'on a hill', 'on a mountain', 'in a swamp', 'in a lake', 'in a valley', 'in a desert', 'on a plateau']
coastal_landforms = ['in the ocean', 'on an island']

def generate_map():
  aNation = random.choice(nations)
  bNation = random.choice(nations)
  cNation = random.choice(nations)
  dNation = random.choice(nations)
  a1 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a2 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a3 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a4 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a5 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a6 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a7 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a8 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a9 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a10 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a11 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a12 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a13 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a14 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a15 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a16 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a17 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a18 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a19 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a20 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a21 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a22 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a23 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a24 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  a25 = {'landform': random.choice(landforms), 'nation': aNation, 'people': [], 'items': []}
  b1 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b2 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b3 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b4 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b5 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b6 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b7 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b8 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b9 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b10 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b11 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b12 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b13 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b14 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b15 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b16 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b17 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b18 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b19 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b20 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b21 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b22 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b23 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b24 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  b25 = {'landform': random.choice(landforms), 'nation': bNation, 'people': [], 'items': []}
  c1 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c2 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c3 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c4 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c5 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c6 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c7 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c8 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c9 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c10 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c11 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c12 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c13 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c14 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c15 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c16 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c17 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c18 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c19 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c20 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c21 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c22 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c23 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c24 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  c25 = {'landform': random.choice(landforms), 'nation': cNation, 'people': [], 'items': []}
  d1 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d2 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d3 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d4 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d5 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d6 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d7 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d8 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d9 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d10 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d11 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d12 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d13 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d14 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d15 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d16 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d17 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d18 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d19 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d20 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d21 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d22 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d23 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d24 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  d25 = {'landform': random.choice(landforms), 'nation': dNation, 'people': [], 'items': []}
  A1 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A2 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A3 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A4 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A5 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A6 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A7 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A8 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A9 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A10 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A11 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A12 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A13 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A14 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A15 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A16 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A17 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A18 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A19 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A20 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A21 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A22 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A23 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A24 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A25 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A26 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A27 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A28 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A29 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A30 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A31 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A32 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A33 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A34 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A35 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A36 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A37 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A38 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A39 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A40 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A41 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A42 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A43 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A44 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A45 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A46 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A47 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A48 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A49 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A50 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A51 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  A52 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B1 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B2 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B3 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B4 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B5 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B6 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B7 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B8 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B9 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B10 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B11 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B12 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B13 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B14 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B15 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B16 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B17 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B18 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B19 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B20 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B21 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B22 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B23 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B24 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B25 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B26 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B27 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B28 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B29 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B30 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B31 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B32 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B33 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B34 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B35 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B36 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B37 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B38 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B39 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B40 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B41 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B42 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B43 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  B44 = {'landform': random.choice(coastal_landforms), 'people': [], 'items': []}
  map = [[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10,A11,A12,A13,A14],
         [A52,B1, B2, B3, B4, B5, B6, B7, B8, B9, B10,B11,B12,A15],
         [A51,B44,a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, B13,A16],
         [A50,B43,a6, a7, a8, a9, a10,b6, b7, b8, b9, b10,B14,A17],
         [A49,B42,a11,a12,a13,a14,a15,b11,b12,b13,b14,b15,B15,A18],
         [A48,B41,a16,a17,a18,a19,a20,b16,b17,b18,b19,b20,B16,A19],
         [A47,B40,a21,a22,a23,a24,a25,b21,b22,b23,b24,b25,B17,A20],
         [A46,B39,d1, d2, d3, d4, d5, c1, c2, c3, c4, c5, B18,A21],
         [A45,B38,d6, d7, d8, d9, d10,c6, c7, c8, c9, c10,B19,A22],
         [A44,B37,d11,d12,d13,d14,d15,c11,c12,c13,c14,c15,B20,A23], 
         [A43,B36,d16,d17,d18,d19,d20,c16,c17,c18,c19,c20,B21,A24],
         [A42,B35,d21,d22,d23,d24,d25,c21,c22,c23,c24,c25,B22,A25],
         [A41,B34,B33,B32,B31,B30,B29,B28,B27,B26,B25,B24,B23,A26],
         [A40,A39,A38,A37,A36,A35,A34,A33,A32,A31,A30,A29,A28,A27]]
  return map