# Online Python compiler (interpreter) to run Python online.

# print("|Reference|Xinet|Phinet|Vocos|")
# print("|---|---|---|---|")

# print("|")

text = ["In the next sections you are going to hear a lot of dystopian fiction quotes",
        "Reality is that which, when you stop believing in it, doesn't go away.",
        "You don't have to burn books to destroy a culture. Just get people to stop reading them.",
        "We've got to have rules and obey them. After all, we're not savages.",
        "The greatest ideas are the simplest.",
        "In a time of deceit, telling the truth is a revolutionary act.",
        "If liberty means anything at all, it means the right to tell people what they do not want to hear.",
        "All animals are equal, but some animals are more equal than others."]
        
print("<table>")
print("""
    <tr>
        <th> Text </th>
        <th> Waveglow </th>
        <th> Xinet </th>
        <th> Phinet </th>
        <th> Vocos </th>
    </tr>
""")
for i, t in enumerate(text):
    print("<tr>")
    print(f"<td> {t} </td>")
    for folder in ["waveglow", "xinet", "phinet", "vocos"]:
        url = "'resources/tinyvocos_audio_out/tacotron/"+folder+"/"+str(i)+".mp3'"
        
        html = f"""
            <audio controls>
              <source src="{{{{ {url} | url_for }}}}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        """
        print("<td>")
        print(html)
        print("</td>")
    
    print("</tr>")

print("</table>")

        
        