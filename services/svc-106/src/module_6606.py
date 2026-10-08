"""Service module 6606: business logic, no crypto."""


def calculate_total_6606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6606():
    return 'module 6606 handles orders and invoices'
