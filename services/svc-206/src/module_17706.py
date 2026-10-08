"""Service module 17706: business logic, no crypto."""


def calculate_total_17706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17706():
    return 'module 17706 handles orders and invoices'
