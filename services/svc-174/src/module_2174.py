"""Service module 2174: business logic, no crypto."""


def calculate_total_2174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2174():
    return 'module 2174 handles orders and invoices'
