title = input()
print("<h1>")
print(f"    {title}")
print("</h1>")
article = input()
print("<article>")
print(f"    {article}")
print("</article>")
comment = input()
while comment != 'end of comments':
    print("<div>")
    print(f"    {comment}")
    print("</div>")
    comment = input()