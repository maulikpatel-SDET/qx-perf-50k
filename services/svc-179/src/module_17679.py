"""Service module 17679: business logic, no crypto."""


def calculate_total_17679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17679():
    return 'module 17679 handles orders and invoices'
