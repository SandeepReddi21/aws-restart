#fibonacci of first 25 numbers
fi1 = 0
fi2 = 1
print(fi1)
print(fi2)
for i in range(23):
    fi = fi1 + fi2
    print(fi)
    fi1 = fi2
    fi2 = fi