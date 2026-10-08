"""Service module 33329: business logic, no crypto."""


def calculate_total_33329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33329():
    return 'module 33329 handles orders and invoices'
