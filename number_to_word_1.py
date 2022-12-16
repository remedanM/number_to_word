numbers = {
            1: 'One',	2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',	6: 'Six', 7: 'Seven', 8: 'Eight',
            9: 'Nine',	10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',	14: 'Fourteen',
            15: 'Fifteen',	16: 'Sixteen', 17: 'Seventeen',	18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
            30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 100: 'One hundred'
}
help_menu = '''     This program only works with numbers less than 100 and 100.
         To change numbers in digit to number in words enter the digit.
         To close the program enter quit.
                               .....ThankYou.....
'''
print(help_menu, end=' ')
while True:
    num = int(input('Enter number here: '))
    if num == 'quit':
        break
    num = int(num)
    if num <= 100:
        if num in numbers:
            k = numbers.get(num)
            print(f'>>> {num} in words is: {k}')
        else:
            b = num % 10
            b = numbers.get(b)
            c = num // 10
            c = c * 10
            c = numbers.get(c)
            result = f'>>> {num} in words is:{c}-{b}'
            print(result)
    else:
        if num > 100:
            print('Please Enter a number between 1 and 100')
