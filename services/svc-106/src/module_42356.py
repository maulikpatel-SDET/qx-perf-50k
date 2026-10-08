"""Service module 42356: business logic, no crypto."""


def calculate_total_42356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42356():
    return 'module 42356 handles orders and invoices'
