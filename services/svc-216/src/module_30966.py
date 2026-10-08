"""Service module 30966: business logic, no crypto."""


def calculate_total_30966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30966():
    return 'module 30966 handles orders and invoices'
