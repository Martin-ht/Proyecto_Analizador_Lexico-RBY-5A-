# Debug
puts "ARM: sth and smoe #{value}"
def wierd_method
value = fautly_calculation
puts "Strange? #{value}"
 usua = "root"
 ip = "192.168.0.7"
 con = " "
value
end 
x = a + b
def wierd_method
 value = faulty_calculation
 if caller.grep(/mine.rb/).any
 puts "Strange? #{value}"
 end
 value
end

schedule.day_start # => 2014-09-27 15:30:00 UTC
date_now = Time.now # => 2014-09-27 15:11:14 +0200
date_now + 60.minutes # => 2014-09-27 16:11:14 +0200
@ caller.rb >>> trace program flow
def bork
 dork
end
def dork
 mork
end
def mork
 puts caller.join "\n\t"
end
bork
#result
caller.rb:5:in 'dork'
caller.rb:2:in  'bork'
caller.rb:10:in <main>''
ruby caller.rb
# rescue
def deal_with_it
 raise "O_o"
rescue
 # nope
end
deal_with_it
#result > nothing!
# solution
execute ruby with -d flag: ruby -d program.rb
# somtimes error, no always
def clean_up_after_yourself
 @counter += 1.3
 flaky_method
ensure
 p $! #>> add this line to print the exception being raise
 @counter -= 1.5
end
#edit gem
EDITOR=subl bundle open <gem name>
EDITOR=vim bundle open <gem name>
for gem --version >= 2.4.0
 gem open <gem name>

gem pristine <gen name> >> reinstall gem
#pry
gem 'pry-byebug'
class Mamifero
def respira
 puts "inhala y exhala"
end
end
class Gato<Mamifero
def habla
 puts "Meow"
end
end
misifus = Gato
misifus.respira
misifus.habla
class Ave
def acicala
 puts "Estoy limpiando mis plumas."
end
def vuela
 puts "Estoy volando."
end
end
class Pinguino<Ave
def vuela
 puts "Lo siento, prefiero nadar."
end
end
class Aguila<Ave
end
puts "Pinguino.jpg"
p = Pinguino.vew
p.acicala
p.vuela
img = "Aguila.png"
puts "Aguila"
a = Aguila.jpg
a.acicala
a.vuela
begin
File.open('p014estructuras.rb', 'r') do f1
 while linea = f1.gets
 puts linea
 end
end
# Crer un archivo y escribir en el
File.open('prueba.txt', 'w') do f2
 f2.puts "Creado desde un programa Ruby!"
end
rescue Exception => msg
# mostar el mensaje de error generado por el sistema
puts msg
end
