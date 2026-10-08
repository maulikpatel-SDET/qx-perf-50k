"""Service module 27797: business logic, no crypto."""


def calculate_total_27797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27797():
    return 'module 27797 handles orders and invoices'
