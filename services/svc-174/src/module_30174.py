"""Service module 30174: business logic, no crypto."""


def calculate_total_30174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30174():
    return 'module 30174 handles orders and invoices'
