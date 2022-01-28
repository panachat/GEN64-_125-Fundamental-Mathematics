chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
input_text = int(input("Enter your number : "))
text = []

for c in range(input_text):
    text.append(input("Enter : your text : "))
n = input("Enter : ")

for x in text:
    for i in range (len(chars)):
        if x == chars[i]: #TODO ถ้าไม่ใส่ชื่อตัวแปรของ list ข้างหน้ามันจะเป็น เลข ถ้าใส่มันจะเป็นค่าใน list
            if n == 'g':
                rot = (i + 13)%26
                print(chars[rot],end='')
            elif n == 'f':
                rot = (i + 3)%26
                print(chars[rot],end='')
        

        
