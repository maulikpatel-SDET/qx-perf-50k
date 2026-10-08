"""Service module 48978: business logic, no crypto."""


def calculate_total_48978(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48978():
    return 'module 48978 handles orders and invoices'
