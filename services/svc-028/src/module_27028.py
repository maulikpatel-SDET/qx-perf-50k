"""Service module 27028: business logic, no crypto."""


def calculate_total_27028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27028():
    return 'module 27028 handles orders and invoices'
