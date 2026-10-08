"""Service module 35174: business logic, no crypto."""


def calculate_total_35174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35174():
    return 'module 35174 handles orders and invoices'
