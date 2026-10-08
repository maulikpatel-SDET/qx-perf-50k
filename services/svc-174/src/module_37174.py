"""Service module 37174: business logic, no crypto."""


def calculate_total_37174(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37174():
    return 'module 37174 handles orders and invoices'
