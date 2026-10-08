"""Service module 26966: business logic, no crypto."""


def calculate_total_26966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26966():
    return 'module 26966 handles orders and invoices'
