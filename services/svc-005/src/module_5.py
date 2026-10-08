"""Service module 5: business logic, no crypto."""


def calculate_total_5(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5():
    return 'module 5 handles orders and invoices'
