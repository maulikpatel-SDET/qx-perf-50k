"""Service module 32713: business logic, no crypto."""


def calculate_total_32713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32713():
    return 'module 32713 handles orders and invoices'
