"""Service module 28692: business logic, no crypto."""


def calculate_total_28692(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28692():
    return 'module 28692 handles orders and invoices'
