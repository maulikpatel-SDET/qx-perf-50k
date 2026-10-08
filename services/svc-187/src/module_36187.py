"""Service module 36187: business logic, no crypto."""


def calculate_total_36187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36187():
    return 'module 36187 handles orders and invoices'
