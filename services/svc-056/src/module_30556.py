"""Service module 30556: business logic, no crypto."""


def calculate_total_30556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30556():
    return 'module 30556 handles orders and invoices'
