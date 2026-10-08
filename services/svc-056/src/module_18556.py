"""Service module 18556: business logic, no crypto."""


def calculate_total_18556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18556():
    return 'module 18556 handles orders and invoices'
