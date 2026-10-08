"""Service module 6935: business logic, no crypto."""


def calculate_total_6935(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6935():
    return 'module 6935 handles orders and invoices'
