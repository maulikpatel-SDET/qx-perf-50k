"""Service module 9541: business logic, no crypto."""


def calculate_total_9541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9541():
    return 'module 9541 handles orders and invoices'
