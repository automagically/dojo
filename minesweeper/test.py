from main import Minesweeper

def test_no_input():
    lines = 0
    columns = 0
    field = None
    assert Minesweeper().parse_field(lines, columns, field) == ""

def test_1_x_1():
    lines = 1
    columns = 1
    field1 = [['*']]
    field2 = [['.']]
    
    parser = Minesweeper()

    assert parser.parse_field(lines, columns, field1) == "Field #1:\n*\n"
    assert parser.parse_field(lines, columns, field2) == "Field #2:\n0\n"

def test_4_x_4():
    lines = 4
    columns = 4
    field = [["*",".",".","."],
             [".",".",".","."],
             [".","*",".","."],
             [".",".",".","."]]
    
    parser = Minesweeper()

    assert parser.parse_field(lines, columns, field) == 'Field #1:\n*100\n2210\n1*10\n1110\n'
    
def test_3_x_5():
    lines = 3
    columns = 5
    field= [ ["*","*",".",".","."],
             [".",".",".",".","."],
             [".","*",".",".","."]]

    parser = Minesweeper()

    assert parser.parse_field(lines, columns, field) == "Field #1:\n**100\n33200\n1*100\n"

            
