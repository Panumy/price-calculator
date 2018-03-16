from Tkinter import Listbox,Tk,FALSE,Scrollbar,RIGHT,LEFT,Y,END,mainloop

master = Tk()
master.wm_title("SOLS Object Price Calc")
master.resizable(width=FALSE, height=FALSE)

output_file = open("objects.txt", 'r')
final = 0
objects = 0
st = []
for line in output_file:
    s = line.replace('CreateDynamicObject(', '').replace(');','')
    s = s.strip().split(',')
    s = int(s[0])
    price = 0
    if s >= 321 and s <= 373: price = 500
    elif s >= 615 and s <= 624: price = 1300
    elif s >= 625 and s <= 653: price = 750
    elif s >= 654 and s <= 674: price = 1400
    elif s >= 675 and s <= 679: price = 700
    elif s >= 680 and s <= 681: price = 1400
    elif s == 682: price = 700
    elif s >= 683 and s <= 740: price = 1200
    elif s >= 741 and s <= 743: price = 700
    elif s >= 744 and s <= 752: price = 1000
    elif s >= 753 and s <= 757: price = 750
    elif s >= 758 and s <= 792: price = 1100
    elif s >= 793 and s <= 833: price = 750
    elif s >= 834 and s <= 848: price = 900
    elif s >= 849 and s <= 880: price = 750
    elif s >= 881 and s <= 895: price = 1200
    elif s >= 896 and s <= 906: price = 750
    elif s >= 907 and s <= 913: price = 1100
    elif s >= 914 and s <= 928: price = 900
    elif s >= 929 and s <= 931: price = 1100
    elif s >= 932 and s <= 933: price = 750
    elif s == 934: price = 1100
    elif s >= 935 and s <= 968: price = 1100
    elif s == 969: price = 1200
    elif s == 970: price = 750
    elif s >= 971 and s <= 993: price = 1300
    elif s >= 994 and s <= 998: price = 800
    elif s >= 999 and s <= 1208: price = 650
    elif s == 1209: price = 950
    elif s >= 1210 and s <= 1258: price = 850
    elif s >= 1259 and s <= 1260: price = 1400
    elif s >= 1261 and s <= 1265: price = 750
    elif s == 1267: price = 1400
    elif s >= 1268 and s <= 1377: price = 900
    elif s >= 1378 and s <= 1395: price = 1600
    elif s >= 1396 and s <= 1540: price = 950
    elif s >= 1541 and s <= 1569: price = 700
    elif s >= 1570 and s <= 1571: price = 1300
    elif s >= 1572 and s <= 1630: price = 800
    elif s >= 1631 and s <= 1639: price = 1200
    elif s >= 1640 and s <= 1663: price = 750
    elif s >= 1664 and s <= 1672: price = 500
    elif s >= 1673 and s <= 1664: price = 1100
    elif s == 1675 or s == 1677: price = 23000
    elif s == 1676: price = 1600
    elif s == 1679: price = 850
    elif s >= 1680 and s <= 1684: price = 14000
    elif s >= 1685 and s <= 1701: price = 950
    elif s >= 1702 and s <= 1713: price = 850
    elif s >= 1714 and s <= 1722: price = 500
    elif s == 1723 or s == 1726 or s == 1728: price = 950
    elif s >= 1724 and s <= 1725: price = 800
    elif s == 1727 or s == 1729: price = 750
    elif s >= 1730 and s <= 1752: price = 800
    elif s >= 1753 and s <= 1804: price = 850
    elif s >= 1805 and s <= 1811: price = 650
    elif s >= 1812 and s <= 1828: price = 750
    elif s >= 1829 and s <= 1850: price = 900
    elif s >= 1851 and s <= 1882: price = 300
    elif s >= 1883 and s <= 1898: price = 800
    elif s >= 1899 and s <= 1962: price = 650
    elif s >= 1963 and s <= 1967: price = 1500
    elif s >= 1968 and s <= 1974: price = 850
    elif s >= 1805 and s <= 2211: price = 950
    elif s >= 2212 and s <= 2223: price = 350
    elif s >= 2224 and s <= 2253: price = 950
    elif s >= 2254 and s <= 2289: price = 450
    elif s >= 2290 and s <= 2669: price = 950
    elif s >= 2670 and s <= 2742: price = 450
    elif s >= 2743 and s <= 2745: price = 1750
    elif s >= 2746 and s <= 2748: price = 950
    elif s >= 2749 and s <= 2811: price = 750
    elif s >= 2812 and s <= 2870: price = 450
    elif s >= 2871 and s <= 2879: price = 750
    elif s >= 2880 and s <= 3134: price = 850
    elif s >= 3135 and s <= 3281: price = 9500
    st.append("Model {} | Price ${}\n".format(s,price))
    final = final + price
    objects = objects + 1

st.append("|-----------------------------------------------|\n")
st.append("Total Objects: {} | Total Price: ${}".format(objects,final))

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(master,width=40,height=40)
listbox.pack()
for item in st:
    listbox.insert(END, item)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
mainloop()
