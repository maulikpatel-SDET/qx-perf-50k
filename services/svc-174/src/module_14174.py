"""Service module 14174: business logic, no crypto."""


def calculate_total_14174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14174():
    return 'module 14174 handles orders and invoices'
