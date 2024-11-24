import random
from weasyprint import HTML, CSS

#	Settings
filename = "questions.txt"
numberOfCards = 100

#	Read in the questions
with open( filename ) as file:
	questions = [ line.rstrip() for line in file ]

#	Start the HTML
bodyHTML = "<body>\n"

#	Loop for the total number of cards
for card in range( numberOfCards ):
	#	Start the table
	bodyHTML += """
<table>
	<thead>
		<tr>
			<th colspan="5">Find someone who...</th>
		</tr>
	</thead>
	<tbody>
"""
	#	Random sample of 25 questions
	cardQuestions = random.sample( questions, 25 )
	#	5x5 grid
	rowLength = 5
	#	Write each row
	for i in range( 0, len( cardQuestions ), rowLength ):
		rowQuestions = cardQuestions[ i:i+rowLength ]
		bodyHTML += "<tr>\n\t"
		for question in rowQuestions :
			bodyHTML += "<td>" + question + "</td>\n"
		bodyHTML += "</tr>"
	#	Close the table
	bodyHTML += """
<tr>
	<td colspan="5" id="footer">Mandatory Fun Time Bingo<br><br>
Write your name here:___________________________________________________<br>
In each square, write the name of someone who meets the description.<br>
Find a volunteer when you have completed your sheet.<br>
For more information, please re-read.</td>
</tr>
</tbody>
</table>
"""

#	Finish the body
bodyHTML += "\n</body></html>"

#	Standard HTML head
headHTML = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Mandatory Fun Time</title>
</head>
"""

#	Stick the HTML togeth
pageHTML = headHTML + bodyHTML

#	Create the PDF in A4 with appropriate CSS
HTML(string = pageHTML).write_pdf( "Bingo Sheets.pdf",
    stylesheets=[CSS( string="""
	 @page { size: A4; margin: .5cm }
	 table {
				background-color: black;
				border-collapse: collapse;
				margin-bottom: 1em;
				float: left;
				page-break-after: always; 
				page-break-before: always; 
			}
			table		{
				table-layout: fixed;
			}
			td,th {
				border: .2em solid black;
				text-align: center;
			}
			th {
				color: white;
				font-family: sans;
				font-size: 3em;
			}
			td {
				background-color: white;
				min-height: 9em;
				height: 9em;
				vertical-align: text-top;
				padding: .5em;
				font-size: 1em;
				font-family: sans;
				font-weight: bold;
				min-width: 20%;
			}
			#footer {
				border-top: 1px solid #ccc;
				clear: both;
				height:1em;
			}
		}
	 """
)])