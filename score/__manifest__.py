{
    'name': 'score',  #nama modul yg dibaca user di UI
    'version': '1.0',
    'author': 'Ivonne',
    'summary': 'Modul Nilai SIB UK Petra', #deskripsi singkat dari modul
    'description': 'Score management module', #bisa nampilkan gambar/ deskripsi dalam bentuk html. html diletakkan
    #di idea/static/description, bisa kasi icon modul juga.
    'category': 'Latihan',
    'website': 'http://sib.petra.ac.id',
    'depends': ['base', 'sales_team'],  # list of dependencies, conditioning startup order
    'data': [
        'security/ir.model.access.csv',
        'views/mahasiswa_views.xml',
        'views/khs_views.xml',
        'views/mk_views.xml',
        'views/detail_views.xml',
        'views/kelas_views.xml',
        'wizard/wiz_nilai_kelas_views.xml',
    ],
    'qweb':[],  #untuk memberi tahu static file, misal CSS
    'demo': [], #demo data (for unit tests)
    'installable': True,
    'auto_install': False,  # indikasi install, saat buat database baru
}