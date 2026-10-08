"""Service module 18356: business logic, no crypto."""


def calculate_total_18356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18356():
    return 'module 18356 handles orders and invoices'
