"""Service module 27548: business logic, no crypto."""


def calculate_total_27548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27548():
    return 'module 27548 handles orders and invoices'
