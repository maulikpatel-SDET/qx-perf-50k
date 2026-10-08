"""Service module 17906: business logic, no crypto."""


def calculate_total_17906(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17906():
    return 'module 17906 handles orders and invoices'
