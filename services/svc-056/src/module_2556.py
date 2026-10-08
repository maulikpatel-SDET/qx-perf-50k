"""Service module 2556: business logic, no crypto."""


def calculate_total_2556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2556():
    return 'module 2556 handles orders and invoices'
