"""Service module 2606: business logic, no crypto."""


def calculate_total_2606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2606():
    return 'module 2606 handles orders and invoices'
