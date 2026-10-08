"""Service module 42206: business logic, no crypto."""


def calculate_total_42206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42206():
    return 'module 42206 handles orders and invoices'
