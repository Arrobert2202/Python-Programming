def build_xml_element(tag, content, **key_value):
  string = f"<{tag}"

  for name, parameter in key_value.items():
    string += f' {name}="{parameter}"'

  string += f">{content}</{tag}>"
  return string

print(build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))