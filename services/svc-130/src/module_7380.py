"""Service module 7380: business logic, no crypto."""


def calculate_total_7380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7380():
    return 'module 7380 handles orders and invoices'
