#FLM: AT Marcar Problemas
for g in fl.font.glyphs:
  l = len(g.Audit())
  if l > 25:
    g.mark = 1
  else:
    g.mark = l * 10

fl.UpdateGlyph(-1)
