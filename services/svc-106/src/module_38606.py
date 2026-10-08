"""Service module 38606: business logic, no crypto."""


def calculate_total_38606(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38606():
    return 'module 38606 handles orders and invoices'
