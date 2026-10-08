"""Service module 33606: business logic, no crypto."""


def calculate_total_33606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33606():
    return 'module 33606 handles orders and invoices'
