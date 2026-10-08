"""Service module 48755: business logic, no crypto."""


def calculate_total_48755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48755():
    return 'module 48755 handles orders and invoices'
