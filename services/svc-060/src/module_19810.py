"""Service module 19810: business logic, no crypto."""


def calculate_total_19810(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19810():
    return 'module 19810 handles orders and invoices'
