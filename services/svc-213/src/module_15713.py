"""Service module 15713: business logic, no crypto."""


def calculate_total_15713(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15713():
    return 'module 15713 handles orders and invoices'
