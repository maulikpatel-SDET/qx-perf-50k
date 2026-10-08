"""Service module 15206: business logic, no crypto."""


def calculate_total_15206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15206():
    return 'module 15206 handles orders and invoices'
