ui_file = 'main.ui'
db_name = 'coffee.sqlite'
query = """\
SELECT variety,
       roasting.[roasting degree],
       bean_state.[bean state],
       "taste description",
       price,
       "package volume"
  FROM coffee
       JOIN
       roasting ON roasting.id = coffee.roasting
       JOIN
       bean_state ON bean_state.id = coffee.[bean state];
"""