"""Service module 33997: business logic, no crypto."""


def calculate_total_33997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33997():
    return 'module 33997 handles orders and invoices'
