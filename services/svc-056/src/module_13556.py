"""Service module 13556: business logic, no crypto."""


def calculate_total_13556(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13556():
    return 'module 13556 handles orders and invoices'
