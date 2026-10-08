"""Service module 49706: business logic, no crypto."""


def calculate_total_49706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49706():
    return 'module 49706 handles orders and invoices'
