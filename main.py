from flask import Flask, render_template, request, redirect, url_for
from BUS.datsan_bus import SanBus
from DAO.datsan_dao import SanDAO
from DAO.db_config import get_connection

# Khởi tạo Flask app
app = Flask(__name__, template_folder='GUI')

# Khởi tạo connection, DAO và BUS trước khi định nghĩa route
conn = get_connection()
dao = SanDAO(conn)  # Truyền conn từ get_connection()
san_bus = SanBus(dao)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/san')
def quan_ly_san():
    # Lấy danh sách sân từ SanBus
    danh_sach_san = san_bus.lay_danh_sach_san()
    # Truyền danh sách sân vào template san.html
    return render_template('san.html', danh_sach_san=danh_sach_san)

# Định nghĩa route
@app.route('/them-san', methods=['POST'])
def them_san():
    co_san = request.form.get('coSan')
    dia_chi = request.form.get('diaChi')
    result = san_bus.them_san({'coSan': co_san, 'diaChi': dia_chi})
    if isinstance(result, dict) and 'idSan' in result:  # Sử dụng 'idSan' thay vì 'id'
        danh_sach_san = san_bus.lay_danh_sach_san()
        print(f"Danh sách sân sau khi thêm: {danh_sach_san}")
        return render_template('san.html', danh_sach_san=danh_sach_san, success=True, idSan=result['idSan'])
    print(f"Thêm sân thất bại, result: {result}")
    return redirect(url_for('quan_ly_san'))

@app.route('/xoa-san/<int:id_san>')
def xoa_san(id_san):
    san_bus.xoa_san(id_san)
    return redirect(url_for('quan_ly_san'))

if __name__ == '__main__':
    app.run(debug=True)