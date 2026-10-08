"""Service module 21541: business logic, no crypto."""


def calculate_total_21541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21541():
    return 'module 21541 handles orders and invoices'
