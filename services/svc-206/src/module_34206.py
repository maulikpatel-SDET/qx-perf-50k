"""Service module 34206: business logic, no crypto."""


def calculate_total_34206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34206():
    return 'module 34206 handles orders and invoices'
