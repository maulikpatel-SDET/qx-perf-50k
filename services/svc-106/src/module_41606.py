"""Service module 41606: business logic, no crypto."""


def calculate_total_41606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41606():
    return 'module 41606 handles orders and invoices'
