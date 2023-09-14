class DataOutput:

    def __init__(self) -> None:
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('baike.html', 'w', encoding='utf-8') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table>')
            for data in self.datas:
                f.write('<tr>')
                f.write('<td>{}</td>'.format(data['url']))
                f.write('<td>{}</td>'.format(data['title']))
                f.write('<td>{}</td>'.format(data['summary']))
                f.write('</tr>')
                self.datas.remove(data)
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
