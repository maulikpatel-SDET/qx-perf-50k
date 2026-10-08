"""Service module 28966: business logic, no crypto."""


def calculate_total_28966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28966():
    return 'module 28966 handles orders and invoices'
