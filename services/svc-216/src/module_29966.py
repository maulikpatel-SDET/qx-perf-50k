"""Service module 29966: business logic, no crypto."""


def calculate_total_29966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29966():
    return 'module 29966 handles orders and invoices'
