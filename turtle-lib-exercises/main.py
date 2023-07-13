import turtle

drawing_board = turtle.Screen() #çizim için ekran oluşturur.
drawing_board.bgcolor("green") #çizim tahtamızın arka planını oluşturur.
#renk için hex code verebilirsin.
#google'a 'color hex codes' yazıp 'HTML COLOR CODES' Sitesinden yapabilirsin
#hex code'un başına # koyman lazım
drawing_board.title("Python Turtle") #tahtanın pencere başlığı

'''
my_turtle_instance = turtle.Turtle() #çizimi yapacak olan şeyin adı
my_turtle_instance.forward(100) #100 pixel ileri git

my_turtle_instance_2 = turtle.Turtle() #başka bir çizim yapan nesne
my_turtle_instance_2.left(45) #önce 45 derece sola dön,
my_turtle_instance_2.forward(100) #sonra ilerle
'''

#kare çizelim
#seçenek-1
'''
square_drawing_turtle = turtle.Turtle()
square_drawing_turtle.forward(200) #ilerle
square_drawing_turtle.right(90) #sağa 90 derece dön
square_drawing_turtle.forward(200)
square_drawing_turtle.right(90)
square_drawing_turtle.forward(200)
square_drawing_turtle.right(90)
square_drawing_turtle.forward(200)


#seçenek-2
square_drawing_turtle = turtle.Turtle()
for i in range(4):
    square_drawing_turtle.forward(200) #ilerle
    square_drawing_turtle.right(90) #sağa 90 derece dön
'''

#çokgen çizelim
'''
star_drawing_turtle = turtle.Turtle()
num_of_sides = 5
angle = 360.0 / num_of_sides
side_length = 200

for i in range(5):
    star_drawing_turtle.forward(side_length)
    star_drawing_turtle.left(angle)
'''
'''
#yıldız çizelim
star_drawing_turtle = turtle.Turtle()
num_of_sides = 5
angle = 2*(360 / num_of_sides)
side_length = 200

for i in range(5):
    star_drawing_turtle.forward(side_length)
    star_drawing_turtle.left(angle)
'''
turtle.done() #bitiş, en son

