def string_to_list(your_str):
  out = []
  buff = []
  for c in your_str:
      if c == '\n':
          out.append(''.join(buff))
          buff = []
      else:
          buff.append(c)
  else:
      if buff:
        out.append(''.join(buff))

  return out