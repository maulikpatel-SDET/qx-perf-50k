"""Service module 36174: business logic, no crypto."""


def calculate_total_36174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36174():
    return 'module 36174 handles orders and invoices'
