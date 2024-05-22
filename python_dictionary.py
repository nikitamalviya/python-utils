# update dictionary --> merge dict1 into dict2
dict1.update(dict2)

# sort the dictionary key's values and pretty print the text    
classes_count = {}
classes_count = sorted(classes_count.items(), key=lambda item: item[1], reverse=True)
click.secho(f"Sorted dictionary : ", fg="green")
pprint(classes_count)
