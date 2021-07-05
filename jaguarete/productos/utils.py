def stock_avg(stock_total):
    if not stock_total:
        return 0

    return round(sum(stock_total)/len(stock_total)) # Permite calcular la media del stock del producto.
