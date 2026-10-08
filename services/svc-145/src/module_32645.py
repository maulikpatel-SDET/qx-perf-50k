"""Service module 32645: business logic, no crypto."""


def calculate_total_32645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32645():
    return 'module 32645 handles orders and invoices'
