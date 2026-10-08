"""Service module 46720: business logic, no crypto."""


def calculate_total_46720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46720():
    return 'module 46720 handles orders and invoices'
