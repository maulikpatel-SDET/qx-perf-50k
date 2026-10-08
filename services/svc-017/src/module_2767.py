"""Service module 2767: business logic, no crypto."""


def calculate_total_2767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2767():
    return 'module 2767 handles orders and invoices'
