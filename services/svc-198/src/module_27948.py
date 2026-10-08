"""Service module 27948: business logic, no crypto."""


def calculate_total_27948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27948():
    return 'module 27948 handles orders and invoices'
