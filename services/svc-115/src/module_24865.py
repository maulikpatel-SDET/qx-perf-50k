"""Service module 24865: business logic, no crypto."""


def calculate_total_24865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24865():
    return 'module 24865 handles orders and invoices'
