"""Service module 37999: business logic, no crypto."""


def calculate_total_37999(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37999():
    return 'module 37999 handles orders and invoices'
