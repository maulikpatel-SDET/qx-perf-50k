"""Service module 24556: business logic, no crypto."""


def calculate_total_24556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24556():
    return 'module 24556 handles orders and invoices'
