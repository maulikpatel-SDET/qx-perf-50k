"""Service module 13966: business logic, no crypto."""


def calculate_total_13966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13966():
    return 'module 13966 handles orders and invoices'
