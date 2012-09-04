import time

arreglo = [5, 2, 52, 1, 15, 99, 10, 35, 56, 88]
print "Arreglo ingresado: "
print arreglo
def tiempo(func):
def wrapper(*arg):
t1 = time.clock()
res = func(*arg)
t2 = time.clock()
print '%s se tomo %0.3fms' % (func.func_name, (t2-t1)*1000.0)
return res
return wrapper


@tiempo
def mergesort(arr):
    if len(arr) == 1:
        return arr
          
    m = len(arr) / 2
    l = mergesort(arr[:m])
    r = mergesort(arr[m:])
      
    if not len(l) or not len(r):
        return l or r
              
    result = []
    i = j = 0
    while (len(result) < len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
              
    return result

print "Resultado: "
print mergesort(arreglo)
raw_input()