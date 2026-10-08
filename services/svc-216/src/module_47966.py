"""Service module 47966: business logic, no crypto."""


def calculate_total_47966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47966():
    return 'module 47966 handles orders and invoices'
