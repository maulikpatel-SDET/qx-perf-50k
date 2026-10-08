"""Service module 49692: business logic, no crypto."""


def calculate_total_49692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49692():
    return 'module 49692 handles orders and invoices'
