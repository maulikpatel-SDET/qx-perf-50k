"""Service module 11851: business logic, no crypto."""


def calculate_total_11851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11851():
    return 'module 11851 handles orders and invoices'
