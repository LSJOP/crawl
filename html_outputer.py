#-*-coding:utf-8-*-

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html','w')

		fout.write("<html>")
		fout.write("<body>")
		fout.write("<table>") #表格标签

		for data in self.datas:
			fout.write("<tr>")  										#行标签
			fout.write("<td>%s</td>" % data['url'])						#单元格
			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</html>")
		fout.write("</html>")

		fout.close()