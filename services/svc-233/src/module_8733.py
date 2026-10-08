"""Service module 8733: business logic, no crypto."""


def calculate_total_8733(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8733():
    return 'module 8733 handles orders and invoices'
