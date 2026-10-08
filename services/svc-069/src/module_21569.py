"""Service module 21569: business logic, no crypto."""


def calculate_total_21569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21569():
    return 'module 21569 handles orders and invoices'
