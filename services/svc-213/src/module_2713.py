"""Service module 2713: business logic, no crypto."""


def calculate_total_2713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2713():
    return 'module 2713 handles orders and invoices'
