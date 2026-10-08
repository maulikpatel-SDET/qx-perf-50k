"""Service module 25174: business logic, no crypto."""


def calculate_total_25174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25174():
    return 'module 25174 handles orders and invoices'
